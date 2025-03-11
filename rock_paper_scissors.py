import random

def store_user_choice():
    print("\n===========================")
    print("🪨 Rock, 📄 Paper, ✂️ Scissors")
    print("===========================")
    return input("Choose: 'rock', 'paper', or 'scissors'\nType 'quit' to exit: ").lower()

def display_result(user, computer, result):
    print("\n===========================")
    print(f"You chose: {user.capitalize()} 🎮")
    print(f"Computer chose: {computer.capitalize()} 🤖")
    print("===========================")
    print(f"🏆 Result: {result}\n")

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = store_user_choice()

    if user_choice == "quit":
        print("\nThanks for playing! 🎉")
        break

    if user_choice not in choices:
        print("\n❌ Invalid choice, try again!")
        continue

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        display_result(user_choice, computer_choice, "It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        display_result(user_choice, computer_choice, "You win! 🎉")
    else:
        display_result(user_choice, computer_choice, "Computer wins! 🤖")
