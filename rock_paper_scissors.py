import random

def store_user_choice():
    print("\n===========================")
    print("🪨 Rock, 📄 Paper, ✂️ Scissors")
    print("===========================")
    return input("Choose: 'rock', 'paper', or 'scissors'\nType 'quit' to exit: ").lower()

def display_result(user, computer, player_score, computer_score, result):
    print("\n===========================")
    print(f"You chose: {user.capitalize()} 🎮")
    print(f"Computer chose: {computer.capitalize()} 🤖")
    print("===========================")
    print(f"🏆 Result: {result}\n")
    print(f"📊 Score - You: {player_score} | Computer: {computer_score} \n")  # ✅ Show score after every round

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while True:
    user_choice = store_user_choice()

    if user_choice == "quit":
        print("\n===========================")
        print(f"🎉 Final Score - You: {player_score} | Computer: {computer_score}")
        print("Thanks for playing! 🚀")
        print("===========================\n")
        break

    if user_choice not in choices:
        print("\n❌ Invalid choice, try again!")
        continue

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        display_result(user_choice, computer_choice, player_score, computer_score, "It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
         player_score += 1
         display_result(user_choice, computer_choice, player_score, computer_score, "You win! 🎉")
        
    else:
        computer_score += 1
        display_result(user_choice, computer_choice, player_score, computer_score, "Computer wins! 🤖")
