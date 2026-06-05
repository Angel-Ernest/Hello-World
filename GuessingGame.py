import random
import time

x = random.randint(0,9)

guess_count = 0

guess_limit = 3

print("Welcome to my guessing game! \n You will have")
while True:
    if guess_count < guess_limit:
        current_guess = input("Guess a number between 0 and 9: ")
        guess_count += 1
        if current_guess == x:
            print("Congratulations! You won the game!")
            break
        else:
            print("Try again")
    else:
        print("Sorry, you lost")
        break 