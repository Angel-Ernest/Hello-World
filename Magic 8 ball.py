import random
import time

print("Welcome to the Magic 8 Ball!")
time.sleep(1) 
Name = input("What is your name? ")
time.sleep(0.5)
print("OK,", Name)

def check(x):
    if x == 1:
        print("Magic 8 ball answer: Yes - definitely")
    elif x == 2:
        print("Magic 8 ball answer: It is decidedly so")
    elif x == 3:
        print("Magic 8 ball answer: Without a doubt")
    elif x == 4:
        print("Magic 8 ball answer: Reply hazy, try again")
    elif x == 5:
        print("Magic 8 ball answer: Ask again later")
    elif x == 6:
        print("Magic 8 ball answer: Better not tell you now")
    elif x == 7:
        print("Magic 8 ball answer: My sources say no")
    elif x == 8:
        print("Magic 8 ball answer: Outlook not so good")
    elif x == 9:
        print("Magic 8 ball answer: Very doubtful")

while True:
  input (Name + ", please do a yes or no question. ")
  x = random.randint(1, 9)
  check(x)
  time.sleep(1)