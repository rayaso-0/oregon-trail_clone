import time
import random

def func_ask_for_score():
    ask_for_score = str(input("\nDo you want to see your current score? (y/n): "))
    while True:
        if ask_for_score == "y":
            score_index = (f"\nYou're choices have given you a difficulty score of {score}\n")
            print(score_index)
            break
        if ask_for_score == "n":
            print("Okay!")
            break
        else:
            print("\nPlease input either 'y' or 'n'\n")

welcome = ("Welcome to the Oregon Trail")
name = input("What is your name?: ")
wife = input("What is your wifes name?: ")
son = input("What is your sons name?: ")
daughter = input("What is your daughters name?: ")


intro1 = ("\nOut here in the east, its tough for you and your family. But rumor has it that theres GOLD out west. Across the country...\n\nYou realize that theres nothing here for your family so you want to set off to the west in search of gold. This is the start of your journey...\n")

# game info 
money = 0
score = 0
current_month = 0

# items
oxen_count = 0
lb_food = 0 
clothing = 0
ammunition = 0
spare_parts = 0

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
            score = score + 15
            money = 1000
            starting_location = ("Nashville, Tennesee")
            distance = 2128
            diff_ch1 = ("You chose Farmer. You and your family have been farming for years now but recent back to back droughts have made your profits dwindle every year. You plan on taking all your savings and invest into this trip...\n")
            for i in str(diff_ch1):
                 print(i, end="", flush=True)
                 time.sleep(0.03)
            break
        if difficulty == 2:
            score = score + 10
            money = 1500
            starting_location = ("Champaign, Illinios")
            distance = 2130
            diff_ch2 = ("You chose Carpenter. You have been running a semi-successful wooding cutting business but everyone has been moving out west so business lately has been pretty slow. You've racked up some savings that you now will use on the trip.\n")
            for i in str(diff_ch2):
                print(i, end="", flush=True)
                time.sleep(0.03)
            break
        if difficulty == 3:
            score = score + 5
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

while True:
    beginning_location_dia2 = input("\nYou must choose what month that you want to leave:\n1. March\n2. April\n3. May\n4. June\n5. July\n6. Ask for Advice\nWhat is your choice?: ")
    if beginning_location_dia2.isdigit():
        beginning_location_dia2 = int(beginning_location_dia2)
        if beginning_location_dia2 == 1:
            score = score + 10
            current_month = 3
            month_1 = ("You chose March. You must hate winter.")
            for i in str(month_1):
                print(i, end="", flush=True)
                time.sleep(0.03)
            break
        if beginning_location_dia2 == 2:
            score = score + 7
            current_month = 4
            month_2 = ("You chose April. Pretty early.")
            for i in str(month_2):
                print(i, end="", flush=True)
                time.sleep(0.03)
            break
        if beginning_location_dia2 == 3:
            score = score + 5
            current_month = 5
            month_3 = ("You chose May. Really good choice")
            for i in str(month_3):
                print(i, end="", flush=True)
                time.sleep(0.03)
            break
        if beginning_location_dia2 == 4:
            score = score + 7
            current_month = 6
            month_4 = ("You chose June. Ok choice.")
            for i in str(month_4):
                print(i, end="", flush=True)
                time.sleep(0.03)
            break
        if beginning_location_dia2 == 5:
            score = score + 10
            current_month = 7
            month_5 = ("You chose July. Kind of late don't you think?")
            for i in str(month_5):
                print(i, end="", flush=True)
                time.sleep(0.03)
            break
        if beginning_location_dia2 == 6:
            tavern_meeting_dia = ('\nYou attend a public meeting held for "folks with the --Gold Rush--", Youre told:\n"If you leave too early, there wont be any grass for your oxen to graze on. If you leave too late, you may not to Oregon before winter comes. If you leave at the right time, there will be enough grass and the weather will still be cool."\n')
            for i in str(tavern_meeting_dia):
                print(i, end="", flush=True)
                time.sleep(0.03)
    else:
        print("\nMake sure to input a number!\n")


func_ask_for_score()

intro3 = ("You still got a bit of time before you leave. Head to the shop and grab what you think you'll need on the trip. ")
for i in str(intro3):
    print(i, end="", flush=True)
    time.sleep(0.03)


# finish shop
shop1_dia1 = ("\nWelcome to the shop...\nYou were graciously given a wagon by the townsfolks. This is where you will take the money you saved up and buy all the supplies that you need.\n")
for i in str(shop1_dia1):
    print(i, end="", flush=True)
    time.sleep(0.03)

shop1_dia2 = ("\nThe shop keep tells you that you don't have to spend all your money now. You are able to buy, Oxen, Food, Clothing, Ammunition, and Spare Wagon Parts. Make to to buy what you need. Not any more, not any less.\n")
for i in str(shop1_dia2):
    print(i, end="", flush=True)
    time.sleep(0.03)

while True:
    shop1_dia3 = input("\n1. How many oxen do you want to purchase? Each is $100 (You must buy at least two)\n")
    if shop1_dia3.isdigit():
        shop1_dia3 = int(shop1_dia3)
        if shop1_dia3 <= 1:
            oxen_dia1 = ("Please purchase at least two oxen.")
            for i in str(oxen_dia1):
                print(i, end="", flush=True)
                time.sleep(0.03)
        if 2 <= shop1_dia3 < 11:
            confirm_1 = input(f"You have purchased {shop1_dia3} oxen.")
            oxen_count = shop1_dia3 + oxen_count
            money = money - (100 * oxen_count)
            print(f"You have {money} left with {oxen_count} oxen to your name. ")
            break
        if shop1_dia3 > 11:
            print("The shopkeep says he only has 10 oxen left avaliable for you to purchase.")
    else:
        confirm_2 = ("Please input a number")

while True:
    shop1_dia4 = input("\n1. How many lb of food do you want to purchase? Each is $2 (You must buy at least two)\n")
    if shop1_dia4.isdigit():
        shop1_dia4 = int(shop1_dia4)
        if shop1_dia4 <= 1:
            food_dia1 = ("\nPlease purchase at least two oxen.\n")
            for i in str(food_dia1):
                print(i, end="", flush=True)
                time.sleep(0.03)
        if 2 <= shop1_dia4 < 7:
            confirm_1a = input(f"\nYou have purchased {shop1_dia4} oxen.\n")
            break
        if shop1_dia4 > 7:
            print("\nThe shopkeep says he only has 6 oxen left avaliable.\n")
    else:
        confirm_2a = ("\nPlease input a number\n")





