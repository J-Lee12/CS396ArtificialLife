import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = .5

for x in range(5):
    for y in range(5):
        i = 1
        while i < 11:
            pyrosim.Send_Cube(name="Box", pos=[x,y,i], size=[length - (i *.1),width - (i *.1),height - (i*.1)])
            i += 1

pyrosim.End()