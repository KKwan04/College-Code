# Programmer: Kyle Kwan
# Date 10/31/2022
# File Name: Kwan-HiLoGame.py
# Description: This program is a guessing game where you can choose the maximum number you can choose from.  Then you proceed to continue to guess numbers until it matches with
#              the random number that the program selected between the range of 0 and the highest number the user chose.

# Imports the random module.
import random
# This gives protection if a string is inputed instead of an integer.
while True:
    try:
        # User inputs desired maximum number to guess from.
        max_num = int(input("What should the maximum number for this game be? ")) 
    except ValueError:
        continue
    else:
        break
# Computer chooses a random number to guess
random_num = random.randint(1, max_num)
# This gives protection if a string is inputed instead of an integer.
while True:
    try:
        # User inputs their guess.
        guess = int(input("Guess my number: "))
    except ValueError:
        continue
    else:
        break
# Loops and informs user whether they inputted an integer lower or higher than what the computer chose.
while guess != random_num:        
        if guess > random_num:
            print("Your guess is too high.")    
        elif guess < random_num:
            print("Your guess is too low.")
    
        guess = int(input("Guess my number: "))
    
print("You guessed my number!")
replay = input("Do you wish to play again? (Y/N): ")
if replay.lower() == "n":
    print("Thank you for playing!")
        
replay.lower() == "y"
while replay.lower() == "y":
    # This gives protection if a string is inputed instead of an integer.
    while True:
        try:
            # User inputs desired maximum number to guess from.
            max_num = int(input("What should the maximum number for this game be? ")) 
        except ValueError:
            continue
        else:
            break 
    # Computer chooses a random value to guess.
    random_num = random.randint(1, max_num)

    while True:
        try:
            # User inputs their guess.
            guess = int(input("Guess my number: "))
        except ValueError:
            continue
        else:
            break
    # Loops and informs user whether they inputted an integer lower or higher than what the computer chose.
    while guess != random_num:        
        if guess > random_num:
            print("Your guess is too high.")    
        elif guess < random_num:
            print("Your guess is too low.")
    
        guess = int(input("Guess my number: "))
    
    print("You guessed my number!")
    replay = input("Do you wish to play again? (Y/N): ")
    # Breaks the replay loop if user inputs "n".
    if replay.lower() == "n":
        print("Thank you for playing!")
        break
input(f"\nPress enter to exit")