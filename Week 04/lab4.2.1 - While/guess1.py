# Write a program (guess1.py) that prompts the user to guess a number, the
# program should keep prompting the user to guess the number until the user
# gets the right on

#Author: Audrey Allen


numberToGuess = 30
while True:
    number = int(input("Please guess the number:"))
    if (number) != numberToGuess:
       print (f"{number} Please guess again:")
       continue
    else:
       print ("Well done! Yes the number was ", numberToGuess)
    break
