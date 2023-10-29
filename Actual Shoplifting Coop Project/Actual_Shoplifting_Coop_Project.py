import random
import time
customer = random.randint(1,3)
score = 0
end = False
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
            end = True
        elif choice == 2:
            score +=5
            print("you and your colleague manage to apprehend the shoplifter and call the police")
            time.sleep(1)
            print("however this was a dangerous move and could have risked injury")
            time.sleep(1)
            print("remember that intervening can lead to injury and you should intervene as non-violently as possible to avoid this")
            time.sleep(1)
            print("your score is ",score)
            end= True
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
            end = True
    elif choice == 2:
        score +=5
        print("they put down the item they are holding and attempt to leave without reaching the till. they may have put items in their bag beforehand.")
        time.sleep(1)
        print("you can 1) go up and confront them 2) ask them if they have forgotten to come to the till 3) watch them as they leave ")
        choice = int(input("choose the number that corresponds with your choice "))
        if choice == 1:
            print("the customer starts to becomes violent.")
            time.sleep(1)
            print("You can: 1) intervene yourself 2) ask a colleague to intervene and call the police 3) attempt to call the police yourself")
            time.sleep(1)
            choice1 = int(input("choose the number that corresponds with your choice: "))
            if choice1 == 1:
             score-=10
             print("you obtain a serious injury.")
             time.sleep(1)
             print("you endangered yourself by intervening without backup when you knew the person was violent.")
             time.sleep(1)
             print("this is a bad idea instead try to call for backup with colleagues.")
             time.sleep(1)
             print("your score is ",score)
             end= True
            elif choice1 == 2:
              score +=5
              print("you and your colleague manage to apprehend the shoplifter and call the police")
              time.sleep(1)
              print("however this was a dangerous move and could have risked injury")
              time.sleep(1)
              print("remember that intervening can lead to injury and you should intervene as non-violently as possible to avoid this")
              time.sleep(1)
              print("your score is ",score)
              end= True
            elif choice1 == 3:
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
             end= True
            elif choice == 2:
               score+=5
               print("they approach the till and unwillingly pay for their items. ")
               time.sleep(1)
               print("you avoided violent confrontation but there was a way to stop the possible conflict before it happened.")
               time.sleep(1)
               print("by using non-violent confrontation you may lessen the risk of shoplifters becoming violent and reduce halm to yourself. ")
               time.sleep(1)
               print("your score is ",score)
               end= True
            elif choice==3:
               score-=5
               print("the customer leaves with the shop's stolen possessions.")
               time.sleep(1)
               print("there were possible ways to avoid this by non-violent confrontation however you have avoided all risks physical harm here.")
               time.sleep(1)
               print("your score is ",score)
               end= True
        elif choice ==3 :
           score+=10
           print("they put the items back on the shelf and leave.")
           time.sleep(1)
           print("this is the best choice in this scenario as you have kept yourself safe and prevented shoplifting from occuring.  ")
           time.sleep(1)
           print("your score is ",score)
           end= True       
            
# this is where you add next customer path with if statement 
if customer == 2:
    if choice == 1:
        score == 5
        print("The customer gets offended")
        time.sleep(1)
        print("As a result: 1) Briefly explain concerns/suspicions to customer 2)Apologise to customer")
        time.sleep(1)
        choice2 = int(input("choose the number that corresponds with your choice: "))
#this is where the customer paths end so that the final finishing statement can be printed
if end == True:
 print("remember there are many different reasons why a customer may act suspicious.")
 time.sleep(1)
 print("the right course of action always depends on the circumstances. ")
 time.sleep(1)
 print("if you try this simulation again you may find that your inital right actions may now be wrong for the situation.")
 time.sleep(1)
 print("however the basic principles always apply of trying to keep yourself and other people safe first. ")
