# Program that takes in a float amount of dollars and returns the absolute in cent
# 
# Author: Audrey Allen



number = float(input("Enter a number:"))

absoluteValue = abs(number*100)

Answer1 =  int(absoluteValue)

print('The amount in cent of {} is {}'.format(number, Answer1))
