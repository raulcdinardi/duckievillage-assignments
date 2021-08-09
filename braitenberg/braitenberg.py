# Intro to Robotics - MAC0318
#
# Name:
# NUSP:
#
# ---
#
# Assignment 2 - Braitenberg vehicles
# Carefully read this header and follow submission instructions!
# Failure to follow instructions may result in a zero!
#
# Task:
#  - Write the following Braitenberg behaviors by only setting the bot's left and right activation
#  matrices:
#
#     Aggressive: Follows and runs over Duckies;
#     Coward:     Hides from Duckies;
#
# Don't forget to run this from the Duckievillage root directory!
# From within the root directory, run python like so:
#   python3 assignments/braitenberg/braitenberg.py
#
# Submission instructions:
#  0. Add your name and USP number to the header's header.
#  1. Make sure everything is running fine and there are no errors during startup. If the code does
#     not even start the environment, you will receive a zero.
#  2. Test your code and make sure it's doing what it's supposed to do.
#  4. Submit your work to edisciplinas.
#  3. Push changes to your fork. You will also be evaluated from what's in your repository!

import sys
import math
import pyglet
import numpy as np
from pyglet.window import key
import gym
import gym_duckietown
from duckievillage import create_env
from PIL import Image

env = create_env(
  raw_motor_input = True,
  seed = 101,
  map_name = './maps/nothing.yaml',
  draw_curve = False,
  draw_bbox = False,
  domain_rand = False,
  color_sky = [0, 0, 0],
  user_tile_start = (0, 0),
  distortion = False,
  top_down = False,
  cam_height = 10,
  is_external_map = True,
  enable_lightsensor = True
)
for o in env.objects: o.scale = 0.085

# Behavior is passed as an argument.
behavior = sys.argv[1].lower()

angle = env.unwrapped.cam_angle[0]

env.start_pose = [np.array([0.5, 0, 0.5]), 150]
env.reset()
env.render()

@env.unwrapped.window.event
def on_key_press(symbol, modifiers):
  if symbol == key.ESCAPE:
    env.close()
    sys.exit(0)
  env.render()

# KeyStateHandler handles key states.
key_handler = key.KeyStateHandler()
# Let's register our key handler to the environment's key listener.
env.unwrapped.window.push_handlers(key_handler)

# The left motor activation matrix. The returned matrix will define how much power is given to the
# left motor.
def left_activation(n: int, m: int) -> np.ndarray:
  M = np.zeros(shape=(n, m), dtype=np.float32)
  if behavior == "aggressive":
    pass
  else: # coward
    pass
  return M

# The right motor activation matrix. The returned matrix will define how much power is given to the
# right motor.
def right_activation(n: int, m: int) -> np.ndarray:
  M = np.zeros(shape=(n, m), dtype=np.float32)
  if behavior == "aggressive":
    pass
  else: # coward
    pass
  return M

def update(dt):
  action = [0.0, 0.0]

  action[0], action[1] = env.lightsensor.measure(left_activation, right_activation)
  # If needed, tweak power with constants of your choice.
  action[0] /= 2
  action[1] /= 2

  if key_handler[key.W]:
    action += np.array([0.5, 0.5])
  if key_handler[key.A]:
    action += np.array([-0.5, 0.5])
  if key_handler[key.S]:
    action += np.array([-0.5, -0.5])
  if key_handler[key.D]:
    action += np.array([0.5, -0.5])

  obs, reward, done, info = env.step(action)
  env.render()

pyglet.clock.schedule_interval(update, 1.0 / env.unwrapped.frame_rate)
pyglet.app.run()
env.close()
