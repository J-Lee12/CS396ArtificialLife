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

        self.Generate_Body()
        # self.counter = 0

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
                self.links.append([c.names[i],[newx/2,0,0],[newx,newy,newz],'    <color rgba="0 1.0 0 1.0"/>','<material name="Green">'])
                self.sensors.append(c.names[i])
            else:
                self.links.append([c.names[i],[newx/2,0,0],[newx,newy,newz],'    <color rgba="0 1.0 1.0 1.0"/>','<material name="Cyan">'])
            return [newx,newy,newz,"x"]
        
        elif self.Random_Side(prevside) == "y":
            if bool(random.getrandbits(1)):
                self.links.append([c.names[i],[0,newy/2,0],[newx,newy,newz],'    <color rgba="0 1.0 0 1.0"/>','<material name="Green">'])
                self.sensors.append(c.names[i])
            else:
                self.links.append([c.names[i],[0,newy/2,0],[newx,newy,newz],'    <color rgba="0 1.0 1.0 1.0"/>','<material name="Cyan">'])
            return [newx,newy,newz,"y"]
        
        else:
            if bool(random.getrandbits(1)):
                self.links.append([c.names[i],[0,0,newz/2],[newx,newy,newz],'    <color rgba="0 1.0 0 1.0"/>','<material name="Green">'])
                self.sensors.append(c.names[i])
            else:
                self.links.append([c.names[i],[0,0,newz/2],[newx,newy,newz],'    <color rgba="0 1.0 1.0 1.0"/>','<material name="Cyan">'])
            return [newx,newy,newz,"z"]
        
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        for link in self.links:
            naming = link[0]
            positioning = link[1]
            sizing = link[2]
            coloring = link[3]
            colornaming = link[4]
            pyrosim.Send_Cube(name=naming,pos=positioning,size=sizing,color=coloring,colorname=colornaming)

        for joint in self.motors:
            jointname = joint[0]
            jointparent = joint[1]
            jointchild = joint[2]
            jointposition = joint[3]
            pyrosim.Send_Joint(name=jointname,parent=jointparent,child=jointchild,type= "revolute",position=jointposition,jointAxis="0 1 0")
        pyrosim.End()



    def Generate_Body(self):

        if len(self.links) != 0:
            return

        x = numpy.random.uniform(0,4)
        y = numpy.random.uniform(0,4)
        z = numpy.random.uniform(0,4)
        start = numpy.random.uniform(0,2)
        xpos = numpy.random.randint(-4,4)

        if bool(random.getrandbits(1)):
            ## if true then it has a sensor
            self.links.append(["Torso",[xpos,0,3],[start,1,1],'    <color rgba="0 1.0 0 1.0"/>','<material name="Green">']) 
            self.motors.append(["Torso_"+c.names[0],"Torso",c.names[0],[xpos+start/2,0,3]])
            self.sensors.append("Torso")

        else:
            ## if false then no sensor
            self.motors.append(["Torso_"+c.names[0],"Torso",c.names[0],[xpos+start/2,0,3]])
            self.links.append(["Torso",[xpos,0,3],[start,1,1],'    <color rgba="0 1.0 1.0 1.0"/>','<material name="Cyan">']) 

        if bool(random.getrandbits(1)):
            self.links.append([c.names[0],[x/2,0,0],[x,y,z],'    <color rgba="0 1.0 0 1.0"/>','<material name="Green">'])
            self.sensors.append(c.names[0])
        else:
            self.links.append([c.names[0],[x/2,0,0],[x,y,z],'    <color rgba="0 1.0 1.0 1.0"/>','<material name="Cyan">'])
        
        i = 1
        prevface = "x"
        
        prevx = x
        prevy = y
        prevz = z
        while i < c.numoflinks:
            if i == 1:
                temp = self.Generate_Face(i,prevface)
                self.motors.append([c.names[i-1]+"_"+c.names[i],c.names[i-1], c.names[i], [prevx,0,0]])
                prevx = temp[0]
                prevy = temp[1]
                prevz = temp[2]
                prevface = temp[3]
                i += 1
            else:
                temp = self.Generate_Face(i,prevface)
                if temp[3] == "x":
                    if prevface == "x":
                        self.motors.append([c.names[i-1]+"_"+c.names[i],c.names[i-1],c.names[i],[prevx,0,0]])

                        x = numpy.random.uniform(0,4)
                        y = numpy.random.uniform(0,4)
                        z = numpy.random.uniform(0,4)
                        self.motors.append([c.names[i]+"_"+c.names1[i],c.names[i],c.names1[i],[temp[0]/2,temp[1]/2,0]])
                        self.links.append([c.names1[i],[0,y/2,0],[x,y,z],'    <color rgba="0 0 0.5 1"/>','<material name="Ryan">'])
    
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1

                    elif prevface == "y":
                        self.motors.append([c.names[i-1]+"_"+c.names[i],c.names[i-1],c.names[i],[prevx/2,prevy/2,0]])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1
                    
                    else:
                        self.motors.append([c.names[i-1]+"_"+c.names[i],c.names[i-1],c.names[i],[prevx/2,0,prevz/2]])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1

                elif temp[3] == "y":
                    if prevface == "y":
                        self.motors.append([c.names[i-1]+"_"+c.names[i],c.names[i-1],c.names[i],[0,prevy,0]])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1
                    
                    elif prevface == "x":
                        self.motors.append([c.names[i-1]+"_"+c.names[i],c.names[i-1],c.names[i],[prevx/2,prevy/2,0]])
                        x = numpy.random.uniform(0,4)
                        y = numpy.random.uniform(0,4)
                        z = numpy.random.uniform(0,4)
                        self.motors.append([c.names[i]+"_"+c.names1[i],c.names[i],c.names1[i],[0,temp[1]/2,temp[2]/2]])
                        self.links.append([c.names2[i],[0,0,z/2],[x,y,z],'    <color rgba="1 0.5 0.5 1"/>','<material name="Quin">'])

                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1

                    else:
                        self.motors.append([c.names[i-1]+"_"+c.names[i],c.names[i-1],c.names[i],[0,prevy/2,prevz/2]])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1

                else:
                    if prevface == "z":
                        self.motors.append([c.names[i-1]+"_"+c.names[i],c.names[i-1],c.names[i],[0,0,prevz]])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1

                    elif prevface == "x":
                        self.motors.append([c.names[i-1]+"_"+c.names[i],c.names[i-1],c.names[i],[prevx/2,0,prevz/2]])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1
                    
                    else:
                        self.motors.append([c.names[i-1]+"_"+c.names[i],c.names[i-1],c.names[i],[0,prevy/2],prevz/2])
                        prevx = temp[0]
                        prevy = temp[1]
                        prevz = temp[2]
                        prevface = temp[3]
                        i += 1

    def Create_Brain(self):
         #Brain creation
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        
        count = 0
        for i in self.sensors:
            pyrosim.Send_Sensor_Neuron(name= count, linkName=i)
            count += 1
        
        for j in self.motors:
            pyrosim.Send_Motor_Neuron(name=count, jointName=j[0])
            count += 1

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()        

    def Mutate(self):
        ## changes the snyaptic weights of the brain
        print("\n")
        print(f'here is my id {self.myID}\n')
        print(f'here are the links {self.links}\n')
        print(f'here are the joints {self.motors}\n')
        print(f'here are the motors {self.motors}\n')
        print("\n")

        row = random.randint(0,(c.numSensorNeurons - 1))
        column = random.randint(0,(c.numMotorNeurons - 1))
        self.weights[row,column] = random.random() * 2 - 1

        # print("\n")
        # print(f'here are the links {self.links}')

        # ## change the size of the x,y,z of the first link
        # firstlink = self.links[0]
        # firstjoint = self.motors[0]
        # start = firstlink[2][0]
        # print("\n")
        # print(f'here is start {start}')

        # print("\n")
        # print(f'before modifiying here is firstlink {firstlink}')
        # print(f'before modifiying here is firstjoint {firstjoint}\n')

        # xlength = numpy.random.uniform(0,2)
        # ylength = numpy.random.uniform(0,2)
        # zlength = numpy.random.uniform(0,2)

        # firstlink[2] = [xlength,ylength,zlength]
        # firstjoint[3] = [xlength+start/2,0,3]

        # print("\n")
        # print(f'after modifiying here is firstlink {self.links[0]}')
        # print(f'after modifiying here is firstjoint {self.motors[0]}\n')
        
    







            