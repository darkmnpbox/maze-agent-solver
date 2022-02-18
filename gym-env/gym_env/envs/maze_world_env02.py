import gym
import numpy as np


class MazeWorldEnv02(gym.Env):
    def __init__(self, maze, start=0):
        self.maze = maze
        self.rows, self.cols = maze.shape
        self.start = start
        self.state = start
        self.done = False

    def action_available(self):
        row = self.state//self.cols
        col = self.state % self.cols
        actions = [0, 1, 2, 3]
        if row == 0:
            actions.remove(0)
        if col == 0:
            actions.remove(3)
        if col == self.cols - 1:
            actions.remove(1)
        if row == self.rows - 1:
            actions.remove(2)
        return actions

    def step(self, action):
        row = self.state//self.cols
        col = self.state % self.cols
        if action == 0:
            row -= 1
        elif action == 1:
            col += 1
        elif action == 2:
            row += 1
        elif action == 3:
            col -= 1

        if self.maze[row, col] == 0:
            reward = 0
        elif self.maze[row, col] == 1:
            self.state = row*self.cols + col
            reward = 0
        elif self.maze[row, col] == 3:
            self.state = row*self.cols + col
            reward = 1
            self.done = True
        elif self.maze[row, col] == 4:
            self.state = row*self.cols + col
            reward = -1
            self.done = True
        return self.state, reward, self.done

    def reset(self):
        self.state = self.start
        self.done = False
        return self.state
