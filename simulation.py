import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c
import sys

from world import WORLD
from robot import ROBOT

class SIMULATION:
    
    def __init__(self) -> None:


        directOrGui = sys.argv[1]
        solutionID = sys.argv[2]

        if directOrGui == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)


    def Run(self):
        for i in range(0,1000):
            time.sleep(1/60)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

    def Get_Fitness(self):
        self.robot.Get_Fitness()
    
    def __del__(self):
        p.disconnect()

    