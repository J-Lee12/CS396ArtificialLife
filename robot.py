import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim

from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import  NEURAL_NETWORK
import os

class ROBOT:

    def __init__(self,solutionID) -> None:
        self.solutionID = solutionID
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain"+str(self.solutionID)+".nndf")
        # os.system("rm brain"+str(self.solutionID)+".nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        
        

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self,index):
        for i in self.sensors.values():
            i.Get_Value(index)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self,t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        stateofLinkZero = p.getLinkState(self.robotId,0)
        positionofLinkZero = stateofLinkZero[0]
        xCoordinateofLinkZero = positionofLinkZero[0]

        f = open("tmp"+str(self.solutionID)+".txt", "w")
        f.write(str(xCoordinateofLinkZero))
        f.close()

        os.system("mv tmp"+str(self.solutionID)+".txt" " fitness"+str(self.solutionID)+".txt")


        exit()