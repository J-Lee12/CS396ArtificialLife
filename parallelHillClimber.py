import constants as c
from solution import SOLUTION
import copy
import os

class PARALLELHILLCLIMBER:
    
    def __init__(self) -> None:
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm body*.urdf")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        self.child = 0

    def Evaluate(self,solutions):
        for i in range(c.populationSize):
            print(f'I am running this individual {i} in this populationsize {c.populationSize}')
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
        self.Spawn(self.nextAvailableID)
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self,id):
        self.children = {}
        for parent in self.parents:
            print("\n")
            print(f'here is the current parent {self.parents[parent].myID}\n')
            print(F'here is its weights {self.parents[parent].weights}\n')
            print(f'and here is its links and joints {self.parents[parent].links}, {self.parents[parent].motors}\n')
            currchild = copy.deepcopy(self.parents[parent])
            self.children[parent] = currchild
            self.children[parent].Set_ID()
            print(self.children)
            # print(f'here is the child created {self.children[currchild].myID}')
            # print(f'here are its weights {self.children[currchild].weights}')
            # print(f'here are its links and joints {self.children[parent].links}, {self.children[parent].motors}')
            self.nextAvailableID += 2

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self):
        for i in self.children:
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Evolve(self):
        self.Evaluate(self.parents)
        
        for currentGeneration in range(c.numberofGenerations):
            self.Evolve_For_One_Generation()