import time
import random

# Player info
def main():
    player = {}
    name = input("What is your name?: ")
    wife = input("What is your wife's name?: ")
    son = input("What is your son's name?: ")
    daughter = input("What is your daughter's name?: ")

    player["name"] = name
    player["wife"] = wife
    player["son"] = son
    player["daughter"] = daughter

    # Game info 
    game_data = {
        "info": {
            "money": 0,
            "score": 0,
            "current_month": 0,
            "distance": 0,
            "starting_location": ""
        },
        "items": {
            "oxen_count": 0,
            "lb_food": 0,
            "clothing": 0,
            "ammunition": 0,
            "spare_parts": 0
        }
    }

    oxen_count = 0
    money = 0
    clothing = 0
    ammunition = 0
    spare_parts = 0

    def func_ask_for_score():
        ask_for_score = input("\nDo you want to see your current score? (y/n): ")
        while True:
            if ask_for_score == "y":
                score_index = f"\nYour choices have given you a difficulty score of {game_data['info']['score']}\n"
                print(score_index)
                break
            elif ask_for_score == "n":
                print("Okay!")
                break
            else:
                print("\nPlease input either 'y' or 'n'\n")
                ask_for_score = input("Do you want to see your current score? (y/n): ")

    def typing_animation(text):
        for i in text:
            print(i, end="", flush=True)
            time.sleep(0.03)

    def distance_roll():
        return random.randint(1, 6)

    def zero_money():
        messages = {
            "Nashville, Tennessee": "Sorry but you spent all your money already. You're a farmer though so I don't blame you.",
            "Champaign, Illinois": "You run a carpentry business. How are you not financially literate?",
            "New York, New York": "You're literally a banker. There is no way you spent all your money already. GG go next."
        }
        message = messages.get(game_data["info"]["starting_location"], "You're out of money!")
        typing_animation(message)

    welcome = f"Welcome {player['name']} to the Oregon Trail"

    intro1 = ("\nOut here in the east, it's tough for you and your family. But rumor has it that there's GOLD out west. Across the country...\n\n"
              "You realize that there's nothing here for your family, so you want to set off to the west in search of gold. This is the start of your journey...\n")

    typing_animation(welcome)
    typing_animation(intro1)

    # Choose Difficulty (what your backstory is)
    def backstory():
        while True:
            difficulty = input("\nChoose your background:\n1. Farmer from Tennessee.\n2. Carpenter from Illinois.\n3. Banker from New York.\n4. Find out the difference between each background.\nWhat is your choice?: ")
            if difficulty.isdigit():
                difficulty = int(difficulty)
                if difficulty == 1:
                    game_data["info"]["score"] += 15
                    game_data["info"]["money"] += 1000
                    game_data["info"]["starting_location"] = "Nashville, Tennessee"
                    game_data["info"]["distance"] = 2128
                    typing_animation("You chose Farmer...\n")
                    break
                elif difficulty == 2:
                    game_data["info"]["score"] += 10
                    game_data["info"]["money"] += 1500
                    game_data["info"]["starting_location"] = "Champaign, Illinois"
                    game_data["info"]["distance"] = 2130
                    typing_animation("You chose Carpenter...\n")
                    break
                elif difficulty == 3:
                    game_data["info"]["score"] += 5
                    game_data["info"]["money"] += 2000
                    game_data["info"]["starting_location"] = "New York, New York"
                    game_data["info"]["distance"] = 2441
                    typing_animation("You chose Banker...\n")
                    break
                elif difficulty == 4:
                    typing_animation("This choice may change how you play the game. Think carefully...\n")
            else:
                print("\nInvalid input. Please input one of the choices...\n")
    backstory()

    intro2 = f"\nYou have ${game_data["info"]["money"]} left.\n"
    typing_animation(intro2)

    beginning_location_dia1 = f"\nIt is 1848. You are leaving from {game_data["info"]["starting_location"]} which is {game_data["info"]["distance"]} mi away from your final destination."
    typing_animation(beginning_location_dia1)

    # Choose Month 
    def choose_month():
        while True:
            beginning_location_dia2 = input("\nChoose what month to leave:\n1. March\n2. April\n3. May\n4. June\n5. July\n6. Ask for Advice\nWhat is your choice?: ")
            if beginning_location_dia2.isdigit():
                beginning_location_dia2 = int(beginning_location_dia2)
                if beginning_location_dia2 in range(1, 6):
                    month_messages = {
                        1: ("You chose March. You must hate winter."),
                        2: ("You chose April. Pretty early."),
                        3: ("You chose May. Really good choice."),
                        4: ("You chose June. Ok choice."),
                        5: ("You chose July. Kind of late, don't you think?")
                    }
                    game_data["info"]["current_month"] = beginning_location_dia2 + 2  # Adding 2 since March is month 3
                    typing_animation(month_messages[beginning_location_dia2])
                    break
                elif beginning_location_dia2 == 6:
                    typing_animation("You receive advice about timing your trip...\n")
                    break
            else:
                print("\nMake sure to input a number!\n")
    choose_month()

    month = ""
    chosen_month = game_data["info"]["current_month"]
    if chosen_month == 3:
        month = "March"
    elif chosen_month == 4:
        month = "April"
    elif chosen_month == 5:
        month = "May"
    elif chosen_month == 6:
        month = "June"
    elif chosen_month == 7:
        month = "July"

    func_ask_for_score()

    intro3 = "You still have some time before you leave. Head to the shop and grab what you think you'll need for the trip.\n"
    typing_animation(intro3)

    # Shop
    def shop():
        print("\nWelcome to the shop...")
        print("You were graciously given a wagon by the townsfolk. This is where you will take the money you saved up and buy all the supplies that you need.\n")
        print("The shopkeeper tells you that you don't have to spend all your money now. You can buy Oxen, Food, Sets of Clothing, Ammunition, and Spare Wagon Parts. Make sure to buy what you need, not any more, not any less.\n")

        # Initialize counts for items
        oxen_count = 0
        lb_food = 0
        clothing_count = 0
        ammunition_count = 0
        spare_parts_count = 0

        # Helper function for checking money
        def check_money(cost):
            if game_data["info"]["money"] >= cost:
                return True
            else:
                print("\nYou don't have enough money for that!\n")
                return False

        # Oxen
        while True:
            shop1_dia3 = input("\nHow many oxen do you want to purchase? Each is $100 (You must buy at least two): ")
            if shop1_dia3.isdigit():
                shop1_dia3 = int(shop1_dia3)
                if shop1_dia3 < 2:
                    print("\nPlease purchase at least two oxen.\n")
                elif shop1_dia3 > 10:
                    print("The shopkeeper says he only has 10 oxen left available for you to purchase.")
                else:
                    cost = shop1_dia3 * 100
                    if check_money(cost):
                        oxen_count += shop1_dia3
                        game_data["info"]["money"] -= cost
                        print(f"\nYou have purchased {shop1_dia3} oxen. You now have {oxen_count} oxen and ${game_data['info']['money']} left.\n")
                    break
            else:
                print("\nMake sure to input a number!\n")

        # Food
        while True:
            shop1_dia4 = input("\nIt is $10 per lb. How many lbs of food do you want to purchase?: ")
            if shop1_dia4.isdigit():
                shop1_dia4 = int(shop1_dia4)
                if shop1_dia4 < 1:
                    print("\nPlease purchase at least some food...\n")
                elif shop1_dia4 > 100:
                    print("\nThe shopkeeper says he only has 100 lbs of food for sale.\n")
                else:
                    cost = shop1_dia4 * 10
                    if check_money(cost):
                        lb_food += shop1_dia4
                        game_data["info"]["money"] -= cost
                        print(f"\nYou have purchased {shop1_dia4} lbs of food. You now have {lb_food} lbs of food and ${game_data['info']['money']} left.\n")
                    break
            else:
                print("\nMake sure to input a number!\n")

        # Clothing
        while True:
            shop1_dia5 = input("\nIt is $20 per set of clothing. How many sets of clothes do you want to buy? (You must buy at least 2): ")
            if shop1_dia5.isdigit():
                shop1_dia5 = int(shop1_dia5)
                if shop1_dia5 < 2:
                    print("\nPlease purchase at least 2 sets. (You won't survive without them)\n")
                elif shop1_dia5 > 10:
                    print("\nThe shopkeeper says he only has 10 sets of clothing available.\n")
                else:
                    cost = shop1_dia5 * 20
                    if check_money(cost):
                        clothing_count += shop1_dia5
                        game_data["info"]["money"] -= cost
                        print(f"\nYou have purchased {shop1_dia5} sets of clothing. You now have {clothing_count} sets and ${game_data['info']['money']} left.\n")
                    break
            else:
                print("\nMake sure to input a number!\n")

        # Ammunition
        while True:
            shop1_dia6 = input("\nIt is $1 per piece of ammunition. How much ammunition do you want to buy?: ")
            if shop1_dia6.isdigit():
                shop1_dia6 = int(shop1_dia6)
                if shop1_dia6 < 1:
                    print("\nPlease purchase at least 1 piece of ammunition.\n")
                elif shop1_dia6 > 500:
                    print("\nThe shopkeeper says he only has 500 pieces of ammunition available.\n")
                else:
                    cost = shop1_dia6
                    if check_money(cost):
                        ammunition_count += shop1_dia6
                        game_data["info"]["money"] -= cost
                        print(f"\nYou have purchased {shop1_dia6} pieces of ammunition. You now have {ammunition_count} pieces and ${game_data['info']['money']} left.\n")
                    break
            else:
                print("\nMake sure to input a number!\n")

        # Spare Wagon Parts
        while True:
            shop1_dia7 = input("\nIt is $250 per set of spare wagon parts. How many sets do you want to buy?: ")
            if shop1_dia7.isdigit():
                shop1_dia7 = int(shop1_dia7)
                if shop1_dia7 < 0:
                    print("\nYou can't purchase a negative amount.\n")
                elif shop1_dia7 > 4:
                    print("\nThe shopkeeper says he only has 4 sets of spare parts available.\n")
                else:
                    cost = shop1_dia7 * 250
                    if check_money(cost):
                        spare_parts_count += shop1_dia7
                        game_data["info"]["money"] -= cost
                        print(f"\nYou have purchased {shop1_dia7} sets of spare wagon parts. You now have {spare_parts_count} sets and ${game_data['info']['money']} left.\n")
                    break
            else:
                print("\nMake sure to input a number!\n")

        # Update game data with purchased items
        game_data["items"]["oxen_count"] = oxen_count
        game_data["items"]["lb_food"] = lb_food
        game_data["items"]["clothing"] = clothing_count
        game_data["items"]["ammunition"] = ammunition_count
        game_data["items"]["spare_parts"] = spare_parts_count
    shop()

    def intro_summary():
        summary_dia1 = "\nHere is a summary of your trip and everything that you purchased: \n"
        typing_animation(summary_dia1) 
    
        summary_dia2 = (f"\nYou are leaving in the month of {month}.\n"
                        f"You have ${game_data['info']['money']} left over.\n"
                        f"You have {game_data['items']['oxen_count']} oxen.\n"
                        f"You have {game_data['items']['lb_food']} lbs of food.\n"
                        f"You have {game_data['items']['clothing']} sets of clothing for you and your family.\n"
                        f"You have {game_data['items']['ammunition']} bullets of ammunition.\n"
                        f"You have {game_data['items']['spare_parts']} sets of spare parts for your wagon.")
        typing_animation(summary_dia2)

        # End Intro
        while True:
            summary_dai3 = input("\nAre you ready to go? (y/n): ")
            if summary_dai3.lower() == "y":
                summary_ch1 = (f"\nGood. Your journey of {game_data['info']['distance']} grueling miles begins now...\n")
                typing_animation(summary_ch1)
                break
            elif summary_dai3.lower() == "n":
                summary_ch2 = (f"\nToo bad, your journey of {game_data['info']['distance']} grueling miles begins now...\n")
                typing_animation(summary_ch2)
                break
            else:
                print("\nPlease input either y or n...\n")
    intro_summary()


if __name__ == "__main__":
    main()
