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

def typing_animation():
    print(i, end="",flush=True)
    time.sleep(0.03)

def distance_roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

def zero_money():
    user_broke = ("Sorry but you spent all your money already. You're a farmer though so I don't blame you. ")
    user_broke_1 = ("You run a carpentry business. How you are not financially literate. How are you already broke.")
    user_broke_2 = ("You're literally a banker. There is no way you spent all your money already. GG go next.")
    if starting_location == ("Nashville, Tennesee"):
        for i in str(user_broke):
            typing_animation()
    if starting_location == ("Champaign, Illinios"):
        for i in str(user_broke_1):
            typing_animation()
    if starting_location == ("New York, New York"):
        for i in str(user_broke_2):
            typing_animation()

# player info
name = input("What is your name?: ")
wife = input("What is your wifes name?: ")
son = input("What is your sons name?: ")
daughter = input("What is your daughters name?: ")
welcome = (f"Welcome {name} to the Oregon Trail")

intro1 = ("\nOut here in the east, its tough for you and your family. But rumor has it that theres GOLD out west. Across the country...\n\nYou realize that theres nothing here for your family so you want to set off to the west in search of gold. This is the start of your journey...\n")

# game info 
money = 0
score = 0
current_month = 0
distance = 0

# items
oxen_count = 0
lb_food = 0 
clothing = 0
ammunition = 0
spare_parts = 0

for i in str(welcome):
    typing_animation()
for i in str(intro1):
    typing_animation()

# Choose Difficulty (what your backstory is)
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
                 typing_animation()
            break
        if difficulty == 2:
            score = score + 10
            money = 1500
            starting_location = ("Champaign, Illinios")
            distance = 2130
            diff_ch2 = ("You chose Carpenter. You have been running a semi-successful wooding cutting business but everyone has been moving out west so business lately has been pretty slow. You've racked up some savings that you now will use on the trip.\n")
            for i in str(diff_ch2):
                typing_animation()
            break
        if difficulty == 3:
            score = score + 5
            money = 2000
            starting_location = ("New York, New York")
            distance = 2441 
            diff_ch3 = ("You chose Banker. You have been a very successful business man but you want to be set free. Everyday feels that same in your gloomy town that is New York. You want adventure. Your wife's been nagging you about moving so you finally cave and take the bait of the recent news you heard about there being gold in the west. You always wanted to be even more rich so this is an opportunity that you cannot miss. You have a lot of saving and you are ready to go.\n")
            for i in str(diff_ch3):
                typing_animation()
            break
        if difficulty == 4:
            diff_ch4 = ("This choice may change how you play the game. Think carefully.\n - The Banker starts out with the most most amount of money but its harder to get points. \n - The Farmer starts out with the least amount of points but is able to get points the easiest. \n - The Carpenter is someone inbetween.\n")
            for i in str(diff_ch4):
                 typing_animation()
    else:
        print("\nInvalid. Please input one of the choices...\n")

intro2 = (f"\nYou have ${money}\n")

for i in str(intro2):
    typing_animation()

beginning_location_dia1 = (f"\nIt is 1848. You are leaving from {starting_location} which is {distance} mi away from your final destination. You got a lot of ground to cover!")
for i in str(beginning_location_dia1):
    typing_animation()

# Choose Month 
while True:
    beginning_location_dia2 = input("\nYou must choose what month that you want to leave:\n1. March\n2. April\n3. May\n4. June\n5. July\n6. Ask for Advice\nWhat is your choice?: ")
    if beginning_location_dia2.isdigit():
        beginning_location_dia2 = int(beginning_location_dia2)
        if beginning_location_dia2 == 1:
            score = score + 10
            current_month = 3
            month_1 = ("You chose March. You must hate winter.")
            for i in str(month_1):
                typing_animation()
            break
        if beginning_location_dia2 == 2:
            score = score + 7
            current_month = 4
            month_2 = ("You chose April. Pretty early.")
            for i in str(month_2):
                typing_animation()
            break
        if beginning_location_dia2 == 3:
            score = score + 5
            current_month = 5
            month_3 = ("You chose May. Really good choice")
            for i in str(month_3):
                typing_animation()
            break
        if beginning_location_dia2 == 4:
            score = score + 7
            current_month = 6
            month_4 = ("You chose June. Ok choice.")
            for i in str(month_4):
                typing_animation()
            break
        if beginning_location_dia2 == 5:
            score = score + 10
            current_month = 7
            month_5 = ("You chose July. Kind of late don't you think?")
            for i in str(month_5):
                typing_animation()
            break
        if beginning_location_dia2 == 6:
            tavern_meeting_dia = ('\nYou attend a public meeting held for "folks with the --Gold Rush--", Youre told:\n"If you leave too early, there wont be any grass for your oxen to graze on. If you leave too late, you may not to Oregon before winter comes. If you leave at the right time, there will be enough grass and the weather will still be cool."\n')
            for i in str(tavern_meeting_dia):
                typing_animation()
    else:
        print("\nMake sure to input a number!\n")

