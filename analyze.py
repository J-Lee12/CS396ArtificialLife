import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("./data/meow.npy")
frontLegSensorValues = numpy.load("./data/bark.npy")

front = numpy.load("./data/front.npy")
back = numpy.load("./data/back.npy")
matplotlib.pyplot.plot(front,linewidth=4)
matplotlib.pyplot.plot(back)

matplotlib.pyplot.xlabel("Steps")
matplotlib.pyplot.ylabel("Value in Radians")

# matplotlib.pyplot.plot(backLegSensorValues, label='BackLeg', linewidth=2)
# matplotlib.pyplot.plot(frontLegSensorValues, label='FrontLeg')
# matplotlib.pyplot.legend()
matplotlib.pyplot.show()