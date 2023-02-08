import numpy
import random
import os
import pyrosim.pyrosim as pyrosim
import time
import constants as c


class SOLUTION:

    def __init__(self,ID) -> None:
        # self.weights = numpy.array([[numpy.random.rand(), numpy.random.rand()],
        #                             [numpy.random.rand(), numpy.random.rand()],
        #                             [numpy.random.rand(), numpy.random.rand()]])
        weights = []
        for i in range(c.numSensorNeurons):
            temp = []
            for j in range(c.numMotorNeurons):
                temp.append(numpy.random.rand())
            weights.append(temp)
        weights = numpy.asarray(weights)

        self.weights = weights
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
        os.system("python3 simulate.py " + mode + " " + temp + " 2&>1" + "&")

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

        x = numpy.random.uniform(0,2)
        y = numpy.random.uniform(0,2)
        z = numpy.random.uniform(0,2)

        start = numpy.random.uniform(0,2)
        name = "a"

        pyrosim.Start_URDF("body.urdf")
        ## absolute
        pyrosim.Send_Cube(name="Torso", pos=[-4,0,3], size=[start,1,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[x/2,0,0], size=[x,y,z])
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-4 + start/2,0,3], jointAxis= "0 0 1")
        ## relative
    
        pyrosim.End()

    def Create_Brain(self):
         #Brain creation
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName="BackLeg")
        # pyrosim.Send_Sensor_Neuron(name = 2, linkName="FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3, linkName="LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3, linkName="RightLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3, linkName="FrontLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 2, linkName="BackLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 6, linkName="LeftLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 6, linkName="RightLowerLeg")

        # pyrosim.Send_Motor_Neuron( name = 7, jointName="RightLeg_RightLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 7, jointName="LeftLeg_LeftLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 3, jointName="BackLeg_BackLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 6, jointName="FrontLeg_FrontLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 7, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 4, jointName="Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron( name = 5, jointName="Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron( name = 12, jointName="Torso_LeftLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()        

    def Mutate(self):
        row = random.randint(0,(c.numSensorNeurons - 1))
        column = random.randint(0,(c.numMotorNeurons - 1))
        self.weights[row,column] = random.random() * 2 - 1


            