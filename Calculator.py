print("Scalculator, basic calculator for basic caclculations")
Z1 = input("First number: ")
Z2 = input("Second number: ")
W1 = input("What do you want to add, subtract, multiply, or divide? ")
if W1 == "add":
    print(float(Z1) + float(Z2))
elif W1 == "subtract":
    print(float(Z1) - float(Z2))
elif W1 == "multiply":
    print(float(Z1) * float(Z2))
elif W1 == "divide":
    print(float(Z1) / float(Z2))