month = current_month
if month == 3:
    month = "March"
if month == 4:
    month = "April"
if month == 5:
    month = "May"
if month == 6:
    month = "June"
if month == 7:
    month = "July"

func_ask_for_score()

intro3 = ("You still got a bit of time before you leave. Head to the shop and grab what you think you'll need on the trip.\n")
for i in str(intro3):
    typing_animation()

# Shop
shop1_dia1 = ("\nWelcome to the shop...\nYou were graciously given a wagon by the townsfolks. This is where you will take the money you saved up and buy all the supplies that you need.\n")
for i in str(shop1_dia1):
    typing_animation()

shop1_dia2 = ("\nThe shop keep tells you that you don't have to spend all your money now. You are able to buy, Oxen, Food, Sets of Clothing, Ammunition, and Spare Wagon Parts. Make to to buy what you need. Not any more, not any less.\n")
for i in str(shop1_dia2):
    typing_animation()

# Oxen
while True:
    shop1_dia3 = input("\nHow many oxen do you want to purchase? Each is $100 (You must buy at least two): ")
    if shop1_dia3.isdigit():
        shop1_dia3 = int(shop1_dia3)
        if shop1_dia3 <= 1:
            oxen_dia1 = ("\nPlease purchase at least two oxen.\n")
            typing_animation()
        if 2 <= shop1_dia3 < 11:
            confirm_1 = (f"\nYou have purchased {shop1_dia3} oxen.\n")
            oxen_count = shop1_dia3 + oxen_count
            money = money - (100 * oxen_count)
            if money < 0:
                money = 0
            print(f"\nYou have ${money} left with {oxen_count} oxen to your name.\n")
            confirmation = input("\nWould you like to buy more oxen? (y/n): ")
            print(confirmation)
            if confirmation == "y":
                confirmation = True
            if confirmation == "n":
                confirmation = False
            if confirmation == False:
                break
        if shop1_dia3 > 11:
            print("The shopkeep says he only has 10 oxen left avaliable for you to purchase.")
    else:
        print("\nMake sure to input a number!\n")

# Food
while True:
    if money == 0:
        zero_money()
        break
    shop1_dia4 = input("\nIt is $10 per lb. How many lb of food do you want to purchase?: ")
    if shop1_dia4.isdigit():
        shop1_dia4 = int(shop1_dia4)
        if shop1_dia4 <= 1:
            food_dia1 = ("\nPlease purchase at least some food...\n")
            for i in str(food_dia1):
                typing_animation()
        if 2 <= shop1_dia4 <= 100:
            money = money - (shop1_dia4 * 10)
            lb_food = lb_food + shop1_dia4
            print (f"\nYou have purchased {shop1_dia4} lb of food with ${money} left.\n")
            confirmation = input("\nWould you like to buy more lb of food? (y/n): ")
            print(confirmation)
            if confirmation == "y":
                confirmation = True
            if confirmation == "n":
                confirmation = False
            if confirmation == False:
                break
        if shop1_dia4 > 100:
            print("\nThe shopkeep says he only has 100lb of food for sale.\n")
    else:
        print("\nMake sure to input a number!\n")

# Clothing
while True:
    if money == 0:
        zero_money()
        break
    shop1_dia5 = input("\n It is $20 per set of clothing. How many sets of clothes do you want to buy? (You must buy at least 2): ")
    if shop1_dia5.isdigit():
        shop1_dia5 = int(shop1_dia5)
        if shop1_dia5 <= 1:
            clothing_dia1 = ("\nPlease purchase the minimum of 2 sets. (You won't survive without them)")
            print(clothing_dia1)
        if 2 <= shop1_dia5 <= 10:
            clothing = clothing + shop1_dia5
            money = money - (shop1_dia5 * 20)
            if money < 0:
                money = 0
            print(f"\nYou have purchased {shop1_dia5} sets of clothing with ${money} left.\n")
            confirmation = input("\nWould you like to buy more sets of clothing? (y/n): ")
            print(confirmation)
            if confirmation == "y":
                confirmation = True
            if confirmation == "n":
                confirmation = False
            if confirmation == False:
                break
    else:
        print("\nMake sure to input a number!\n")

