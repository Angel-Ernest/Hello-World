import time

score = 0

def check(answer):
    global score
    if answer == "Cell":
        print("Correct")
        score += 1
        return 1
    elif answer == "acute":        
        print("Correct")
        score += 1
        return 1
    elif answer == "9.8":
        print("Correct")
        score += 1
        return 1
    else:
        print("Wrong")
        return 0

print("Welcome to the Math-science quiz (easy)! Let's see what are you capable of!")

R1 = input("What is the basic unit of life?")
      
check(R1)

time.sleep(1)

R2 = input("An equilateral triangle has _______ angles")

check(R2)

time.sleep(1)

R3 = input ("The gravitational pull of the gravity in Earth is around (to the nearest tenth) ____ m/s")
check(R3)

print("Your score is," , score)
