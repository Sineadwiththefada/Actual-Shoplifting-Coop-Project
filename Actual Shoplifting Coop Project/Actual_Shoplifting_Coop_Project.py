import random
import time
score=0
while score < 10:
    score=0
    customer = random.randint(1,3)
    end = False
    print("this program will repeat until you pass (get a score of 10 or more) ")
    time.sleep(1)
    print("you are an employee at Co-op. you see a customer wandering around the store picking up items for a long time with a big backpack. ")
    time.sleep(1)
    print("you can:")
    time.sleep(1)
    print("1) go up and confront them")
    time.sleep(1)
    print("2) watch them")
    time.sleep(1)
    print("3) ask them if they need any help")
    time.sleep(1)
    choice = int(input("choose the number that corresponds with your choice: "))
    #customer types are as follows 1 is violent shoplifter 2 is normal person 3 is confused person
    if customer == 1:
        if choice == 1:
            score-=10
            print("the customer starts to become violent")
            time.sleep(1)
            print("you can:")
            time.sleep(1)
            print("1) intervene yourself")
            time.sleep(1)
            print("2) ask a colleague to intervene and call the police")
            time.sleep(1)
            print("3) attempt to call the police yourself")
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
            print("the shoplifter catches you off guard and you obtain an injury")
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
        print("you can: ")
        time.sleep(1)
        print("1) go up and confront them")
        time.sleep(1)
        print("2) ask them if they have forgotten to come to the till")
        time.sleep(1)
        print("3) watch them as they leave ")
        choice = int(input("choose the number that corresponds with your choice "))
        if choice == 1:
            print("the customer starts to becomes violent.")
            time.sleep(1)
            print("You can:")
            time.sleep(1)
            print("1) intervene yourself")
            time.sleep(1)
            print("2) ask a colleague to intervene and call the police")
            time.sleep(1)
            print("3) attempt to call the police yourself")
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
            
# 2nd customer path starts here 
    elif customer == 2:
        if choice == 1:
            score == 5
            print("The customer gets offended")
            time.sleep(1)
            print("As a result:")
            time.sleep
            print("1) Briefly explain concerns/suspicions to customer")
            time.sleep(1)
            print("2)Apologise to customer")
            time.sleep(1)
            choice2 = int(input("choose the number that corresponds with your choice: "))
        if choice2 == 1:
            score += 5
            print(" Customer gains an understanding ")
            time.sleep(1)
            print("You have reassured the customer")
            time.sleep(1)
            print("This was a good choice as they'll continue to buy from your shop!")
            time.sleep(1)
            print("your score is ",score)
            end = True
        elif choice2 == 2:
            print(" the customer appreciates your apology")
            time.sleep(1)
            print("you have calmed the customer down")
            time.sleep(1)
            print("this was a good choice because the customer will now happily buy what they need ")
            time.sleep(1)
            score += 5
            print("your score is ",score)
            end = True
               
     
    elif choice == 2:
         print(" the customer may start to feel uncomfortable")
         time.sleep(1)
         print("as a result, customer may leave the shop and not buy anything at all")
         time.sleep(1)
         print("the customer may make a complaint")
         time.sleep(1)
         print("this wasnt the best choice as it jeopardises yours and the shop's reputation")
         score +=5
         print("your score is ",score)
         end= True
         

    elif choice == 3:
        print("by asking if the customer needs assistance, they'll appreciate  the good customer service and leave a good review of the shop!")
        time.sleep(1)
        print("additionally, they may find more product to buy with your assistance")
        time.sleep(1)
        print("you've made the best choice!")
        score += 10
        print("your score is ",score)
        end = True
#3rd customer path starts here
    elif customer == 3:
        # if customer picks choice 1
        if choice == 1:
            score-=10
            print("the customer gets angry and leaves a bad review ")
            time.sleep(1)
            print("you upset an innocent customer that needed your help")
            time.sleep(1)
            print("instead of this you can ask if they need any help calmly")
            time.sleep(1)
            print("your score is ",score)
            end = True
        # if cutomer picks choice 2
        elif choice == 2:
            score +=5
            print("the customer struggles for a while and attempts to find that they want.")
            time.sleep(1)
            print("but fails and leave the shop unsatisfied")
            end= True
        elif choice == 3:
             score +=10
             print("this is the best option. Well done!")
             time.sleep(1)
             print("the customer leaves happy and gets what they want")
             end= True
#this is where the customer paths end so that the final finishing statement can be printed
    if end == True & score <10 :
        print("remember there are many different reasons why a customer may act suspicious.")
        time.sleep(1)
        print("the right course of action always depends on the circumstances. ")
        time.sleep(1)
        print("if you try this simulation again you may find that your inital right actions may now be wrong for the situation.")
        time.sleep(1)
        print("however the basic principles always apply of trying to keep yourself and other people safe first. ")
    elif end==True& score>=10:
            print("your score is good as you handled the customer well. Well done!")
            time.sleep(1)
            print("however always remember that there are many different reasons why a customer may act suspicious.")
            time.sleep(1)
            print("the right course of action always depends on the circumstances. ")
            time.sleep(1)
            print("if you try this simulation again you may find that your inital right actions may now be wrong for the situation.")
            time.sleep(1)
            print("however the basic principles always apply of trying to keep yourself and other people safe first. ")
    
