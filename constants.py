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

populationSize = 1

# numoflinks = numpy.random.randint(10,20)
numoflinks = 40

numSensorNeurons = numoflinks + 2
numMotorNeurons = numoflinks + 1
motorJointRange = .45

names = [
    "Apple", "Dog", "Person", "Fox", "Flower", "Neighbor", "Coffee", "Phone", "Table", "Impact",
    "Genshin", "Flute", "Garbage", "Powerade", "Construct", "Artifact", "Feature", "Token", "Library", 
    "Mana", "Top", "Shuffle", "Chair", "Stool", "Water", "Pound", "Computer", "Bottle", "Clock", "Lamp",
    "Systems", "A", "Programmer", "Perspective", "Cracking", "The", "Code", "Interview", "Linear", "Algebra",
    "It's", "Applications"
]