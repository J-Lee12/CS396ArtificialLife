import numpy
import matplotlib.pyplot as plt

data1 = numpy.load("fitness-scores1.npy")
data1 = data1 * -1

data2= numpy.load("fitness-scores2.npy")
data2 = data2 * -1

data3 = numpy.load("fitness-scores3.npy")
data3 = data3 * -1

data4 = numpy.load("fitness-scores4.npy")
data4 = data4 * -1

data5 = numpy.load("fitness-scores5.npy")
data5 = data5 * -1



plt.plot(data1, label="Seed1")
plt.plot(data2, label="Seed2")
plt.plot(data3, label="Seed3")
plt.plot(data4, label="Seed4")
plt.plot(data5, label="Seed5")

plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("Best Fitness From Each Generation of a Population Size of 25")
plt.legend()
plt.show()