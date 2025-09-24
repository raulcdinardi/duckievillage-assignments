# MAC0318 Intro to Robotics
# Please fill-in the fields below with your info
#
# Name: Raul Cavalcante Dinardi
# NUSP: 15486341
#
# ---
#
# Assignment 7 - Potential Fields
#
# Task:
#  - Write a potential field based agent.
#
# Don't forget to run this file from the Duckievillage root directory path (example):
#   cd ~/duckievillage
#   source bin/activate 
#   python3 assignments/p-fields/agent.py
#
# Submission instructions:
#  0. Add your name and USP number to the file header above.
#  1. Make sure that any last change hasn't broken your code. If the code crashes without running you'll get a 0.
#  2. Submit this file via e-disciplinas.

import sys
import pyglet
import numpy as np
import numpy.linalg
import math
from pyglet.window import key
from duckievillage import create_env
import cv2

def go_mr_duckie(env):
    '''Creates and plops a walking Duckie into the environment's world.'''
    import random
    possible_starts = [[0.88, 0.86], [3.85, 0.89], [3.90, 2.68], [0.80, 3.26]]
    p = possible_starts[random.randint(0, len(possible_starts)-1)]
    return env.add_walking_duckie(p)
mr_duckie = None

def mr_duckie_pos() -> np.ndarray:
    '''Returns the position of Mr. Duckie, the walking duck.'''
    return np.delete(mr_duckie.pos, 1)

def dist(p: np.ndarray, q: np.ndarray) -> float:
    '''Returns the distance between two points.'''
    return np.linalg.norm(p-q)

def line(a: np.ndarray, b: np.ndarray, x: float) -> float:
    '''Line equation function.'''
    return a + x*(b-a)

def dist_obj(p: np.ndarray, o: list) -> (float, np.ndarray):
    '''
    Measures the distance between a point p and an object (polygon) o. The polygonal object is
    represented as a list of vertices. Returns the distance and the nearest point in the frontier
    of o relative to p.
    '''
    a = o[-1]
    m, mo = math.inf, None
    for i in range(len(o)):
        b = o[i]
        t = np.dot(p-a, b-a)/np.dot(b-a, b-a)
        if t < 0:
            d = dist(p, a)
            if m > d: m, mo = d, a
        elif t > 1:
            d = dist(p, b)
            if m > d: m, mo = d, b
        else:
            q = line(a, b, t)
            d = dist(p, q)
            if m > d: m, mo = d, q
        a = b
    return m, np.array(mo)

def heading_vec(p: np.ndarray, o: np.ndarray) -> (float):
    heading_vec = p - o 
    heading_vec = heading_vec/np.linalg.norm(heading_vec)
    return heading_vec

