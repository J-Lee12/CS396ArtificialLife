import constants as c
from solution import SOLUTION
import copy
import os
from datetime import datetime
import numpy

class PARALLELHILLCLIMBER:
    
    def __init__(self) -> None:
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm body*.urdf")
        self.parents = {}
        self.nextAvailableID = 0
        self.bestfitness = []
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        self.child = 0

    def Evaluate(self,solutions):
        for i in range(c.populationSize):
            print("\n")
            print(f'I am running this individual {i} in this populationsize {c.populationSize}')
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f'it is currently this time {current_time}\n')
            solutions[i].Start_Simulation("DIRECT")

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
        
        reverse[currmin].Start_Simulation("GUI")

    def Evolve_For_One_Generation(self):
        print('currently evolving')
        self.Spawn(self.nextAvailableID)
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
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
            self.bestfitness.append(self.parents[i].fitness)

    def Save(self):
        temp = numpy.array(self.bestfitness)
        numpy.save('fitness-scores',temp)
        print(f'saved into fitness-scores.npy {self.bestfitness}, {temp}')


    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberofGenerations):
            print(f'evolving {currentGeneration}')
            self.Evolve_For_One_Generation()