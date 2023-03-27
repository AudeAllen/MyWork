import numpy as np
# it is a good idea to have your absolute values set into variables at the beginning of your program
np.random.seed(1)
minSalary= 20000
maxSalary = 80000
numberOfEntries = 10
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
salariesPlus = salaries+5000
print (salariesPlus)

