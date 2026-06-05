# This is a program for a game
''' This is a simple implementation of the Scissor, Paper, Stone game. The user will play against the computer, and the first to reach a specified target score wins the game. 
The user can choose to play again after each game.'''
import random
import sys


# Game function
def welcomegame():
    print("****************************************************************************************************************")
    print("Welcome to the Scissor, Paper, Stone Game!")
    print("****************************************************************************************************************")
    target = 0
    while target <= 0:
        try:
            target = int(input("Enter the target number: "))
        except ValueError:
            print("Please enter a valid positive integer for target.")
    print("To Win You have to score", target, "points")
    # Score for both opponents
    player_score = 0
    computer_score = 0
    round_number=1
    # Game loop
    print("Game Started")
    game(target,player_score, computer_score, round_number)


def game(target,player_score, computer_score,round_number):
    print(f"player score: {player_score}         Computer score: {computer_score}\nTarget: {target}")
    
    while True:
        if player_score < target and computer_score < target:
            round(player_score, computer_score, target, round_number)
        elif player_score >= target:
            print("************************************************************************************************")
            print("Congratulations! You win!")
            print("Thank you for playing!")
            print("************************************************************************************************")
        else:
            print("Computer wins! Better luck next time.")
            print("************************************************************************************************")
        print("Do you want to play again? (yes/no)")
        play_again = input().lower()
        if play_again == "yes":
            welcomegame()
        else:
            print("Thank you for playing! Goodbye!")
            sys.exit(0)

# Round function
def round(Player_score, computer_score, target, round_number):
    print("###############################################################################################")
    input("Press Enter to start the round...")
    print("###############################################################################################")
    print(f"Round {round_number} Started")
    # User Choice
    print("###############################################################################################")
    print("Select Options:\nScissor\nPaper\nStone")
    print("###############################################################################################")
    user_choice = ""
    while user_choice.lower() not in ["scissor", "paper", "stone"]:
        user_choice = input("Enter your choice: ")
        if user_choice.lower() not in ["scissor", "paper", "stone"]:
            print("Invalid choice. Please try again.")



    # Computer Choice
    computer_choice = random.choice(["scissor", "paper", "stone"])
    print(f"Computer chose: {computer_choice}")
    print("###############################################################################################")


    # Determine the winner of the round
    if user_choice.lower() == computer_choice:
        print("It's a tie! No points awarded.")
    elif (user_choice.lower() == "scissor" and computer_choice == "paper") or (user_choice.lower() == "paper" and computer_choice == "stone") or (user_choice.lower() == "stone" and computer_choice == "scissor"):
        print("You win this round! You get 1 point.")
        Player_score += 1
    else:
        print("Computer wins this round! Computer gets 1 point.")
        computer_score += 1
    round_number += 1
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    # Return to the game function with updated scores and round number
    game(target, Player_score, computer_score, round_number)


#----main----
print("Welcome to the Game!")
while True:
    print("1. Start Game")
    print("2. Exit")
    # User choice
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")
        continue
    if choice == 1:
        welcomegame()
    elif choice == 2:
        print("Thankyou")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")

