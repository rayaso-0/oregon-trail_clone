# My try at creating a "The Oregon Traill" game clone in python
# Possible future project to create this into an actual application/mobile app 
# Date: Wed Sep 11 2024
import time
import random


welcome = ("Welcome to the Oregon Trail")
name = input("What is your name?: ")
wife = input("What is your wifes name?: ")
son = input("What is your sons name?: ")
daughter = input("What is your daughters name?: ")


rules = ('\n"Out here, its tough for you and your family. But rumor has it that theres GOLD out west. Across the country..."\nYou realize that theres nothing here for your family here so you want to set off to the west in search of gold."\n')

for i in str(welcome):
    print(i, end="", flush=True)
    time.sleep(0.1)

for i in str(rules):
    print(i, end="", flush=True)
    time.sleep(0.1)




