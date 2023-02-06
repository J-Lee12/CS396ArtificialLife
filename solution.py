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
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[1,1,1])

        # ## Back Leg
        # pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-.5,1], jointAxis= "1 0 0")
        # pyrosim.Send_Cube(name="BackLeg", pos=[0,-.5,0], size=[.2,1,.2])
        # pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis= "1 0 0")
        # pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-.5], size=[.2,.2,1.5])

        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-.5,.6], jointAxis= "0 0 1")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-.1,0], size=[.2,.2,.2])
        pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-.2,0], jointAxis= "0 0 1")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,-.5,0], size=[.2,1,.2])

        # ## Front Leg
        # pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,.5,1], jointAxis= "1 0 0")
        # pyrosim.Send_Cube(name="FrontLeg", pos=[0,.5,0], size=[.2,1,.2])
        # pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis= "1 0 0")
        # pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-.5], size=[.2,.2,1.5])

        ## Front Leg
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,.5,.6], jointAxis= "0 0 1")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,.1,0], size=[.2,.2,.2]) #1.3
        pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,.2,0], jointAxis= "0 0 1")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,.5,-0], size=[.2,1,.2])

        ## Left Leg
        # pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-.5,0,1], jointAxis= "0 1 0")
        # pyrosim.Send_Cube(name="LeftLeg", pos=[-.5,0,0], size=[1,.2,.2])
        # pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis= "0 1 0")
        # pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-.5], size=[.2,.2,1])

        ## Right Leg
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [.5,0,1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[.5,0,0], size=[1,.2,.2])
        pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-.6], size=[.2,.2,1])





        pyrosim.End()

    def Create_Brain(self):
         #Brain creation
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName="FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 5, linkName="BackLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 6, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6, linkName="RightLowerLeg")

        pyrosim.Send_Motor_Neuron( name = 7, jointName="RightLeg_RightLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 7, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 8, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 9, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 10, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 11, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 12, jointName="Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron( name = 12, jointName="Torso_LeftLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()        

    def Mutate(self):
        row = random.randint(0,(c.numSensorNeurons - 1))
        column = random.randint(0,(c.numMotorNeurons - 1))
        self.weights[row,column] = random.random() * 2 - 1


            