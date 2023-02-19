# This program reads in
# a students percentage
# and prints out the
# corresponding grade
# Modify the grade.py program to allow for percentags with decimal places
# Author: Audrey Allen


percentage = float(input("Enter the percentage: "))
roundedpercentage =     round(percentage)
#print (percentage)
# be careful with ands and ors
if roundedpercentage < 0 or roundedpercentage > 100:
 # Later we will show you error handling
 # This should really throw an error
 print ("Please enter a number between 0 and 100")
elif roundedpercentage < 40: # we know it is greater than 0
 print ("Fail")
elif roundedpercentage < 50: # between 40 and 49
 print ("Pass")
elif roundedpercentage < 60: # between 50 and 59
 print ("Merit1")
elif roundedpercentage < 70: # between 60 and 69
 print ("Merit2")
else: # the only option left is between 70 and 100
 print ("Distinction")
