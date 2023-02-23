import numpy
import random
import os
import pyrosim.pyrosim as pyrosim
import time
import constants as c
import random

from body_generate import BODYGENERATOR


class SOLUTION:

    def __init__(self,ID) -> None:
        self.fitness = 0
        self.myID = ID
        self.body = BODYGENERATOR(ID)

    def Set_ID(self):
        self.myID += 1

    def Start_Simulation(self,mode):
        if self.myID == 0:
            self.body.Create_World()
            self.body.Create_Body()
        self.body.Create_Brain()
        temp = str(self.myID)
        os.system("python3 simulate.py " + mode + " " + temp)

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(.01)

        f = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(f.read())
        f.close()

    def Evaluate(self,mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        temp = str(self.myID)
        os.system("python3 simulate.py " + mode + " " + temp)
        
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(.01)

        f = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(f.read())
        f.close()

    def Mutate(self):
        ## changes the snyaptic weights of the brain
        row = random.randint(0,(c.numSensorNeurons - 1))
        column = random.randint(0,(c.numMotorNeurons - 1))
        self.body.weights[row,column] = random.random() * 2 - 1
        


            