from typing import Tuple
import gym
from gym import spaces
import numpy as np


class MazeWorldEnv01(gym.Env):

    def __init__(self, start=0):
        self.start = start
        self.state = start
        self.done = False
        self.info = {}

    def move(self):
        move = [0, 1, 2, 3]
        if self.state % 4 == 3:
            move.remove(1)
        elif self.state % 4 == 0:
            move.remove(3)
        if self.state // 4 == 0:
            move.remove(0)
        elif self.state // 4 == 3:
            move.remove(2)
        return move

    def step(self, action):
        if action == 0:
            self.state -= 4
        elif action == 1:
            self.state += 1
        elif action == 2:
            self.state += 4
        elif action == 3:
            self.state -= 1

        reward = 0

        if self.state in [5, 7, 11, 12, 15]:
            self.done = True
            if self.state == 15:
                reward = 1
            else:
                reward = -1
        return self.state, reward, self.done, self.info

    def reset(self):
        self.done = False
        self.state = self.start
        return self.state
