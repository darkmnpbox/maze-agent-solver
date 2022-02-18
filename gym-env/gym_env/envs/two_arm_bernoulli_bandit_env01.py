import gym
from gym import spaces
from gym.utils import seeding
import numpy as np


class TwoArmBernoulliBanditEnv01(gym.Env):
    def __init__(self, alpha=0.5, beta=0.5):
        self.alpha = alpha
        self.beta = beta
        self.state = 0
        self.done = False
        self.observation_space = spaces.Discrete(3)
        self.action_space = spaces.Discrete(2)

    def step(self, action):
        if action == 0:
            self.state = np.random.choice(
                [1, 2], 1, p=[self.alpha, 1-self.alpha])
        elif action == 1:
            self.state = np.random.choice(
                [1, 2], 1, p=[1-self.beta, self.beta])

        if self.state == 1:
            reward = 1
        else:
            reward = 0
        self.done = True
        return self.state, reward, self.done

    def seed(self, seed):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        self.state = 0
        return self.state
