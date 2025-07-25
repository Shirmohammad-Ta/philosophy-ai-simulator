
# env_simulator.py
import gym
from gym import spaces
import numpy as np

class PhilosophyEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.H = 0.8
        self.A = 0.5
        self.V = 0.7
        self.beta = 1.0

        self.action_space = spaces.Discrete(5)  # sacrifice level: 0 to 1
        self.observation_space = spaces.Box(low=0.0, high=1.0, shape=(3,), dtype=np.float32)

    def reset(self):
        self.H = 0.8
        self.A = 0.5
        self.V = 0.7
        return np.array([self.H, self.A, self.V], dtype=np.float32)

    def step(self, action_idx):
        action = action_idx / 4.0
        self.A = min(1.0, action)
        E = self.beta * self.A * self.V
        self.H = max(0.0, self.H - 0.05 * self.A)
        reward = -E
        done = False
        obs = np.array([self.H, self.A, self.V], dtype=np.float32)
        return obs, reward, done, {}
