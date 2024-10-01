import random

def get_user_choice():
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    while True:
        user_input = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").lower()
        if user_input in choices:
            return user_input, choices[user_input]
        else:
            print("Invalid choice, please try again.")

def get_computer_choice():
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    computer_choice = random.choice(list(choices.keys()))
    return computer_choice, choices[computer_choice]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        print("\n--- Rock, Paper, Scissors Game ---")
        user_choice, user_choice_full = get_user_choice()
        computer_choice, computer_choice_full = get_computer_choice()

        print(f"\nYou chose: {user_choice_full}")
        print(f"Computer chose: {computer_choice_full}")

        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")

        play_again = input("\nDo you want to play again? (Y/N): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__== "__main__":
    play_game()