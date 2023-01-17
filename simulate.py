import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

frontamplitude = 0
frontfrequency = 5
frontphaseOffset = 0

backamplitude = numpy.pi/10
backfrequency = 8
backphaseOffset = 0

x = numpy.linspace(0,2*numpy.pi,1000)
frontLegtargetAngles = frontamplitude * numpy.sin(frontfrequency * x + frontphaseOffset)
i = 0
OldRange = (1 - -1)
NewRange = (numpy.pi/4 - -numpy.pi/4)
while i < 1000:
	frontLegtargetAngles[i] = (((frontLegtargetAngles[i] - -1)* NewRange)/ OldRange) + -numpy.pi/4
	i += 1

y = numpy.linspace(0,2*numpy.pi,1000)
backLegtargetAngles = backamplitude * numpy.sin(backfrequency * y + backphaseOffset)
i = 0
OldRange = (1 - -1)
NewRange = (numpy.pi/4 - -numpy.pi/4)
while i < 1000:
	backLegtargetAngles[i] = (((backLegtargetAngles[i] - -1)* NewRange)/ OldRange) + -numpy.pi/4
	i += 1

# numpy.save("./data/front.npy", frontLegtargetAngles)
# numpy.save("./data/back.npy", backLegtargetAngles)
# quit()

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
for i in range(0,1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = 'Torso_BackLeg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = backLegtargetAngles[i],
	maxForce = 500)
	
	pyrosim.Set_Motor_For_Joint(
	bodyIndex = robotId,
	jointName = 'Torso_FrontLeg',
	controlMode = p.POSITION_CONTROL,
	targetPosition = frontLegtargetAngles[i],
	maxForce = 500)
	time.sleep(1/60)

	
numpy.save("./data/bark.npy",frontLegSensorValues)
numpy.save("./data/meow.npy",backLegSensorValues)