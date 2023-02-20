import numpy
import random
import os
import pyrosim.pyrosim as pyrosim
import time
import constants as c
import random


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
        self.sensors = []
        self.motors = []
        self.links = []
        self.linked = []
        self.linkfaces = {}

    def Set_ID(self):
        self.myID += 1

    def Start_Simulation(self,mode):
        if self.myID == 0:
            self.Create_World()
            self.Create_Body()
        self.Create_Brain()
        temp = str(self.myID)
        os.system("python3 simulate.py " + mode + " " + temp)

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
        os.system("python3 simulate.py " + mode + " " + temp)
        
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(.01)

        f = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(f.read())
        f.close()
        

    def Create_World(self):
        #World creation
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[0,5,.5], size=[1,1,1], color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
        pyrosim.End()

    def Face_Generate(self,prevface):
        faces = {"x":["y","z"],
                 "y":["x","z"],
                 "z":["x","y"]}
        
        return faces[prevface][numpy.random.randint(0,2)]

    def Generate_Links(self):
        i = 1
        while i < c.numoflinks:
            x = numpy.random.uniform(0,2)
            y = numpy.random.uniform(0,2)
            z = numpy.random.uniform(0,2)

            if bool(random.getrandbits(1)):
                pyrosim.Send_Cube(name=c.names[i], pos=[x/2,y/2,z/2], size=[x,y,z], color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
                self.sensors.append(c.names[i])
            else:
                pyrosim.Send_Cube(name=c.names[i], pos=[x/2,y/2,z/2], size=[x,y,z], color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
            
            self.links.append([c.names[i],[x/2,y/2,z/2],[x,y,z]])
            self.linkfaces[c.names[i]] = []
            i += 1

    def Create_Body(self):
        #Robot creation
        x = numpy.random.uniform(0,2)
        y = numpy.random.uniform(0,2)
        z = numpy.random.uniform(0,2)

        start = numpy.random.uniform(0,2)
        pyrosim.Start_URDF("body.urdf")
        xpos = numpy.random.randint(-4,4)

        if bool(random.getrandbits(1)):
            pyrosim.Send_Cube(name="Torso", pos=[xpos,0,3], size=[start,1,1], color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
            self.sensors.append("Torso")
        else:
            pyrosim.Send_Cube(name="Torso", pos=[xpos,0,3], size=[start,1,1], color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
        
        self.linked.append(["Torso",[xpos,0,3],[start,1,1]])
        self.linkfaces["Torso"] = []
        self.Generate_Links()

        j = 0
        i = 0
        prevface = "x"
        while j < len(self.links):

            currlink = self.links.pop()
            currparent = self.linked[numpy.random.randint(0,len(self.linked))]
            randomface = self.Face_Generate(prevface)

            if currlink[0] == currparent[0]:
                self.links.append(currlink)
                pass

            if i == 0:
                currparent = self.linked[0]
                pyrosim.Send_Joint(name = currparent[0]+"_"+currlink[0] , parent=currparent[0] , child = currlink[0] ,
                                type = "revolute", position = [xpos+start/2,currparent[1][1], currparent[1][2]], jointAxis= "0 1 0")
                self.linkfaces[currparent[0]].append("x")
                randomface = "x"
            
            else:
                if randomface not in self.linkfaces[currparent[0]]:
                    if randomface == "x":
                        pyrosim.Send_Joint(name = currparent[0]+"_"+currlink[0] , parent=currparent[0] , child = currlink[0] ,
                                        type = "revolute", position = [currparent[2][0]/2,0,0], jointAxis= "0 1 0")
                        self.linkfaces[currparent[0]].append(randomface)
                    elif randomface == "y":
                        pyrosim.Send_Joint(name = currparent[0]+"_"+currlink[0] , parent=currparent[0] , child = currlink[0] ,
                                type = "revolute", position = [0,currparent[2][1]/2,0], jointAxis= "0 1 0")
                        self.linkfaces[currparent[0]].append(randomface)
                    else:
                        pyrosim.Send_Joint(name = currparent[0]+"_"+currlink[0] , parent=currparent[0] , child = currlink[0] ,
                                type = "revolute", position = [0,0,currparent[2][2]/2], jointAxis= "0 1 0")
                        self.linkfaces[currparent[0]].append(randomface)
                else:
                        pyrosim.Send_Joint(name = currparent[0]+"_"+currlink[0] , parent=currparent[0] , child = currlink[0] ,
                                type = "revolute", position = [currparent[2][0]/3,currparent[2][1]/3,currparent[2][2]/3], jointAxis= "0 1 0")
            i += 1
            self.linked.append(currlink)
            prevface = randomface

        pyrosim.End()

    def Create_Brain(self):
         #Brain creation
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        
        count = 0
        for i in self.sensors:
            pyrosim.Send_Sensor_Neuron(name= count, linkName=i)
            count += 1
        
        for j in self.motors:
            pyrosim.Send_Motor_Neuron(name=count, jointName=j)
            count += 1

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()        

    def Mutate(self):
        row = random.randint(0,(c.numSensorNeurons - 1))
        column = random.randint(0,(c.numMotorNeurons - 1))
        self.weights[row,column] = random.random() * 2 - 1


            