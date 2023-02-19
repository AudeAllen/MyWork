# Write a program (guess1.py) that prompts the user to guess a number, the
# program should keep prompting the user to guess the number until the user
# gets the right on but also tells the user if the answer is too high or too low

#Author: Audrey Allen


numberToGuess = 30
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