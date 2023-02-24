import numpy
import random
import os
import pyrosim.pyrosim as pyrosim
import time
import constants as c
import random


class SOLUTION:

    def __init__(self,ID) -> None:
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
        self.counter = 0
        self.first_link = []

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

    def Random_Side(self, currside):
        sides = {
            "x": ["x","y","z"],
            "y": ["x","y","z"],
            "z": ["x","y","z"],
        }
        currchoices = sides[currside]
        return currchoices[numpy.random.randint(0,3)]


    def Generate_Face(self,i,prevside):

        newx = numpy.random.uniform(0,2)
        newy = numpy.random.uniform(0,2)
        newz = numpy.random.uniform(0,2)

        if self.Random_Side(prevside) == "x":
            if bool(random.getrandbits(1)):
                pyrosim.Send_Cube(name=c.names[i], pos=[newx/2,0,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
                self.sensors.append(c.names[i])
            else:
                pyrosim.Send_Cube(name=c.names[i], pos=[newx/2,0,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
            
            self.links.append([newx,newy,newz])
            return [newx,newy,newz,"x"]
        
        elif self.Random_Side(prevside) == "y":
            if bool(random.getrandbits(1)):
                pyrosim.Send_Cube(name=c.names[i], pos=[0,newy/2,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
                self.sensors.append(c.names[i])
            else:
                pyrosim.Send_Cube(name=c.names[i], pos=[0,newy/2,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
            
            self.links.append([newx,newy,newz])
            return [newx,newy,newz,"y"]
        
        else:
            if bool(random.getrandbits(1)):
                pyrosim.Send_Cube(name=c.names[i], pos=[0,0,newz/2], size=[newx,newy,newz],color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
                self.sensors.append(c.names[i])
            else:
                pyrosim.Send_Cube(name=c.names[i], pos=[0,0,newz/2], size=[newx,newy,newz],color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
            
            self.links.append([newx,newy,newz])
            return [newx,newy,newz,"z"]

    def Create_Body(self):
        print(f'create body is getting called')
        x = numpy.random.uniform(0,4)
        y = numpy.random.uniform(0,4)
        z = numpy.random.uniform(0,4)
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

        self.motors.append("Torso_"+c.names[0])    
        
        if bool(random.getrandbits(1)):
            pyrosim.Send_Cube(name=c.names[0], pos=[x/2,0,0], size=[x,y,z], color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
            self.sensors.append(c.names[0])
        else:
            pyrosim.Send_Cube(name=c.names[0], pos=[x/2,0,0], size=[x,y,z], color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
        
        self.first_link.append(["Torso",[start,1,1]])

        i = 1
        prevface = "x"
        
        prevx = x
        prevy = y
        prevz = z
        print(c.numoflinks)
        while i < c.numoflinks:
            print(i)
            if i == 1:
                temp = self.Generate_Face(i,prevface)
                pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [prevx,0,0], jointAxis= "0 1 0")
                self.motors.append(c.names[i-1]+"_"+c.names[i])
                prevx = temp[0]
                prevy = temp[1]
                prevz = temp[2]
                prevface = temp[3]
                i += 1
            else:
                temp = self.Generate_Face(i,prevface)
                if temp[3] == "x":
                    if prevface == "x":
                        pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [prevx,0,0], jointAxis= "0 1 0")
                        self.motors.append(c.names[i-1]+"_"+c.names[i])

                        x = numpy.random.uniform(0,4)
                        y = numpy.random.uniform(0,4)
                        z = numpy.random.uniform(0,4)

                        pyrosim.Send_Cube(name=c.names1[i], pos=[0,y/2,0], size=[x,y,z], color='    <color rgba="0 0 0.5 1"/>', colorname = '<material name="Ryan">')
                        pyrosim.Send_Joint(name = c.names[i]+"_"+c.names1[i] , parent= c.names[i] , child = c.names1[i] , type = "revolute", position = [temp[0]/2,temp[1]/2,0], jointAxis= "0 1 0")
                        self.motors.append(c.names[i]+"_"+c.names1[i])
                        
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1

                    elif prevface == "y":
                        pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [prevx/2,prevy/2,0], jointAxis= "0 1 0")
                        self.motors.append(c.names[i-1]+"_"+c.names[i])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1
                    
                    else:
                        pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [prevx/2,0,prevz/2], jointAxis= "0 1 0")
                        self.motors.append(c.names[i-1]+"_"+c.names[i])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1

                elif temp[3] == "y":
                    if prevface == "y":
                        pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [0,prevy,0], jointAxis= "0 1 0")
                        self.motors.append(c.names[i-1]+"_"+c.names[i])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1
                    
                    elif prevface == "x":
                        pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [prevx/2,prevy/2,0], jointAxis= "0 1 0")
                        self.motors.append(c.names[i-1]+"_"+c.names[i])

                        x = numpy.random.uniform(0,4)
                        y = numpy.random.uniform(0,4)
                        z = numpy.random.uniform(0,4)
                        pyrosim.Send_Cube(name=c.names1[i], pos=[0,0,z/2], size=[x,y,z], color='    <color rgba="1 0.5 0.5 1"/>', colorname = '<material name="Quin">')

                        pyrosim.Send_Joint(name = c.names[i]+"_"+c.names1[i] , parent= c.names[i] , child = c.names1[i] , type = "revolute", position = [0,temp[1]/2,temp[2/2]], jointAxis= "0 1 0")
                        self.motors.append(c.names[i]+"_"+c.names1[i])

                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1

                    else:
                        pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [0,prevy/2,prevz/2], jointAxis= "0 1 0")
                        self.motors.append(c.names[i-1]+"_"+c.names[i])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1

                else:
                    if prevface == "z":
                        pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [0,0,prevz], jointAxis= "0 1 0")
                        self.motors.append(c.names[i-1]+"_"+c.names[i])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1

                    elif prevface == "x":
                        pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [prevx/2,0,prevz/2], jointAxis= "0 1 0")
                        self.motors.append(c.names[i-1]+"_"+c.names[i])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1
                    
                    else:
                        pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [0,prevy/2,prevz/2], jointAxis= "0 1 0")
                        self.motors.append(c.names[i-1]+"_"+c.names[i])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
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
        ## changes the snyaptic weights of the brain
        row = random.randint(0,(c.numSensorNeurons - 1))
        column = random.randint(0,(c.numMotorNeurons - 1))
        self.weights[row,column] = random.random() * 2 - 1



            