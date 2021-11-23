# MAC0318 Intro to Robotics
# Please fill-in the fields below with your info
#
# Name:
# NUSP:
#
# ---
#
# Final Project - The Travelling Mailduck Problem
#
# Don't forget to run this file from the Duckievillage root directory path (example):
#   cd ~/MAC0318/duckievillage
#   conda activate duckietown
#   python3 assignments/mailduck/mailduck.py
#
# Submission instructions:
#  0. Add your name and USP number to the file header above.
#  1. Make sure that any last change hasn't broken your code. If the code crashes without running you'll get a 0.
#  2. Submit this file via e-disciplinas.

import sys
import pyglet
from pyglet.window import key
from duckievillage import create_env, FRONT_VIEW_MODE

from agent import Agent

def main():
    print("MAC0318 - Final Project")

    map_name = None
    with open(sys.argv[1]) as file:
        map_name = file.readline().strip()

    env = create_env(
        raw_motor_input = True,
        noisy = True,
        mu_l = 0.007123895,
        mu_r = -0.000523123,
        std_l = 1e-7,
        std_r = 1e-7,
        seed = 101,
        map_name = map_name,
        mailbox_file = sys.argv[1],
        enable_mailbox = True,
        enable_eval = True,
        draw_curve = False,
        draw_bbox = False,
        domain_rand = False,
        distortion = False,
        top_down = False,
        cam_height = 10,
        is_external_map = True,
        randomize_maps_on_reset = False,
    )

    env.set_view(FRONT_VIEW_MODE)
    env.render()

    @env.unwrapped.window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.ESCAPE: # exit simulation
            # Dump log to file
            with open("/tmp/output.txt", 'w') as file:
                for k in env.eval._log:
                    for l in env.eval._log[k]: file.write(str(l[0]) + " " + str(l[1]) + '\n')
            env.close()
            sys.exit(0)

    agent = Agent(env)

    print(env.mailbox.mail())

    def loop(dt: float):
        agent.send_commands(dt)
        env.eval.track()
        env.render()

    pyglet.clock.schedule_interval(loop, 1.0 / env.unwrapped.frame_rate)
    pyglet.app.run()
    env.close()

if __name__ == '__main__':
    main()
