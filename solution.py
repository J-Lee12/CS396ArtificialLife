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

    def Generate_Cube(self,i,prevside):
            
            ## Generate a cube of a random size onto a random side
            sides = {
                "x":["y","z"],
                "y":["x","z"],
                "z":["x","y"]
            }
            newx = numpy.random.uniform(0,2)
            newy = numpy.random.uniform(0,2)
            newz = numpy.random.uniform(0,2)

            currside = sides[prevside][numpy.random.randint(0,2)]
            if currside == "x":
                if bool(random.getrandbits(1)):
                    pyrosim.Send_Cube(name=c.names[i], pos=[newx/2,0,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
                    self.sensors.append(c.names[i])
                else:
                    pyrosim.Send_Cube(name=c.names[i], pos=[newx/2,0,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
            
            elif currside == "y":
                if bool(random.getrandbits(1)):
                    pyrosim.Send_Cube(name=c.names[i], pos=[0,newy/2,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
                    self.sensors.append(c.names[i])
                else:
                    pyrosim.Send_Cube(name=c.names[i], pos=[0,newy/2,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
            
            else:
                if bool(random.getrandbits(1)):
                    pyrosim.Send_Cube(name=c.names[i], pos=[0,0,newz/2], size=[newx,newy,newz],color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
                    self.sensors.append(c.names[i])
                else:
                    pyrosim.Send_Cube(name=c.names[i], pos=[0,0,newz/2], size=[newx,newy,newz],color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
            
            return([c.names[i],currside,newx,newy,newz])

    def Create_Body(self):
        #Robot creation
        x = numpy.random.uniform(0,2)
        y = numpy.random.uniform(0,2)
        z = numpy.random.uniform(0,2)
        start = numpy.random.uniform(0,2)
        pyrosim.Start_URDF("body.urdf")
        xpos = numpy.random.randint(-4,4)

        if bool(random.getrandbits(1)):
            ## if true then it has a sensor
            pyrosim.Send_Cube(name="Torso", pos=[xpos,0,3], size=[start,1,1], color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
            pyrosim.Send_Joint(name = "Torso_"+c.names[0] , parent= "Torso" , child = c.names[0] , type = "revolute", position = [xpos + start/2,0,3], jointAxis= "0 1 0")
            self.sensors.append("Torso")

        else:
            ## if false then no sensor
            pyrosim.Send_Cube(name="Torso", pos=[xpos,0,3], size=[start,1,1], color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
            pyrosim.Send_Joint(name = "Torso_"+c.names[0] , parent= "Torso" , child = c.names[0] , type = "revolute", position = [xpos + start/2,0,3], jointAxis= "0 1 0")

        self.links.append(["Torso",start,1,1])
        self.motors.append("Torso_"+c.names[0])    
    
        if bool(random.getrandbits(1)):
            pyrosim.Send_Cube(name=c.names[0], pos=[x/2,0,0], size=[x,y,z], color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
            self.sensors.append(c.names[0])
        else:
            pyrosim.Send_Cube(name=c.names[0], pos=[x/2,0,0], size=[x,y,z], color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')

        self.links.append([c.names[0],x,y,z])
        prevside = "x"
        i = 1
        while i < c.numoflinks:
            ## randomly generate a cube, then attach it to a random cube
            currcube = self.Generate_Cube(i,prevside)
            currside = currcube[1]
        
            prev = self.links[numpy.random.randint(0,len(self.links))]
            prevparentname = prev[0]
            prevx = prev[1]
            prevy = prev[2]
            prevz = prev[3]

            ## need to check the previous face and the current face
            ## 
            if prevside == "x":
                if currside == "x":
                    pyrosim.Send_Joint(name = prevparentname+"_"+c.names[i] , parent= prevparentname , child = c.names[i] , type = "revolute", position = [prevx,0,0], jointAxis= "0 1 0")
                    self.motors.append(prevparentname+"_"+c.names[i])
                elif currside == "y":
                    pyrosim.Send_Joint(name = prevparentname+"_"+c.names[i] , parent= prevparentname , child = c.names[i] , type = "revolute", position = [prevx/2,prevy/2,0], jointAxis= "0 1 0")
                    self.motors.append(prevparentname+"_"+c.names[i])
                else:
                    pyrosim.Send_Joint(name = prevparentname+"_"+c.names[i] , parent= prevparentname , child = c.names[i] , type = "revolute", position = [prevx/2,0,prevz/2], jointAxis= "0 1 0")
                    self.motors.append(prevparentname+"_"+c.names[i])
            elif prevside == "y":
                if currside == "x":
                    pyrosim.Send_Joint(name = prevparentname+"_"+c.names[i] , parent= prevparentname , child = c.names[i] , type = "revolute", position = [prevx/2,prevy/2,0], jointAxis= "0 1 0")
                    self.motors.append(prevparentname+"_"+c.names[i])
                elif currside == "y":
                    pyrosim.Send_Joint(name = prevparentname+"_"+c.names[i] , parent= prevparentname , child = c.names[i] , type = "revolute", position = [0,prevy,0], jointAxis= "0 1 0")
                    self.motors.append(prevparentname+"_"+c.names[i])
                else:
                    pyrosim.Send_Joint(name = prevparentname+"_"+c.names[i] , parent= prevparentname , child = c.names[i] , type = "revolute", position = [0,prevy/2,prevz/2], jointAxis= "0 1 0")
                    self.motors.append(prevparentname+"_"+c.names[i])
            else:
                if currside == "x":
                    pyrosim.Send_Joint(name = prevparentname+"_"+c.names[i] , parent= prevparentname , child = c.names[i] , type = "revolute", position = [prevx/2,0,prevz/2], jointAxis= "0 1 0")
                    self.motors.append(prevparentname+"_"+c.names[i])
                elif currside == "y":
                    pyrosim.Send_Joint(name = prevparentname+"_"+c.names[i] , parent= prevparentname , child = c.names[i] , type = "revolute", position = [prevx/2,0,prevy/2], jointAxis= "0 1 0")
                    self.motors.append(prevparentname+"_"+c.names[i])
                else:
                    pyrosim.Send_Joint(name = prevparentname+"_"+c.names[i] , parent= prevparentname , child = c.names[i] , type = "revolute", position = [0,0,prevz], jointAxis= "0 1 0")
                    self.motors.append(prevparentname+"_"+c.names[i])
            i += 1

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


            