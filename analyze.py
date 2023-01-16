import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("./data/meow.npy")
frontLegSensorValues = numpy.load("./data/bark.npy")
print(backLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues, label='BackLeg', linewidth=2)
matplotlib.pyplot.plot(frontLegSensorValues, label='FrontLeg')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()