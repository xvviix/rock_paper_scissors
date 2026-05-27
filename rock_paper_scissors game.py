import random

def play_game():
    """
    Main function to run the Rock, Paper, Scissors game loop.
    Handles user input, generates computer choices, and determines the winner.
    """
    choices = ["rock", "paper", "scissors"]
    
    print("--- Welcome to Rock, Paper, Scissors! ---")
    print("Type 'quit' at any time to exit the game.\n")
    
    while True:
        # 1. Get and sanitize user input
        user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        
        if user_choice == 'quit':
            print("Thanks for playing! Goodbye.")
            break
            
        if user_choice not in choices:
            print("Invalid input. Please choose rock, paper, or scissors.\n")
            continue
            
        # 2. Generate computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # 3. Determine the game outcome
        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("Congratulations! You win!\n")
        else:
            print("Computer wins! Better luck next time.\n")

if __name__ == "__main__":
    play_game()