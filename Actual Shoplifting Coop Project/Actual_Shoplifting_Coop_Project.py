import random
import time
customer = random.randint(1,3)
print("You are an employee at Co-op. You see a customer wandering around the store picking up items for a long time with a big backpack. ")
time.sleep(1)
print("you can: 1) Go up and confront them 2) Watch them 3) ask them if they need any help")
time.sleep(1)
choice = int(input("choose the number that corresponds with your choice: "))
#customer types are as follows 1 is violent shoplifter 2 is normal person 3 is confused person
if customer == 1:
    if choice == 1:
        print("The customer becomes violent.")
# this is where you add next customer path with if statement 