import time
import random
import os

money = 100
health = 100

inventory = (f"money:{money}-health:{health}")

input(f"this is your inventory {inventory} press enter to continue:   ")

print("level 1 (1-2) level 2 (1-5)  level (1-10)")

level = input("select a level: ")

if level == "1":
    while True:
        os.system('cls')
        

        print(f"money-{money}  health-{health}")

        level_1 = random.randint(1, 2)

        bet_1 = int(input("select how much money you want to bet"))

        if bet_1 > money:
            print("you dont have enough money")

            time.sleep(2)
        else:

            answer_1 = int(input("choose a number between 1-2:  "))
        
            if answer_1 == level_1:

                bet_1 *= 2

                money += bet_1    
                print("nice you won")
                print(f"the number was {level_1}")
            else:

                money -= bet_1   
                print("you lost hahahahaah")
                print(f"the number was {level_1}")     
        
            time.sleep(1) 
            

if level == "2":
    while True:
        os.system('cls')
        

        print(f"money-{money}  health-{health}")

        level_2 = random.randint(1, 5)

        bet_2 = int(input("select how much money you want to bet"))

        if bet_2 > money:
            print("you dont have enough money")

            time.sleep(2)
        else:

            answer_2 = int(input("choose a number between 1-5:  "))
        
            if answer_2 == level_2:

                bet_2 *= 5

                money += bet_2    
                print("nice you won")
                print(f"the number was {level_2}")
            else:

                money -= bet_2   
                print("you lost hahahahaah")
                print(f"the number was {level_2}")     
        
            time.sleep(1) 

if level == "3":
    while True:
        os.system('cls')
        

        print(f"money-{money}  health-{health}")

        level_3 = random.randint(1, 10)

        bet_3 = int(input("select how much money you want to bet"))

        if bet_3 > money:
            print("you dont have enough money")

            time.sleep(2)
        else:

            answer_3 = int(input("choose a number between 1-10:  "))
        
            if answer_3 == level_3:

                bet_3 *= 10

                money += bet_3    
                print("nice you won")
                print(f"the number was {level_3}")
            else:

                money -= bet_3   
                print("you lost hahahahaah")
                print(f"the number was {level_3}")     
        
            time.sleep(1) 







