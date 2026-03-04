import time

#The questions
print("Hello adventurer! I will be your guide in this adventure that you will experience. But first, let's do a few questions.")
name = input("What's your name? ")
print("Ok," , name)
fear = input("What do you fear? ")
print("That's very scary!")
hero = input("What's your favorite hero? ")
print("I also like",hero,"!")
country = input("Where are you from? ")
print("I would like to visit", country)
power = input("What power would you like to have? ")
print("Interesting!")
supername = input("And finally: if you were a superhero, what would bee your name? ")
print("Ok,", supername)
print("Now, let's make your story!")
time.sleep(1)
print("Creating story...")
time.sleep(3)
#The story
print("In" , country , "there was a kid called", name, ".", name , "feared" , fear , ". But one day he fought it and won.", hero , "appeared and reawarded", name, "with something incredible,", hero , "gifted", name , "a superpower! Out of nowhere," , name, "recieved the power of" , power , "! Since that day, he became", supername , "!")