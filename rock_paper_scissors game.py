import random



def play_game():

    choices = ["rock", "paper", "scissors"]

    user_score = 0

    computer_score = 0

    total_rounds = 0

    

    print("=== Welcome to Rock, Paper, Scissors (v2.0) ===")

    

    # Get winning condition from user

    while True:

        try:

            target_score = int(input("Enter target score to win the match (e.g., 3): "))

            if target_score > 0:

                break

            print("Please enter a number greater than 0.")

        except ValueError:

            print("Invalid input. Please enter a valid integer.")



    print(f"\nFirst to reach {target_score} wins the match! Type 'quit' to exit.\n")

    

    # Main game loop

    while user_score < target_score and computer_score < target_score:

        user_choice = input(f"[Score - You: {user_score} | Computer: {computer_score}] Enter choice: ").strip().lower()

        

        if user_choice == 'quit':

            print("\nGame ended early by user.")

            break

            

        if user_choice not in choices:

            print("Invalid choice. Choose rock, paper, or scissors.\n")

            continue

            

        computer_choice = random.choice(choices)

        print(f"Computer chose: {computer_choice}")

        total_rounds += 1

        

        # Determine round winner

        if user_choice == computer_choice:

            print("Round result: It's a tie!\n")

        elif (user_choice == "rock" and computer_choice == "scissors") or \

             (user_choice == "paper" and computer_choice == "rock") or \

             (user_choice == "scissors" and computer_choice == "paper"):

            print("Round result: You win this round!\n")

            user_score += 1

        else:

            print("Round result: Computer wins this round!\n")

            computer_score += 1



    # End game summary

    print("=========================================")

    if user_score == target_score:

        print(" Congratulations! You won the match! ")

    elif computer_score == target_score:

        print(" Computer won the match. Better luck next time!")

        

    if total_rounds > 0:

        win_rate = (user_score / total_rounds) * 100

        print(f"Match Statistics: Total Rounds: {total_rounds} | Your Win Rate: {win_rate:.1f}%")

    print("=========================================")



if __name__ == "__main__":

    play_game()
