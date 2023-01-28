import numpy
import random
import os
import pyrosim.pyrosim as pyrosim
import time


class SOLUTION:

    def __init__(self,ID) -> None:
        self.weights = numpy.array([[numpy.random.rand(), numpy.random.rand()],
                                    [numpy.random.rand(), numpy.random.rand()],
                                    [numpy.random.rand(), numpy.random.rand()]])
        self.weights = self.weights * 2 - 1
        self.fitness = 0
        self.myID = ID

    def Set_ID(self):
        self.myID += 1

    def Start_Simulation(self,mode):
        if self.myID == 0:
            self.Create_World()
            self.Create_Body()
        self.Create_Brain()
        temp = str(self.myID)
        os.system("python3 simulate.py " + mode + " " + temp + " &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(.01)

        f = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(f.read())
        f.close()

        # os.system("rm " + "fitness"+str(self.myID)+".txt")

    def Evaluate(self,mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        temp = str(self.myID)
        os.system("python3 simulate.py " + mode + " " + temp + " &")
        
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(.01)

        f = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(f.read())
        f.close()
        

    def Create_World(self):
        #World creation
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[0,5,.5], size=[1,1,1])
        pyrosim.End()

    def Create_Body(self):
        #Robot creation
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1])

        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])

        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])
        pyrosim.End()

    def Create_Brain(self):
         #Brain creation
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4, jointName="Torso_FrontLeg")

        outerloop = [0,1,2]
        innerloop = [0,1]

        for currentRow in outerloop:
            for currentColumn in innerloop:
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()        

    def Mutate(self):
        row = random.randint(0,2)
        column = random.randint(0,1)
        self.weights[row,column] = random.random() * 2 - 1


            