import pyglet
from pyglet.window import key
import numpy as np
import math
import random
from duckievillage import create_env, FRONT_VIEW_MODE
import cv2
import tensorflow

class Agent:
    def __init__(self, env):
        self.env = env
        self.radius = 0.0318
        self.baseline = env.unwrapped.wheel_dist/2
        self.motor_gain = 0.68*0.0784739898632288
        self.motor_trim = 0.0007500911693361842

        key_handler = key.KeyStateHandler()
        env.unwrapped.window.push_handlers(key_handler)
        self.key_handler = key_handler

    def get_pwm_control(self, v: float, w: float)-> (float, float):
        ''' Takes velocity v and angle w and returns left and right power to motors.'''
        V_l = (self.motor_gain - self.motor_trim)*(v-w*self.baseline)/self.radius
        V_r = (self.motor_gain + self.motor_trim)*(v+w*self.baseline)/self.radius
        return V_l, V_r

    def preprocess(self):
        pass

    def send_commands(self, dt: float):
        velocity = 0
        rotation = 0

        if self.key_handler[key.W]:
            velocity += 0.5
        if self.key_handler[key.A]:
            rotation += 1.5
        if self.key_handler[key.S]:
            velocity -= 0.5
        if self.key_handler[key.D]:
            rotation -= 1.5

        pwm_left, pwm_right = self.get_pwm_control(velocity, rotation)
        self.env.step(pwm_left, pwm_right)
