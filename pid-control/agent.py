# MAC0318 Intro to Robotics
# Please fill-in the fields below with your info
#
# Name:
# NUSP:
#
# ---
#
# Assignment 6 - PID Control
#
# Task:
#  - Write a PID controller for lane-following.
#
# Don't forget to run this file from the Duckievillage root directory path (example):
#   cd ~/MAC0318/duckievillage
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

class Agent:
    # Agent initialization
    def __init__(self, environment):
        ''' Initializes agent '''
        self.env = environment

        key_handler = key.KeyStateHandler()
        environment.unwrapped.window.push_handlers(key_handler)
        self.key_handler = key_handler

    def send_commands(self, dt):
        ''' Agent control loop '''
        pwm_left, pwm_right = 0, 0

        # Remote control for testing in order to understand the environment.
        # You may delete this snippet.
        if self.key_handler[key.W]:
            pwm_left += 0.5; pwm_right += 0.5
        if self.key_handler[key.A]:
            pwm_left -= 0.25; pwm_right += 0.25
        if self.key_handler[key.S]:
            pwm_left -= 0.5; pwm_right -= 0.5
        if self.key_handler[key.D]:
            pwm_left += 0.25; pwm_right -= 0.25
        # End of remote control snippet.

        # Target value for lane-following.
        t = self.env.lf_target()
        print(t)

        self.env.step(pwm_left, pwm_right)
        self.env.render()

def main():
    print("MAC0318 - Assignment 6")
    env = create_env(
        raw_motor_input = True,
        seed = 101,
        map_name = './maps/loop_empty.yaml',
        draw_curve = False,
        draw_bbox = False,
        domain_rand = False,
        user_tile_start = (0, 0),
        distortion = False,
        top_down = False,
        cam_height = 10,
        is_external_map = True,
        randomize_maps_on_reset = False,
    )

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
