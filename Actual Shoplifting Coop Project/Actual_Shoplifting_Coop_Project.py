import random
import time
customer = random.randint(1,3)
score = 0
print("You are an employee at Co-op. You see a customer wandering around the store picking up items for a long time with a big backpack. ")
time.sleep(1)
print("you can: 1) Go up and confront them 2) Watch them 3) ask them if they need any help")
time.sleep(1)
choice = int(input("choose the number that corresponds with your choice: "))
#customer types are as follows 1 is violent shoplifter 2 is normal person 3 is confused person
if customer == 1:
    if choice == 1:
        score-=10
        print("The customer starts to become violent")
        time.sleep(1)
        print("You can: 1) intervene yourself 2) ask a colleague to intervene and call the police 3) attempt to call the police yourself")
        time.sleep(1)
        choice = int(input("choose the number that corresponds with your choice: "))
        if choice == 1:
            score-=10
            print("you obtain a serious injury.")
            time.sleep(1)
            print("you endangered yourself by intervening without backup when you knew the person was violent.")
            time.sleep(1)
            print("this is a bad idea instead try to call for backup with colleagues.")
            time.sleep(1)
            print("your score is ",score)
        elif choice == 2:
            score +=5
            print("you and your colleague manage to apprehend the shoplifter and call the police")
            time.sleep(1)
            print("however this was a dangerous move and could have risked injury")
            time.sleep(1)
            print("remember that intervening can lead to injury and you should intervene as non-violently as possible to avoid this")
            time.sleep(1)
            print("your score is ",score)
        elif choice == 3:
            score-=10
            print("you obtain an injury as the shoplifter gets you off guard.")
            time.sleep(1)
            print("you endangered yourself by trying to get backup when you knew the person was violent.")
            time.sleep(1)
            print("remember that getting immediate backup from colleagues is important and ensures your safety first.")
            time.sleep(1)
            print("you should remember to also intervene as non-violently as possible to avoid violent confrontations. ")
            time.sleep(1)
            print("your score is ",score)
    elif choice == 2:
        score +=5
        print("they put down the item they are holding and attempt to leave without reaching the till. they may have put items in their bag beforehand.")
        time.sleep(1)
        print("you can 1) go up and confront them 2) ask them if they have forgotten to come to the till 3) watch them as they leave ")
        choice = int(input("choose the number that corresponds with your choice "))
        if choice == 1:
            print("choice 1")
        
            
# this is where you add next customer path with if statement 
