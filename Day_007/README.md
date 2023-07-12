		Today i will do the hangman game
	This game uses my knowledge on strings, modules, if statements and loops

 

<img width="588" alt="Solution+-+Hangman+Flowchart+1" src="https://github.com/Sumshi/100DaysOfPython/assets/109363465/70c7bb58-9f46-4f81-ad5f-bd899575b5fd">

#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
chosen_word = random.choice(word_list)
guess = input("guess a letter: ").lower()
if guess in  chosen_word:
  print(guess)
