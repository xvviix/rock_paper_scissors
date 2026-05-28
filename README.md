# rock_paper_scissors
A simple rock_paper_scissors game based on python coding
# Rock, Paper, Scissors Game 

A simple, interactive command-line Rock, Paper, Scissors game written in Python. This project serves as **Day 1** of a dedicated portfolio challenge, focusing on clean code practices, basic control flow, and input validation.

## Features
- **Robust Input Handling:** Automatically sanitizes user input (handles spacing and capitalization) and validates against unexpected entries.
- **Dynamic AI Opponent:** Uses Python's built-in `random` module to generate unpredictable computer moves.
- **Continuous Gameplay:** Features a persistent loop allowing the player to play multiple rounds until they explicitly type `quit`.

## Core Concepts Covered
- Control flow structures (`while` loops, `if-elif-else` conditions)
- Error filtering and input validation
- Working with Python standard libraries (`random`)

## What's new in v2.0
- **Score tracker:** keeps track of both player and camputer scores.
- **Match limit:** You can set a limit at the beginning(for example first one to reach 3 points wins)
- **End game status:** When the match ends or you type 'quit', it shows the total rounds played and calculates your winning percentage.
- **Input Check:** Added exception handling (`try-except`) so the program won't crash if you accidentally enter text instead of a number for the target score.

## How to Run
Make sure you have Python 3.x installed. Open your terminal and run the game
