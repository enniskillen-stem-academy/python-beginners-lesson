#!/usr/bin/env python3
"""
Guess the Number Game

Welcome to the Guess the Number Game! In this game, the computer will choose a random number between 1 and 100,
and you will try to guess it. The computer will provide hints (too high/too low) until you guess the correct number.

Instructions:
- Run this script.
- Follow the prompts and enter your guesses.
- Have fun!

For advanced students: Try modifying the game to limit the number of guesses or add a scoring system.
"""

import random

def main():
    print("Welcome to Guess the Number!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

if __name__ == '__main__':
    main()
