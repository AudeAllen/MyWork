# This program   asks the user to enter in a number, until the number is equal to -1.

#Author: Audrey Allen

while True:
    number = int(input("enter an integer:"))
    if (number) != -1:
       print (f"{number} is not equal to minus 1")
       continue
    else:
        print(f"{number} is equal to minus 1")
    break
