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
numberofGenerations = 10

populationSize = 10

numSensorNeurons = 10
numMotorNeurons = 8
motorJointRange = .2