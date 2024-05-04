# Week 4 Guess My Number
import random

hidden_number = random.randint(1,10)
guessed = False
msg = ""

while not guessed:
    guessed_number = int(input("What's your guess? "))

    if(guessed_number == hidden_number):
        msg = "You guessed it! Great job!"
        guessed = True
    elif(guessed_number > hidden_number):
        msg = "Lower"
    elif(guessed_number < hidden_number):
        msg = "Higher"
    else:
        msg = "Please guess a number between 1-10"

    print(msg)
print(f"The number was {hidden_number}")