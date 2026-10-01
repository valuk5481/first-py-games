import keyboard
import time
import os

gold = 50
money = 50
health = 100


while True:

    os.system('cls')

    my_inventory =(f"gold = {gold} money = {money} health = {health}")

    print("=======INVENTORY GAME=======")
    print(f"your inventory {my_inventory}")
    print("PRESS (g) to add gold-----PRESS (m) to add money------PRESS (h) to add health all +15______PRESS (q) to quit")
    print("waiting for input......")

    key = keyboard.read_key()

    if key == "g":
        gold += 1
    elif key == "m":
        money += 1
    elif key == "h":
        health += 1
    elif key == "q":
        break                   



        

  