# Ammo
while True:
    if money == 0:
        zero_money()
        break
    shop1_dia6 = input("\nIt is $1 per piece of Ammunition. How much Ammunition do you want to buy?: ")
    if shop1_dia6.isdigit():
        shop1_dia6 = int(shop1_dia6)
        if shop1_dia6 <= 1:
            ammo_dia1 = ("\nPlease purchase the minimum of 1 ammo. (You won't survive without it)")
            print(ammo_dia1)
        if 2 <= shop1_dia6 <= 500:
            ammunition = ammunition + shop1_dia6
            money = money - (shop1_dia6 * 1)
            if money < 0:
                money = 0
            print(f"\nYou have purchased {shop1_dia6} bullets of ammunition with ${money} left.\n")
            confirmation = input("\nWould you like to buy more ammunition? (y/n): ")
            print(confirmation)
            if confirmation == "y":
                confirmation = True
            if confirmation == "n":
                confirmation = False
            if confirmation == False:
                break
            else:
                print("Please input 'y' or 'n'.")
    else:
        print("\nMake sure to input a number!\n")

# Spare Wagon Parts
while True:
    if money == 0:
        zero_money()
        break
    shop1_dia7 = input("\nIt is $250 per set of Spare Wagon Parts. How many sets do you want to buy?: ")
    if shop1_dia7.isdigit():
        shop1_dia7 = int(shop1_dia7)
        if shop1_dia7 == 0:
            spare_parts_dia1 = input("\nYou sure you don't want to purchase any? (y/n): ")
            print(spare_parts_dia1)
            if spare_parts_dia1 == "n":
                spare_parts_dia1 = True
            if spare_parts_dia1 == "y":
                spare_parts_dia1 = False
            if spare_parts_dia1 == False:
                break
            else:
                print("Please input 'y' or 'n'.")
        if  1 <= shop1_dia7 <= 4:
            spare_parts = spare_parts + shop1_dia7
            money = money - (shop1_dia7 * 250)
            if money < 0:
                money = 0
            print(f"\nYou have purchased {shop1_dia7} sets of Spare Wagon Parts with ${money} left.\n")
            confirmation = input("\nWould you like to buy more Spare Parts? (y/n): ")
            print(confirmation)
            if confirmation == "y":
                confirmation = True
            if confirmation == "n":
                confirmation = False
            if confirmation == False:
                break
            else:
                print("Please input 'y' or 'n'.")
        if shop1_dia7 > 4:
            shop1_dia7_a = ("The shope keep only has 4 sets of Spare Wagon Parts for sale. Please buy accordingly...")
            for i in str(shop1_dia7_a):
                typing_animation
    else:
        print("\nMake sure to input a number!\n")

if money == 0:
    zero_money()

# Final Summary
summary_dia1 = ("\nHere is a summary of your trip and everything that you purchased: \n")
for i in str(summary_dia1):
    typing_animation()

summary_dai2 = (f"\nYou are leaving in the month of {month}.\nYou have ${money} left over.\nYou have {oxen_count} oxen.\nYou have {lb_food} lb of food.\nYou have {clothing} sets of clothing for you and your family.\nYou have {ammunition} bullets of ammunition.\nYou have {spare_parts} sets of spare parts for your wagon.")
for i in str(summary_dai2):
    typing_animation()

# End Intro (fix)
while True:
    summary_dai3 = input("\nAre you ready to go? (y/n): ")
    print(summary_dai3)
    if summary_dai3 == "y":
        summary_ch1 = (f"Good. Your journey of {distance} grueling miles begins now...")
        for i in str(summary_ch1):
            typing_animation()
            break
    if summary_dai3 == "n":
        summary_ch2 = (f"Too bad, Your journey of {distance} grueling miles begins now...")
        for i in str(summary_ch2):
            typing_animation()
            break
    else:
        print("Please input either y/n...")







            

            














