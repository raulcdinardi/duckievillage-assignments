# MAC0318 Intro to Robotics
# Please fill-in the fields below with your info
#
# Name:
# NUSP:
#
# ---
#
# Assignment 0 - Manual steering
#
# Task:
#  - Write a remote control Duckiebot
#
# Don't forget to run this from the Duckievillage root directory (example):
#   cd ~/MAC0318/duckievillage
#   python3 assignments/manual/manual.py
#
# Submission instructions:
#  0. Add your name and USP number to the file header above.
#  1. Make sure that any last change haven't broken your code. If the code chrases without running you'll get a 0.
#  2. Submit this file via e-disciplinas.
#  3. Push changes to your git fork.import sys

import pyglet
from pyglet.window import key
from duckievillage import create_env

# We'll use our version of Duckietown: Duckievillage. This environment will be where we'll run most
# our tasks.
env = create_env(
  raw_motor_input = True,
  seed = 101,
  map_name = 'loop_empty',
  draw_curve = False,
  draw_bbox = False,
  domain_rand = False,
  distortion = False,
  top_down = False
)

# Let's reset the environment to get our Duckiebot somewhere random.
env.reset()
# This function is used to draw the environment to a graphical user interface using Pyglet.
env.render()

# We use this function for on-press key events (not something we use for real-time feedback,
# though). We'll register ESC as our way out of the Matrix.
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

# This function handles every frame update. Parameter dt is the elapsed time, in milliseconds,
# since the last update call.
def update(dt):
  # At each step, the agent accepts an action in the form of two [-1,1] reals:
  #   pwm_left, pwm_right = left motor power, right motor power
  # Play with the actions and figure out how to make your own remote control duckiebot!
  pwm_left, pwm_right = 0, 0

  # The key_handler object handles keyboard events. It's basically a map indexed by Pyglet keys
  # with values True if the key is being held, or False otherwise.
  if key_handler[key.D]:
    print('D!')
  if key_handler[key.U]:
    print('U!')
  if key_handler[key.C]:
    print('C!')
  if key_handler[key.K]:
    print('K!')

  # At each step, the environment may (or may not) change given your actions. Function step takes
  # as parameter the two motor powers as action and returns an observation (what the robot is
  # currently seeing), a reward (mostly used for reinforcement learning), whether the episode is
  # done (also used for reinforcement learning) and some info on the elapsed episode.  Let's ignore
  # return values for now.
  obs, reward, done, info = env.step(pwm_left, pwm_right)

  # Refresh at every update.
  env.render()

# Let's call update every 1.0 / frame_rate second.
pyglet.clock.schedule_interval(update, 1.0 / env.unwrapped.frame_rate)

# Enter main event loop.
pyglet.app.run()

env.close()
