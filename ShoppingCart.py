import time

Cart ={

}

Stock = {
    "Apple" : 0.75,    
    "Bread" : 4.50, 
    "Carrot" : 0.50,
    "Donut" : 1.25,
    "Eggs" : 3.99,
    "Flour" : 6.00,
    "Grape" : 0.05,
    "Honey" : 8.00,
}

print("Heres's what we have in stock: ")
for key, value in Stock.items():
    print(f"{key}    {value}") #f allows to the code to replace the word that is in the brackets with the value of the variable

time.sleep(1)

T = True

while T:
    item = input("What would you like to buy? (Or type 'checkout' to finish) ")
    if item in Stock:
        Cart[item] = Stock[item] #Copy the item written to the other dictionary
        for i, x in enumerate(Cart, start = 1): #i and x are not special variables, but they are used to count
            print(f"{i}. {x}   {Cart[x]}")
        print(f"Total:      {sum(Cart.values())}")
    elif item == "checkout":
        T = False
        for i, x in enumerate(Cart, start = 1): #i and x are not special variables, but they are used to count
            print(f"{i}. {x}   {Cart[x]}")
        print(f"Your total is:      {sum(Cart.values())}")

    else:
        print("Sorry, we don't have that item in stock right now.")
