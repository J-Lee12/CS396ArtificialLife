import constants as c
from solution import SOLUTION
import copy

class HILLCLIMBER:
    
    def __init__(self) -> None:
        
        self.parent = SOLUTION()
        self.child = 0

    def Print(self):
        print(self.parent.fitness,self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate("GUI")

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Evolve(self):
        self.parent.Evaluate("GUI")

        for currentGeneration in range(c.numberofGenerations):
            self.Evolve_For_One_Generation()