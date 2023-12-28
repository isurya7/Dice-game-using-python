import random

def roll_dice():
    """Simulates rolling a six-sided dice."""
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Game!")
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}!")

    play_again = 'yes'
    while play_again.lower() == 'yes':
        input("Press Enter to roll the dice...")
        roll_result = roll_dice()
        print(f"You rolled a {roll_result}!")

        if roll_result == 6:
            print("Congratulations! You rolled a 6. You win!")
        else:
            print("Better luck next time!")

        play_again = input("Do you want to roll again? (yes/no): ")

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
