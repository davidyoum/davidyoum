import random

choices = ["rock", "paper", "scissors"]
while True:
    print("\nRock, Paper, Scissors! (or 'quit' to exit)")
    player = input("Your choice: ").lower()
    if player == 'quit':
        print("Thanks for playing! 👋")
        break
    if player not in choices:
        print("Invalid choice! Try again.")
        continue
    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("It's a tie! 🤝")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win! 🎉")
    else:
        print("Computer wins! 😢") 