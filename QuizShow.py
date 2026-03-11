import time

score = 0

print("Welcome to the Math-science quiz (easy)! Let's see what are you capable of!")

R1 = input("What is the basic unit of life?")

if R1 == "Cell":
    print("Correct")
    score += 1
else:
    print("Wrong")

time.sleep(1)

R2 = input("An equilateral triangle has _______ angles")

if R2 == "acute":
    print("Correct")
    score += 1
else:
    print("Wrong")

time.sleep(1)

R3 = input ("The gravitational pull of the gravity in Earth is around (to the nearest tenth) ____ m/s")

if R3 == "9.8":
    print("Correct")
    score += 1
else:
    print("Wrong")

time.sleep(1)

print("Your score is," , score)
