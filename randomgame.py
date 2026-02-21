"""
Random Number Guessing Game
A simple command-line game where the user guesses a number within a specified range.

Usage: 
python randomgame.py <start_number> <end_number>
"""

import sys
from random import randint

def run_game(start, end):
    """Runs the guessing game logic within the given bounds."""
    answer = randint(start, end)
    
    while True:
        try:
            # Dynamically use the start and end variables in the prompt
            guess = int(input(f"Guess a number between {start} and {end}: "))
            
            # Check if the guess is within the dynamic bounds
            if start <= guess <= end:
                if guess == answer:
                    print("You are the man!")
                    break
                else:
                    print("Not quite! Try again.")
            else:
                print(f"Pick a number between {start} and {end}!")
                
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == '__main__':
    # Check if the user provided the correct number of terminal arguments
    if len(sys.argv) != 3:
        print("Usage: python randomgame.py <start_number> <end_number>")
        print("Defaulting to a range of 1 to 10...")
        start_num, end_num = 1, 10
    else:
        try:
            start_num = int(sys.argv[1])
            end_num = int(sys.argv[2])
            
            # Swap values if the user accidentally puts the bigger number first
            if start_num > end_num:
                start_num, end_num = end_num, start_num
                
        except ValueError:
            print("Arguments must be numbers. Defaulting to a range of 1 to 10...")
            start_num, end_num = 1, 10

    # Start the game
    run_game(start_num, end_num)