#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
def game():
  if difficulty == "easy":
    lives = 10
    while lives > 0:
      print(f"You have {lives} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if guess > number:
        print("Too high.")
        print("Guess again.")
        lives += -1
      elif guess < number:
        print("Too low.")
        print("Guess again.")
        lives += -1
      elif guess == number:
        print("You've guessed the correct number, you win!")
        return
      else:
        lives += -1
  else:
    lives = 5
    while lives > 0:
      print(f"You have {lives} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if guess > number:
        print("Too high.")
        print("Guess again.")
        lives += -1
      elif guess < number:
        print("Too low.")
        print("Guess again.")
        lives += -1
      elif guess == number:
        print(f"You've guessed the correct number! The answer was {number}!")
        return
      else:
        lives += -1
    print("You have run out of lives, you lose.")

game()