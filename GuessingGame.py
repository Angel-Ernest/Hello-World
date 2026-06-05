import random
import time

x = random.randint(0,9) #Do a random number between 0 and 9

guess_count = 0

guess_limit = 5

print("Welcome to my guessing game! \n You will have 5 tries to guess")
time.sleep(1)
while True:
    if guess_count < guess_limit:
        current_guess = input("Guess a number between 0 and 9: ")
        guess_count += 1
        if x == int(current_guess):
            print("Congratulations! You won the game!")
            break
        else:
            print("Try again")
            if x > int(current_guess):
                print("Hint: The number is higher")
            elif x < int(current_guess):
                print("Hint: The number is lower")
    else:
        print("Sorry, you lost")
        print(x)
        break 