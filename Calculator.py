import sys

print("Scalculator, basic calculator for basic caclculations")
try:
   Z1 = int(input("First number: "))
except ValueError:
    print("Please enter a valid number")
    sys.exit(0)

try:
    Z2 = int(input("Second number: "))
except ValueError:
    print("Please enter a valid number")
    sys.exit(0)

W1 = input("What do you want to add, subtract, multiply, or divide? ")
if W1 == "add":
    print(float(Z1) + float(Z2))
elif W1 == "subtract":
    print(float(Z1) - float(Z2))
elif W1 == "multiply":
    print(float(Z1) * float(Z2))
elif W1 == "divide":
    print(float(Z1) / float(Z2))
else :
    print("Please enter a valid operation")