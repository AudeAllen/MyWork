import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('carcrashes.txt')

minSalary = data[:,0]
maxSalary = data[:,1]
numberOfEntries = 3

salaries = (minSalary, maxSalary, numberOfEntries)
plt.hist(salaries)
plt.show()


