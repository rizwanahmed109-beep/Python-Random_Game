# Random Number Guessing Game 🎲

A simple, interactive command-line game written in Python. The game generates a random number within a specified range, and the user must guess the correct number. It includes input validation and handles errors gracefully if incorrect arguments are provided.

## Features
* **Custom Number Ranges:** Set your own difficulty by defining the minimum and maximum numbers via terminal arguments.
* **Input Validation:** Prevents crashes if the user types letters or symbols instead of numbers.
* **Graceful Defaults:** Automatically defaults to a 1–10 range if no terminal arguments are provided.

## Prerequisites
* Python 3.x

## How to Run

You can run the script directly from your terminal. Provide two numbers after the script name to set your custom range.

**Syntax:**
```bash or Windows Terminal
python randomgame.py <start_number> <end_number>

## Example (Guessing between 1 and 50) ##
DOS
python randomgame.py 1 50
