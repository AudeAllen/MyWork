# This program   asks the user to enter in a number, and the
# program will tell the user if the number is even or odd.

#Author: Audrey Allen

number = int(input("enter an integer:"))
if (number % 2) == 0:
       print (f"{number} is an even number")
else:
    print(f"{number} is an odd number")