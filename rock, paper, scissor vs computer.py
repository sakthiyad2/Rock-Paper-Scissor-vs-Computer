import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_result(user, computer):
    if user == computer:
        return "It's a a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        user_choice = input("Enter rock, paper, scissors (or 'exit' to quit): ").lower()

        if user_choice == "exit":
            print("Game ended")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        print("Computer chose:", computer_choice)

        result = get_result(user_choice, computer_choice)
        print(result)
        print()

play_game()
