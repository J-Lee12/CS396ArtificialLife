import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c
from simulation import SIMULATION
import sys


simulation = SIMULATION()
simulation.Run()
simulation.Get_Fitness()