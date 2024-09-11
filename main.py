import time
import random

welcome = ("Welcome to the Oregon Trail")
name = input("What is your name?: ")
wife = input("What is your wifes name?: ")
son = input("What is your sons name?: ")
daughter = input("What is your daughters name?: ")


intro1 = ("\nOut here, its tough for you and your family. But rumor has it that theres GOLD out west. Across the country...\n\nYou realize that theres nothing here for your family so you want to set off to the west in search of gold. This is the start of your 2000 mi journey...\n")
money = [0]
score = [0]

for i in str(welcome):
    print(i, end="", flush=True)
    time.sleep(0.1)
for i in str(intro1):
    print(i, end="", flush=True)
    time.sleep(0.1)

while True:
    difficulty = input("\nThis is where you can choose your background.\n1. Farmer from North Carolina.\n2. Carpenter from Illinois\n3. Banker from New York.\n4. Find out the difference between each background.\n")
    if difficulty.isdigit():
        difficulty = int(difficulty)
        if difficulty == 1:
            money[0] = 1000
            diff_ch1 = ("You chose Farmer. You and your family have been farming for years now but recent back to back droughts have made your profits dwindle every year. You plan on taking all your savings and invest into this trip...")
            for i in str(diff_ch1):
                 print(i, end="", flush=True)
                 time.sleep(0.1)
            break
        if difficulty == 2:
            money[0] = 1500
            diff_ch2 = ("You chose Carpenter. You have been running a semi-successful wooding cutting business but everyone has been moving out west so business lately has been pretty slow. You've racked up some savings that you now will use on the trip.")
            for i in str(diff_ch2):
                print(i, end="", flush=True)
                time.sleep(0.1)
            break
        if difficulty == 3:
            money[0] = 2000
            diff_ch3 = ("You chose Banker. You have been a very successful business man but you want to be set free. Everyday feels that same in your gloomy town that is New York. You want adventure. Your wife's been nagging you about moving so you finally cave and take the bait of the recent news you heard about there being gold in the west. You always wanted to be even more rich so this is an opportunity that you cannot miss. You have a lot of saving and you are ready to go.")
            for i in str(diff_ch3):
                print(i, end="", flush=True)
                time.sleep(0.1)
        if difficulty == 4:
            diff_ch4 = ("This choice may change how you play the game. Think carefully.\nThe banker starts out with the most most amount of money but its harder to get points. \nThe farmer starts out with the least amount of points but is able to get points the easiest. \nThe Carpenter is someone inbetween.")
            for i in str(diff_ch4):
                 print(i, end="", flush=True)
                 time.sleep(0.1)
    else:
        print("Please input one of the choices...")
    

# add money variable
intro2 = ("\nYou have", money, "to your name. Choose everything carefully that you will buy for this long, grueling, trip...\n")

for i in str(intro2):
    print(i, end="", flush=True)
    time.sleep(0.1)


while True:
    choice1 = input("Choose the number of oxen you want to bring (Choose at least 2): ")
    if choice1.isdigit():
        choice1 = int(choice1)
        if 2 <= choice1 <7:
                    break
        else:
            print("Why would you even need this many oxen???")
    else:
        print("Input a number please.")




