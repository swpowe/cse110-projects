# Project 04: Word Puzzle
## I randomized the secret word from a list
## I added a way to give up and reveal the word
## I use a variable to switch between try and tries depending on the number of guesses

# Have a secret word stored in the program.
import random
# Prompt the user for a guess.
# Continue looping as long as that guess is not correct.
# Calculate the number of guesses and display it at the end.
secret_words = ["temple", "Mosiah", "Spirit", "Christ", "Savior", "Lord", "Sabbath"]

secret_word = random.choice(secret_words).lower()
# guess = input("What is your guess? ").lower()
guess = ""
count = 0
form = "tries"

print("Welcome to the word guessing game!")
print()
print("Your hint is: ", end="")

for letter in secret_word:
    print("_ ", end="")

while guess != secret_word:
    guess = input("\nWhat is your guess? ").lower()
    
    if guess == "give up":
        break
    
    if len(guess) == len(secret_word): # same length
        
        if guess != secret_word: # guess doesn't match
            
            for i in range(len(guess)): # check each letter
                
                if guess[i] in secret_word: # is letter found in word?
                    if guess[i] == secret_word[i]: # correct location
                      print(f"{guess[i].upper()} ", end="")
                    else:
                        print(f"{guess[i]} ", end="")
                else:
                    print("_ ", end="")
        
    else: # different length
        print("Sorry, the guess must have the same number of letters as the secret word.")
        
    count += 1
 
if count == 1:
    form = "try" 

if guess == "give up":
    print(f"The word was {secret_word}")
else:    
    print(f"You guessed it! It only took you {count} {form}!")