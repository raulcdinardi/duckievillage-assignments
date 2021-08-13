# MAC0318 Intro to Robotics
# Please fill-in the fields below with your info
#
# Name:
# NUSP:
#
# ---
#
# Assignment 3 - Braitenberg vehicles for lane following
#
# Task:
#  - Implement a reactive agent that implements the "lover" behaviour of Braitenberg's vehicle on
#  the task of lane following.
# Your agent should be able to go up a lane by reacting to the markings on the road. Construct a
# color filter to identify road markings and use the lover behavior to maintain a short distance
# from them.
#
# Don't forget to run this from the Duckievillage root directory (example):
#   cd ~/MAC0318/duckievillage
#   python3 assignments/braitenberg/lane_following.py
#
# Submission instructions:
#  0. Add your name and USP number to the file header above.
#  1. Make sure that any last change haven't broken your code. If the code chrases without running you'll get a 0.
#  2. Submit this file via e-disciplinas.
#  3. Push changes to your git fork.

import sys
import pyglet
import numpy as np
from pyglet.window import key
from duckievillage import create_env
import cv2

class Agent:
    # Agent initialization
    def __init__(self, environment):
        """ Initializes agent """
        self.env = environment
        # Color segmentation hyperspace
        self.inner_lower = np.array([20, 85, 20])
        self.inner_upper = np.array([30, 255, 255])
        self.outer_lower = np.array([180, 180, 180])
        self.outer_upper = np.array([255, 255, 255])
        # Acquire image for initializing activation matrices
        img = self.env.front()
        img_shape = img.shape[0], img.shape[1]
        self.inner_left_motor_matrix = np.zeros(shape=img_shape, dtype="float32")
        self.inner_right_motor_matrix = np.zeros(shape=img_shape, dtype="float32")
        self.outer_left_motor_matrix = np.zeros(shape=img_shape, dtype="float32")
        self.outer_right_motor_matrix = np.zeros(shape=img_shape, dtype="float32")
        # TODO! Replace with your code
        self.inner_left_motor_matrix[:, :img_shape[1]//2] = 1

    # Image processing routine - Color segmentation
    def preprocess(self, image: np.ndarray) -> np.ndarray:
        """ Returns a 2D array mask color segmentation of the image """
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        inner_mask = cv2.inRange(hsv, self.inner_lower, self.inner_upper)//255
        outer_mask = cv2.inRange(image, self.outer_lower, self.outer_upper)//255
        mask = cv2.bitwise_or(inner_mask, outer_mask)
        self.masked = cv2.bitwise_and(image, image, mask=mask)
        return inner_mask, outer_mask, mask

    def send_commands(self, dt):
        ''' Agent control loop '''
        # acquire front camera image
        img = self.env.front()
        # run image processing routines
        P, Q, M = self.preprocess(img)
        # build left and right signals
        L = float(np.sum(P * self.inner_left_motor_matrix)) + float(np.sum(Q * self.outer_left_motor_matrix))
        R = float(np.sum(P * self.inner_right_motor_matrix)) + float(np.sum(Q * self.outer_right_motor_matrix))
        limit = img.shape[0]*img.shape[1]*2
        # These are big numbers, thus rescale them to unit interval
        L = rescale(L, 0, limit)
        R = rescale(R, 0, limit)
        # Tweak with the constants below to get to change velocity or stabilize movements
        # Recall that pwm sets wheel torque, and is capped to be in [-1,1]
        gain = 3.0
        const = 0.15 # power under null activation - this ensures the robot does not halt
        pwm_left = const + R * gain
        pwm_right = const + L * gain
        # print('>', L, R, pwm_left, pwm_right) # uncomment for debugging
        # Now send command
        self.env.step(pwm_left, pwm_right)
        self.env.render('human')


def rescale(x: float, L: float, U: float):
    ''' Map scalar x in interval [L, U] to interval [0, 1]. '''
    return (x - L) / (U - L)


def main():
    print("MAC0318 - Assignment 3")
    env = create_env(
      raw_motor_input = True,
      seed = 101,
      map_name = './maps/loop_empty.yaml',
      draw_curve = False,
      draw_bbox = False,
      domain_rand = False,
      #color_sky = [0, 0, 0],
      user_tile_start = (0, 0),
      distortion = False,
      top_down = False,
      cam_height = 10,
      is_external_map = True,
    )

    angle = env.unwrapped.cam_angle[0]

    env.start_pose = [[0.8, 0, 0.8], 4.5]
    env.reset()
    env.render('human')

    @env.unwrapped.window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.ESCAPE: # exit simulation
            env.close()
            sys.exit(0)
        elif symbol == key.BACKSPACE or symbol == key.SLASH: # reset simulation
            print("RESET")
            env.reset()
        elif symbol == key.RETURN:  # Take a screenshot
            print('saving screenshot')
            img = env.render('rgb_array')
            cv2.imwrite(f'screenshot-{env.unwrapped.step_count}.png', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        env.render()

    # Instantiate agent
    agent = Agent(env)
    # Call send_commands function from periodically (to simulate processing latency)
    pyglet.clock.schedule_interval(agent.send_commands, 1.0 / env.unwrapped.frame_rate)
    # Now run simulation forever (or until ESC is pressed)
    pyglet.app.run()
    env.close()

if __name__ == '__main__':
    main()
