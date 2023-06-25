#!/usr/bin/python3
import random

def play_game():
    secret_number = random.randint(1, 10)
    guess_limit = 3
    num_guesses = 0
    guessed_nums = []  # stores the guessed numbers
    while num_guesses < guess_limit:
        guess_value = int(input("Guess a number between 1 and 10: "))
        try:
            if guess_value < 1 or guess_value > 10:
                print("Invalid input. Number must be between 1 and 10.")
                continue
            elif guess_value in guessed_nums:
                print("You already guessed that number. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue        
        # Add guessed number to list and increment counter
        guessed_nums.append(guess_value)
        num_guesses = num_guesses + 1
        if guess_value == secret_number:
            print("Congratulations! You guessed the secret number!")
            return True
        elif num_guesses < guess_limit:
            if guess_value < secret_number:
                print("The secret number is higher than your guess.")
            else:
                print("The secret number is lower than your guess.")
    print(f"Sorry, you did not find the secret number ({secret_number}). Better luck next time!")
    return False
play_again = True  # Play game loop until user chooses to stop playing
while play_again:
    play_game()
    play_again_str = input("Do you want to play again? (y/n): ")
    play_again = (play_again_str.lower() == "y")
print("Thanks for playing!")
