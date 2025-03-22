import random
import time
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()

def print_colored(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print_colored("\n🎮 Welcome to the Number Guessing Game! 🎮", Fore.CYAN)
    print_colored("I'm thinking of a number between 1 and 100...", Fore.YELLOW)
    time.sleep(1)
    print_colored(f"You have {max_attempts} attempts to guess it!", Fore.GREEN)

    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input(f"\n{Fore.WHITE}Enter your guess (1-100): "))
            attempts += 1

            # Check if guess is valid
            if guess < 1 or guess > 100:
                print_colored("Please enter a number between 1 and 100!", Fore.RED)
                continue

            # Check if guess is correct
            if guess == secret_number:
                print_colored(f"\n🎉 Congratulations! You found the number in {attempts} attempts! 🎉", Fore.GREEN)
                return True
            elif guess < secret_number:
                print_colored("Too low! ⬆️", Fore.BLUE)
            else:
                print_colored("Too high! ⬇️", Fore.RED)

            # Show remaining attempts
            print_colored(f"Attempts remaining: {max_attempts - attempts}", Fore.YELLOW)

        except ValueError:
            print_colored("Please enter a valid number!", Fore.RED)
            attempts += 1

    print_colored(f"\n😢 Game Over! The number was {secret_number}", Fore.RED)
    return False

def main():
    while True:
        play_game()
        
        # Ask if player wants to play again
        play_again = input(f"\n{Fore.WHITE}Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print_colored("\nThanks for playing! Goodbye! 👋", Fore.CYAN)
            break

if __name__ == "__main__":
    main() 