import time
import random

welcome = ("Welcome to the Oregon Trail")
name = input("What is your name?: ")
wife = input("What is your wifes name?: ")
son = input("What is your sons name?: ")
daughter = input("What is your daughters name?: ")


intro1 = ("\nOut here, its tough for you and your family. But rumor has it that theres GOLD out west. Across the country...\n\nYou realize that theres nothing here for your family so you want to set off to the west in search of gold. This is the start of your journey...\n")
money = 0
score = [0]

for i in str(welcome):
    print(i, end="", flush=True)
    time.sleep(0.03)
for i in str(intro1):
    print(i, end="", flush=True)
    time.sleep(0.03)

while True:
    difficulty = input("\nThis is where you can choose your background.\n1. Farmer from Tennesee.\n2. Carpenter from Illinois.\n3. Banker from New York.\n4. Find out the difference between each background.\nWhat is your choice?: ")
    if difficulty.isdigit():
        difficulty = int(difficulty)
        if difficulty == 1:
            money = 1000
            starting_location = ("Nashville, Tennesee")
            distance = 2128
            diff_ch1 = ("You chose Farmer. You and your family have been farming for years now but recent back to back droughts have made your profits dwindle every year. You plan on taking all your savings and invest into this trip...\n")
            for i in str(diff_ch1):
                 print(i, end="", flush=True)
                 time.sleep(0.03)
            break
        if difficulty == 2:
            money = 1500
            starting_location = ("Champaign, Illinios")
            distance = 2130
            diff_ch2 = ("You chose Carpenter. You have been running a semi-successful wooding cutting business but everyone has been moving out west so business lately has been pretty slow. You've racked up some savings that you now will use on the trip.\n")
            for i in str(diff_ch2):
                print(i, end="", flush=True)
                time.sleep(0.03)
            break
        if difficulty == 3:
            money = 2000
            starting_location = ("New York, New York")
            distance = 2441 
            diff_ch3 = ("You chose Banker. You have been a very successful business man but you want to be set free. Everyday feels that same in your gloomy town that is New York. You want adventure. Your wife's been nagging you about moving so you finally cave and take the bait of the recent news you heard about there being gold in the west. You always wanted to be even more rich so this is an opportunity that you cannot miss. You have a lot of saving and you are ready to go.\n")
            for i in str(diff_ch3):
                print(i, end="", flush=True)
                time.sleep(0.03)
            break
        if difficulty == 4:
            diff_ch4 = ("This choice may change how you play the game. Think carefully.\nThe Banker starts out with the most most amount of money but its harder to get points. \nThe Farmer starts out with the least amount of points but is able to get points the easiest. \nThe Carpenter is someone inbetween.\n")
            for i in str(diff_ch4):
                 print(i, end="", flush=True)
                 time.sleep(0.03)
    else:
        print("\nPlease input one of the choices...\n")

intro2 = (f"\nYou have ${money}\n")
for i in str(intro2):
    print(i, end="", flush=True)
    time.sleep(0.03)

beginning_location_dia1 = (f"\nIt is 1848. You are leaving from {starting_location} which is {distance} mi away. You got a lot of ground to cover!")
for i in str(beginning_location_dia1):
    print(i, end="", flush=True)
    time.sleep(0.03)

# finish starting month
while True:
    beginning_location_dia2 = input("\nYou must choose what month that you want to leave:\n1. March\n2. April\n3. May\n4. June\n5. July\n6. Ask for Advice\nWhat is your choice?: ")
    if beginning_location_dia2.isdigit():
        beginning_location_dia2 = int(beginning_location_dia2)
        if beginning_location_dia2 == 1:
            break

# finish shop
shop1 = ("\nWelcome to the shop...\nYou were graciously given a wagon by the townsfolks. This is where you will take the money you saved up and buy all the supplies that you need.\n")
for i in str(shop1):
    print(i, end="", flush=True)
    time.sleep(0.03)

shop1_dia1 = ("\n!!! You must buy at least oxen and food !!!\n")
for i in str(shop1_dia1):
    print(i, end="", flush=True)
    time.sleep(0.03)

while True:
    shop1_dia2 = input("\n1. Oxen\n2. Food\n3. Extra Wagon Parts\n4. ")


while True:
    choice1 = input("\nChoose the number of oxen you want to bring (Choose at least 2): \n")
    if choice1.isdigit():
        choice1 = int(choice1)
        if 2 <= choice1 <7:
                    break
        else:
            print("\nWhy would you even need this many oxen??\n")
    else:
        print("Input a number please.")