class Agent:
    # Agent initialization
    def __init__(self, environment):
        ''' Initializes agent '''
        self.env = environment

        self.radius = 0.0318 # R
        self.baseline = environment.unwrapped.wheel_dist/2
        self.motor_gain = 0.68*0.0784739898632288
        self.motor_trim = 0.0007500911693361842

        self.velocity = 0
        self.rotation = 0

        self.K_att = 0
        self.K_rep = 0
        self.rho = 0
        self.alpha = 0
        self.epsilon = 0

        self.K_v = 0
        self.K_w = 0

        self.erro_cumulativo = 0
        self.erro_anterior = None

        key_handler = key.KeyStateHandler()
        environment.unwrapped.window.push_handlers(key_handler)
        self.key_handler = key_handler
    def get_pwm_control(self, v: float, w: float)-> (float, float):
        ''' Takes velocity v and angle w and returns left and right power to motors.'''
        V_l = (self.motor_gain - self.motor_trim)*(v-w*self.baseline)/self.radius
        V_r = (self.motor_gain + self.motor_trim)*(v+w*self.baseline)/self.radius
        return V_l, V_r

    def F_att(self, p: np.ndarray, g: np.ndarray) -> float:
        '''Returns the attraction force applied at position p from goal g.'''
        return 1/np.linalg.norm(p-g)**2
        
    def F_rep(self, p: np.ndarray, o: list) -> float:
        '''Returns the repulsion force applied at position p from object o.'''
        return -1/dist_obj(p,o)[0]**3

    def preprocess(self, p: np.ndarray, g: np.ndarray, P: list) -> np.ndarray:
        vec = self.F_att(p,g) * heading_vec(p, g) * 1.5
        for o in P:
            vec += self.F_rep(p, o)*heading_vec(p, dist_obj(p,o)[1]) *0.004

        '''
        Takes the bot's current position p, a goal position g, and a list of polygons P. The
        function should then compute the force and return the resulting point for the bot to
        follow.
        '''
        return p+vec
    def pid(self, erro):
        kEp = 1000
        kEd = -300
        kEi = -0

        erro_der = 0
        if self.erro_anterior != None:
            self.erro_anterior = erro
        else:
            try:
                erro_der = erro - self.erro_anterior
            except:
                pass
        
        self.erro_cumulativo = 0

        return kEp*erro + kEd*erro_der + kEi*self.erro_cumulativo

    def send_commands(self, dt: float):
        ''' Agent control loop '''
        pwm_left, pwm_right = 0, 0

        if self.key_handler[key.W]:
            pwm_left += 0.5; pwm_right += 0.5
        if self.key_handler[key.A]:
            pwm_left -= 0.25; pwm_right += 0.25
        if self.key_handler[key.S]:
            pwm_left -= 0.5; pwm_right -= 0.5
        if self.key_handler[key.D]:
            pwm_left += 0.25; pwm_right -= 0.25
        # current 
        p = self.env.get_position()
        # target position
        q = self.preprocess(p, mr_duckie_pos(), self.env.poly_map.polygons())
        #q = np.array([2,2])
        # robot's heading
        a = self.env.cur_angle
        # TODO: compute velocity and rotation using PID controller




        direcao = np.array([np.sin(a+ np.pi), np.cos(a + np.pi)])
        direcao_q = p-q

        direcao = direcao/np.linalg.norm(direcao) / 100
        direcao_q = direcao_q/np.linalg.norm(direcao) / 100

        #self.rotation = 1
        erro = np.dot(direcao, direcao_q) 
        self.velocity = 0.2
        self.rotation = self.pid(erro)
        print(f"p: {p} ; q: {q} ; a: {a}, erro: {erro}, giro: {self.rotation}")
        pwm_left, pwm_right = self.get_pwm_control(self.velocity, self.rotation)

        self.env.step(pwm_left, pwm_right)
        self.env.render()

def main():
    print("MAC0318 - Assignment 6")
    env = create_env(
        raw_motor_input = True,
        noisy = True,
        mu_l = 0.007123895,
        mu_r = -0.000523123,
        std_l = 1e-7,
        std_r = 1e-7,
        seed = 101,
        map_name = './maps/catch',
        draw_curve = False,
        draw_bbox = False,
        domain_rand = False,
        user_tile_start = (0, 0),
        distortion = False,
        top_down = False,
        cam_height = 10,
        #is_external_map = True,
        randomize_maps_on_reset = False,
        enable_polymap = True,
    )

    global mr_duckie
    # Mr. Duckie ready for duty.
    mr_duckie = go_mr_duckie(env)

    # env.poly_map.dilate(0.05, True)
    env.reset()
    env.render('human') # show visualization

    @env.unwrapped.window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.ESCAPE: # exit simulation
            env.close()
            sys.exit(0)
        elif symbol == key.RETURN:  # Reset pose.
            env.reset_pos()

        env.render() # show image to user

    # Instantiate agent
    agent = Agent(env)
    # Call send_commands function from periodically (to simulate processing latency)
    pyglet.clock.schedule_interval(agent.send_commands, 1.0 / env.unwrapped.frame_rate)
    # Now run simulation forever (or until ESC is pressed)
    pyglet.app.run()
    # When it's done, close environment and exit program
    env.close()

if __name__ == '__main__': main()
