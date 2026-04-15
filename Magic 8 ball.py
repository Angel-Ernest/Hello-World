import random
import time

print("Welcome to the Magic 8 Ball!")
time.sleep(1) 
Name = input("What is your name? ")
time.sleep(0.5)
print("OK,", Name)

def check(x):
    if x == 1:
        print("Yes - definitely")
    elif x == 2:
        print("It is decidedly so")
    elif x == 3:
        print("Without a doubt")
    elif x == 4:
        print("Reply hazy, try again")
    elif x == 5:
        print("Ask again later")#last one i did
    elif x == 6:
        print("As I see it, yes")
    elif x == 7:
        print("Most likely")
    elif x == 8:
        print("Outlook good")
    elif x == 9:
        print("Yes")

while True:
  input (Name + ", please do a yes or no question. ")
  x = random.randint(1, 9)
  check(x)
  time.sleep(1)