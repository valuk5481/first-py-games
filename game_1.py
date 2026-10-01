import keyboard
import time
import os
import random



money = 100
health = 100

inventory = (f"health:{health}  money:{money}")

print("A SIMPLE NUMBER GAME PRESS S TO START    q to quit")

key = keyboard.read_key()

if key == "s":
    
    while True:

        os.system('cls')

        print(f"{inventory}")
        print("this is your inventory keep it safe press c to continue")



        time.sleep(1)

        key = keyboard.read_key()

        if key == "c":

            while True:

                os.system('cls')

                print("Pick a level")
                print("LEVEL 1 (1-10)")
                print("LEVEL 2 (1-20)")
                print("LEVEL 3 (1-30)")

                key = keyboard.read_key()

                if key == "1":
                    while True:

                        os.system('cls')

                        level_1 = random.randint(1, 10)
                        

                        answer_1 = int(input("pick a number between 1-10:    "))

                        if answer_1 == level_1:
                            print("you won nice")
                        else:
                            print(f"you lost the answer was {level_1}")
                time.sleep(1)

                                