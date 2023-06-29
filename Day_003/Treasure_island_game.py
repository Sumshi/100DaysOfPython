#!/usr/bin/python3

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to treasure Island!")
print("Your mission is to find the tresure, (or die haha)")
choice1 = input('You\'ve come to a crossroad and a decision must be made. Which road will you pick? Type "left" for left or "right" for right\n').lower()

if choice1 == "left":
  choice2 = input('You are now at a lake but you need to get to the Island in the middle of the lake. Type "swim" to swim across or type "wait" to wait for the boat.\n').lower()
  if choice2 == "wait":
        choice3 = input('You have arrived at the island unharmed. There is a house with 3 doors, one red, one yellow and one blue. you must choose one. What is your choice?\n').lower()
        if choice3 == "red":
            print("The fire got you and now you are dead. Game over")
        elif choice3 == "yellow":
            print("Congratulations! You are the best of the best! The treasure is yours.")
        elif choice3 == "blue":
            print("the water people have you now. Game over")
        else:
            print("lol, you chose a door that doesn\'t exist. we don\'t do that here. Game over")
  else:
        print("You got attacked by hungry hippos and now you are dead. you should have waited. Game over.")
else:
    print("Oops! You fell into a hole and now you are dead!") 
