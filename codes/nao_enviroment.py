import gym
from gym import spaces, logger
from gym.utils import seeding
from baselines.common.vec_env import VecEnv
import numpy as np
from vrepgym import vrep_env
from vrepgym import vrep


class NAOEnviroment():
	def __init__(self, IP, port):
		self.IP = IP
		self.port = port

        self.observation_space = spaces.Box(
            low=np.array([-1.0, -1.0]),
            high=np.array([1.0,  1.0]),
            dtype=np.float32
        )
        
        self.action_space = spaces.Box(
            low = np.array([0.0,0.0,-3.14]),
            high= np.array([1.0,1.0,-3.14]),
            dtype=np.float32
        )

        self.state = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)


        return [seed]

    def _update_state(self):
    	return

    def step(self, action):
    	return



