import constants as c
from solution import SOLUTION
import copy
import os
from datetime import datetime
import numpy

class PARALLELHILLCLIMBER:
    
    def __init__(self) -> None:
        # os.system("rm brain*.nndf")
        # os.system("rm fitness*.txt")
        # os.system("rm body*.urdf")
        self.Erase_Files()
        self.parents = {}
        self.nextAvailableID = 0
        self.bestfitness = []
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        self.child = 0

    def Evaluate(self,solutions,gen):
        for i in range(c.populationSize):
            print("\n")
            print(f'I am running this individual {i} in this populationsize {c.populationSize}')
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f'it is currently this time {current_time}\n')
            solutions[i].Start_Simulation("DIRECT",gen)

        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

    def Print(self):
        print("\n")
        for i in self.parents:
            print(f'parent fitness {self.parents[i].fitness} child fitness {self.children[i].fitness}')
        print("\n")

    def Show_Best(self):
        currmin = float('inf')
        reverse = {}
        for i in self.parents:
            reverse[self.parents[i].fitness] = self.parents[i]
            if self.parents[i].fitness < currmin:
                currparent = self.parents[i]
                currmin = self.parents[i].fitness
        
        f = open('bestid.txt','w')
        f.write(str(reverse[currmin].myID))
        f.close()
        reverse[currmin].Start_Simulation("GUI",c.numberofGenerations-1)

    def Evolve_For_One_Generation(self,num):
        print(f'currently evolving {num}')
        self.Spawn(self.nextAvailableID)
        self.Mutate()
        self.Evaluate(self.children,num)
        self.Print()
        self.Select()
        self.Find_Best_Fitness()
        print('done evolving\n')

    def Spawn(self,id):
        self.children = {}
        for parent in self.parents:
            currchild = copy.deepcopy(self.parents[parent])
            self.children[parent] = currchild
            self.children[parent].Set_ID()
            self.nextAvailableID += 2

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self):
        for i in self.children:
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]
                
            
    def Find_Best_Fitness(self):
        temp = []
        for i in self.parents:
            temp.append(self.parents[i].fitness)
        temp.sort()
        self.bestfitness.append(temp[0])

    def Save(self):
        temp = numpy.array(self.bestfitness)
        numpy.save('fitness-scores',temp)
        print("best fitness from each generation saved into fitness-scores.npy")


    def Evolve(self):
        self.Evaluate(self.parents,0)
        for currentGeneration in range(c.numberofGenerations):
            print(f'evolving {currentGeneration}')
            self.Evolve_For_One_Generation(currentGeneration+1)
    
    def Erase_Files(self):
        i = 0
        while i <= c.numberofGenerations:
            os.system("rm" + " " + str(i)+"*" )
            i += 1