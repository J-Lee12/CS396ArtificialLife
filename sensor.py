import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:

	def __init__(self,linkName):
		self.values = numpy.zeros(c.steps)
		self.linkName = linkName

	def Get_Value(self,i):
		self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

	# def Save_Values(self):
	# 	numpy.save("./data/bark.npy",frontLegSensorValues)
	# 	numpy.save("./data/meow.npy",backLegSensorValues)