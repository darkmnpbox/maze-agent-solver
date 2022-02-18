import gym
from gym import spaces
import numpy as np


class SlipparyBanditWalkEnv01(gym.Env):

    def __init__(self, start=3, sameDirection=0.5, oppisiteDirection=1/6, nonDirection=1/3):
        self.action_spaces = spaces.Discrete(2)
        self.observation_spaces = spaces.Discrete(7)
        self.slip = [sameDirection, oppisiteDirection, nonDirection]
        self.state = start
        self.done = False

    def step(self, action):
        if action == 0:
            self.state = np.random.choice(
                [self.state-1, self.state+1, self.state], p=self.slip)
        elif action == 1:
            self.state = np.random.choice(
                [self.state+1, self.state-1, self.state], p=self.slip)

        reward = 0

        if self.state == 6:
            reward = 1
            self.done = True
        elif self.state == 0:
            self.done = True

        return self.state, reward, self.done

    def reset(self, start=3):
        self.done = False
        self.state = start
        return self.state
