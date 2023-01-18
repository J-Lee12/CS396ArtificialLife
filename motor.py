import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:

	def __init__(self,jointName):
		
		self.jointName = jointName
		self.Prepare_To_Act()
		print(self.jointName)
		if self.jointName == "Torso_BackLeg":
			print("your mom")
		else:
			print("bark")

	def Prepare_To_Act(self):
		if self.jointName == "Torso_BackLeg":
			self.amplitude = c.frontamplitude
			self.frequency = c.frontfrequency/2
			self.offset = c.frontphaseOffset
		else:
			self.amplitude = c.frontamplitude
			self.frequency = c.frontfrequency
			self.offset = c.frontphaseOffset
		# i = 0
		# while i < 1000:
		# 	frontLegtargetAngles[i] = (((frontLegtargetAngles[i] - -1)* c.NewRange)/ c.OldRange) + -numpy.pi/4
		# 	i += 1
		self.motorValues =  self.amplitude * numpy.sin(self.frequency * numpy.linspace(0,2*numpy.pi,c.steps) + self.offset)

	def Set_Value(self,robotId,desiredAngle):
		pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = desiredAngle,
        maxForce = 500)