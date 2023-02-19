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

    def Random_Side(self, currside):

        # sides = {
        #     "x": ["-x","y","-y","z","-z"],
        #     "-x": ["x", "y", "-y", "z", "-z"],
        #     "y": ["x", "-x", "-y", "z", "-z"],
        #     "-y": ["x", "-x", "y", "z", "-z"],
        #     "z": ["x", "-x", "y", "-y", "-z"],
        #     "-z": ["x", "-x", "y", "-y", "z"]
        # }

        sides = {
            "x": ["y","z"],
            "y": ["x","z"],
            "z": ["x","y"],
        }

        currchoices = sides[currside]
        return currchoices[numpy.random.randint(0,1)]

    def Generate_Face(self,i,prevside):

        ## given an x y z coordinate of a joint randomly generate a cube and a joint
        ## return the x y z corrdinate of the joint

        newx = numpy.random.uniform(0,2)
        newy = numpy.random.uniform(0,2)
        newz = numpy.random.uniform(0,2)

        if self.Random_Side(prevside) == "x":
            if bool(random.getrandbits(1)):
                pyrosim.Send_Cube(name=c.names[i], pos=[newx/2,0,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
                self.sensors.append(c.names[i])
            else:
                pyrosim.Send_Cube(name=c.names[i], pos=[newx/2,0,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
            return [newx,"x"]

        # elif self.Random_Side(prevside) == "-x":
        #     if bool(random.getrandbits(1)):
        #         pyrosim.Send_Cube(name=c.names[i], pos=[-1*(newx/2),0,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
        #     else:
        #         pyrosim.Send_Cube(name=c.names[i], pos=[-1*(newx/2),0,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
        #     return [newx,"-x"]
        
        elif self.Random_Side(prevside) == "y":
            if bool(random.getrandbits(1)):
                pyrosim.Send_Cube(name=c.names[i], pos=[0,newy/2,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
                self.sensors.append(c.names[i])
            else:
                pyrosim.Send_Cube(name=c.names[i], pos=[0,newy/2,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
            return [newy,"y"]
        
        # elif self.Random_Side(prevside) == "-y":
        #     if bool(random.getrandbits(1)):
        #         pyrosim.Send_Cube(name=c.names[i], pos=[0,-1*(newy/2),0], size=[newx,newy,newz],color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
        #         self.sensors.append(c.names[i])
        #     else:
        #         pyrosim.Send_Cube(name=c.names[i], pos=[0,-1*(newy/2),0], size=[newx,newy,newz],color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
        #     return [newy,"-y"]
        
        elif self.Random_Side(prevside) == "z":
            if bool(random.getrandbits(1)):
                pyrosim.Send_Cube(name=c.names[i], pos=[0,0,newz/2], size=[newx,newy,newz],color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
                self.sensors.append(c.names[i])
            else:
                pyrosim.Send_Cube(name=c.names[i], pos=[0,0,newz/2], size=[newx,newy,newz],color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
            return [newz,"z"]
        
        # elif self.Random_Side(prevside) == "-z":
        #     if bool(random.getrandbits(1)):
        #         pyrosim.Send_Cube(name=c.names[i], pos=[0,0,-1*(newz/2)], size=[newx,newy,newz],color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
        #         self.sensors.append(c.names[i])
        #     else:
        #         pyrosim.Send_Cube(name=c.names[i], pos=[0,0,-1*(newz/2)], size=[newx,newy,newz],color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
        #     return [newz,"-z"]
        
    def Create_Body(self):
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

        self.motors.append("Torso_"+c.names[0])    
        
        if bool(random.getrandbits(1)):
            pyrosim.Send_Cube(name=c.names[0], pos=[x/2,0,0], size=[x,y,z], color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
            self.sensors.append(c.names[0])
        else:
            pyrosim.Send_Cube(name=c.names[0], pos=[x/2,0,0], size=[x,y,z], color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
        i = 1

        prevface = "x"
        while i < c.numoflinks:
            if i == 1:
                temp = self.Generate_Face(i,prevface)
                pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [temp[0],0,0], jointAxis= "0 1 0")
                self.motors.append(c.names[i-1]+"_"+c.names[i])
                prevface = temp[1]
                i += 1
            else:
                temp = self.Generate_Face(i,prevface)
                print(temp[1])
                if temp[1] == "x":
                    pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [temp[0],0,0], jointAxis= "0 1 0")
                    self.motors.append(c.names[i-1]+"_"+c.names[i])
                    prevface = temp[1]
                    i += 1

                elif temp[1] == "y":
                    pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [0,temp[0],0], jointAxis= "0 1 0")
                    self.motors.append(c.names[i-1]+"_"+c.names[i])
                    prevface = temp[1]
                    i += 1

                else:
                    pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [0,0,temp[1]], jointAxis= "0 1 0")
                    self.motors.append(c.names[i-1]+"_"+c.names[i])
                    prevface = temp[1]
                    i += 1
        pyrosim.End()
    


    # def Create_Body(self):
    #     #Robot creation
    #     x = numpy.random.uniform(0,2)
    #     y = numpy.random.uniform(0,2)
    #     z = numpy.random.uniform(0,2)
    #     start = numpy.random.uniform(0,2)
    #     pyrosim.Start_URDF("body.urdf")
    #     xpos = numpy.random.randint(-4,4)

    #     if bool(random.getrandbits(1)):
    #         ## if true then it has a sensor
    #         pyrosim.Send_Cube(name="Torso", pos=[xpos,0,3], size=[start,1,1], color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
    #         pyrosim.Send_Joint(name = "Torso_"+c.names[0] , parent= "Torso" , child = c.names[0] , type = "revolute", position = [xpos + start/2,0,3], jointAxis= "0 1 0")
    #         self.sensors.append("Torso")

    #     else:
    #         ## if false then no sensor
    #         pyrosim.Send_Cube(name="Torso", pos=[xpos,0,3], size=[start,1,1], color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
    #         pyrosim.Send_Joint(name = "Torso_"+c.names[0] , parent= "Torso" , child = c.names[0] , type = "revolute", position = [xpos + start/2,0,3], jointAxis= "0 1 0")

    #     self.motors.append("Torso_"+c.names[0])    
    
    #     if bool(random.getrandbits(1)):
    #         pyrosim.Send_Cube(name=c.names[0], pos=[x/2,0,0], size=[x,y,z], color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
    #         self.sensors.append(c.names[0])
    #     else:
    #         pyrosim.Send_Cube(name=c.names[0], pos=[x/2,0,0], size=[x,y,z], color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')

    #     prevx = x 
    #     i = 1
    #     while i < c.numoflinks:
    #         newx = numpy.random.uniform(0,2)
    #         newy = numpy.random.uniform(0,2)
    #         newz = numpy.random.uniform(0,2)
            
    #         if bool(random.getrandbits(1)):
    #             pyrosim.Send_Cube(name=c.names[i], pos=[newx/2,0,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 0 1.0"/>', colorname = '<material name="Green">')
    #             self.sensors.append(c.names[i])
    #         else:
    #             pyrosim.Send_Cube(name=c.names[i], pos=[newx/2,0,0], size=[newx,newy,newz],color='    <color rgba="0 1.0 1.0 1.0"/>', colorname = '<material name="Cyan">')
            
    #         pyrosim.Send_Joint(name = c.names[i-1]+"_"+c.names[i] , parent= c.names[i-1] , child = c.names[i] , type = "revolute", position = [prevx,0,0], jointAxis= "0 1 0")
    #         self.motors.append(c.names[i-1]+"_"+c.names[i])
    #         prevx = newx
    #         i += 1

    #     pyrosim.End()

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


            