#!/usr/bin/python3
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissor.\n"))
computer_choice = random.randint(0, 2)
print(f"computer choice  is: {computer_choice}")
if user_choice >= 3 or user_choice < 0:
    print("you entered an invalid number")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
elif computer_choice > user_choice:
    print("you lose")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("it is a draw")
else:
    print("out of range number")
