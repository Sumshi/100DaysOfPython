#!/usr/bin/python3
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(images[your_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(images[computer_choice])

if your_choice >= 3 or your_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif your_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and your_choice == 2:
  print("You lose")
elif computer_choice > your_choice:
  print("You lose")
elif your_choice > computer_choice:
  print("You win!")
elif computer_choice == your_choice:
  print("It's a draw")
