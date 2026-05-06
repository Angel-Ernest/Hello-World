import time

mylist = ["Do work", "Clean my room", "Eat something"]
completelist = []

print("Welcome to your To Do List!")
time.sleep(0.3)

print("Options\n1. Add a task\n2. Remove a task\n3. Complete a task\n4. Display tasks\n5. Exit")
time.sleep(0.5)

while True:
  A1 = input("Choose an option: ")

  if A1 == "4":
     for i, x in enumerate(mylist, start=1):
       if x in completelist:
         print(f"{i}. [X] {x}")
       else:
         print(f"{i}. [ ] {x}")
  elif A1 == "1":
    NW = input("Add a task: ")
    mylist.append(NW)
  elif A1 == "2":
    RW = int(input("Enter the number of the task to remove: ")) - 1
    if 0 <= RW < len(mylist): 
      mylist.pop(RW)
  elif A1 == "5":
    print("Goodbye")
    time.sleep(1)
    break
  elif A1 == "3":
    print("Your to do list:")
    for i, x in enumerate(mylist, start=1):
     if x in completelist:
        print(f"{i}. [X] {x}")
     else:
       print(f"{i}. [ ] {x}")
    QW = int(input("Enter the number of the task you'd like to complete: ")) - 1
    if 0 <= QW < len(mylist):
      completelist.append(mylist[QW])

  else:
    print("Invalid task number.")
     
     
 