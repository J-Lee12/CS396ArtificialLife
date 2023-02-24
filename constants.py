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
numberofGenerations = 5

populationSize = 5

numoflinks = 5

numSensorNeurons = numoflinks + 2
numMotorNeurons = numoflinks + 1
motorJointRange = .45

names = [
    "Apple", "Dog", "Person", "Fox", "Flower", "Neighbor", "Coffee", "Phone", "Table", "Impact",
    "Genshin", "Flute", "Garbage", "Powerade", "construct", "artifact", "feature", "token", "library", 
    "mana", "top", "shuffle", "chair", "stool", "water", "pound"
]

names1 = [
    "Pample", "Essence", "Grace", "Yoojin", "Lee", "My", "Story", "Time", "Math", "Science"
]

names2 = [
    "Because", "I", "Can", "Learn", "Macbook", "Ring", "Orange Juice", "Wood", "Backpack", "North", "Face"
]

names3 = [
    "Concrete", "Car", "Post", "FedEx", "Albion", "Last", "Quarter", "Rocks"
]