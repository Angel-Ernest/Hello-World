import random
import time

x = random.randint(0,9)

guess_count = 0

guess_limit = 3

while True:
    if guess_count < guess_limit:
        current_guess = input("Guess a number betwee 0 and 9: ")
        if current_guess == x:
            break
        else:
            print("hi")