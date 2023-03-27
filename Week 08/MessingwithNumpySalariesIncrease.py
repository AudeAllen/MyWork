import numpy as np
# it is a good idea to have your absolute values set into variables at the beginning of your program
np.random.seed(1)
minSalary= 20000
maxSalary = 80000
numberOfEntries = 10
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
# you can also multiply
salariesMult = salaries * 1.05 # add 5% by multiplying by 1.05
print(salariesMult)
# This is a float array, here I convert it to an int array (it does a floor)
newSalaries = salariesMult.astype(int)
print(newSalaries)