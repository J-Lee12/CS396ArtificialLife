import numpy

frontamplitude = 3
frontfrequency = 1
frontphaseOffset = 0

backamplitude = numpy.pi/10
backfrequency = 8
backphaseOffset = 0

steps = 1000
OldRange = (1 - -1)
NewRange = (numpy.pi/4 - -numpy.pi/4)
numberofGenerations = 1

populationSize = 2

numSensorNeurons = 7
numMotorNeurons = 6
motorJointRange = 1