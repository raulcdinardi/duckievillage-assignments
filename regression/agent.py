# MAC0318 - Intro to Robotics
#
# Name:
# NUSP:
#
# ---
#
# Assignment 8 - Lane following as a regression task
# Don't forget to run this file from the Duckievillage root directory path (example):
#   cd ~/MAC0318/duckievillage
#   git pull
#   $(bash) update.sh
#   conda activate duckietown
#   python3 assignments/pid-control/agent.py
#
# Submission instructions:
#  0. Add your name and USP number to the file header above.
#  1. Make sure that any last change hasn't broken your code. If the code crashes without running you'll get a 0.
#  2. Submit this file via e-disciplinas.


import sys
import pyglet
import numpy as np
import math
from pyglet.window import key
from duckievillage import create_env
import cv2
import tensorflow
import tensorflow.keras as keras

# Converts an RGB image to grayscale.
def rgb2gray(I):
  return np.dot(I[...,:3], [0.2989, 0.5870, 0.1140])

class Agent:
    # Agent initialization
    def __init__(self, environment):
        ''' Initializes agent '''
        self.env = environment
        # Wheel radius
        self.radius = 0.0318 # R
        # Distance between wheels
        self.baseline = environment.unwrapped.wheel_dist # 2L = 0.102 [m]
         # Motor constants
        self.motor_gain = 0.68*0.0784739898632288 # K_m
        self.motor_trim = 0.0007500911693361842 # K_t
        # Controller
        key_handler = key.KeyStateHandler()
        environment.unwrapped.window.push_handlers(key_handler)
        self.velocity = 0.0 # robot's logitudinal velocity
        self.rotation = 0.0 # robot's angular velocity
        self.key_handler = key_handler

    def load_regression_model(self, filepath):
        ''' Loads a Tensorflow model. '''
        N = keras.models.load_model(filepath)
        N.summary()
        return N
    
    def preprocess(self) -> float:
        ''' Returns the metric to be used as signal for the PID controller. '''
        I = env.front() # captures image from the robot's front camera
        J = cv2.resize(I, dsize=(200, 150)) # resize it to reduce processing cost
        J = rgb2gray(J).astype(np.uint8)        
        return 0.0 # value y=6*d + alpha      

    def get_pwm_control(self, v: float, w: float)-> (float, float):
        ''' Takes velocity v and angle w and returns left and right power to motors.'''
        V_l = (self.motor_gain - self.motor_trim)*(v-w*self.baseline/2)/self.radius
        V_r = (self.motor_gain + self.motor_trim)*(v+w*self.baseline/2)/self.radius
        return V_l, V_r

    def send_commands(self, dt) -> None:
        ''' Agent control loop '''
        # Manual control for testing in order to understand the environment.
        # You should delete this snippet after your controller is set.
        if self.key_handler[key.W]:
            self.velocity = 0.2
        if self.key_handler[key.A]:
            self.rotation += 0.5
        if self.key_handler[key.S]:
            self.velocity = 0.0
        if self.key_handler[key.D]:
            self.rotation = -0.5
        # End of remote control snippet.

        pwm_left, pwm_right = self.get_pwm_control(self.velocity, self.rotation)

        # Target value for lane-following.
        y = self.preprocess()
        # print(y) # uncomment this for debugging

        self.env.step(pwm_left, pwm_right) # send commands to motor
        self.env.render() # simulate environment

def main():
    print("MAC0318 - Assignment 8")
    env = create_env(
        raw_motor_input = True,
        noisy = True,
        mu_l = 0.007123895,
        mu_r = -0.000523123,
        std_l = 1e-7,
        std_r = 1e-7,
        seed = 101,
        map_name = 'udem1',
        draw_curve = False,
        draw_bbox = False,
        domain_rand = False,
        #user_tile_start = (0, 0),
        distortion = False,
        top_down = False,
        cam_height = 10,
        #is_external_map = True,
        randomize_maps_on_reset = False,
    )
    env.set_view(FRONT_VIEW_MODE)

    env.reset()
    env.render('human')

    @env.unwrapped.window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.ESCAPE: # exit simulation
            env.close()
            sys.exit(0)
        elif symbol == key.RETURN: # Reset pose.
            env.reset_pos()

        env.render() # show image to user

    agent = Agent(env)
    pyglet.clock.schedule_interval(agent.send_commands, 1.0 / env.unwrapped.frame_rate)
    pyglet.app.run()
    env.close()

if __name__ == '__main__':
    main()

