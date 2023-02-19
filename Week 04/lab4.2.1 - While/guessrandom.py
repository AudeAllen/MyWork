# Write a program (guessrandom.py) thet gets the program to generate a random number between 0 and 100 to
# guess

#Author: Audrey Allen



import random

numberToGuess = random.randint(1, 100)
print("here is a random number {}".format(numberToGuess))


while True:
    number = int(input("Please guess the number:"))
    if (number) != numberToGuess and (number) < numberToGuess: 
       print (f"{number} Please guess again because number is too low:")
       continue
    elif (number) != numberToGuess and (number) > numberToGuess: 
       print (f"{number} Please guess again because number is too high:")
       continue
    else:
       print ("Well done! Yes the number was ", numberToGuess)
    break