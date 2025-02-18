import random

def print_instructions():
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose one of the following:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("Instructions: Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.")
    print()

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
            if choice == 1:
                return "rock"
            elif choice == 2:
                return "paper"
            elif choice == 3:
                return "scissors"
            else:
                print("Invalid input! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0
    play_again = "yes"
    
    while play_again.lower() == "yes":
        print_instructions()
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"Score: You - {user_score} | Computer - {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ")
        print()

    print("Thanks for playing!")


play_game()