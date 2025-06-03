import random  # Importing random module to allow the computer to make random choices

# Infinite loop to keep the game running
while True:
    choices = ('r', 'p', 's')  # Possible choices: r = Rock, p = Paper, s = Scissors

    # Ask user for input
    user_choice = input("Select anyone Rock or Paper or Scissor (r/p/s): ").lower()

    # Validate user input
    if user_choice not in choices:
        print("Invalid input")
        continue  # Skip rest of loop and ask again

    # Generate random choice for computer
    computer_choice = random.choice(choices)

    # Show choices
    print(f"Computer chose {computer_choice}")
    print(f"You chose {user_choice}")

    # Determine winner
    if computer_choice == user_choice:
        print("It's a draw")
    elif (computer_choice == "r" and user_choice == "p") or \
         (computer_choice == "p" and user_choice == "s") or \
         (computer_choice == "s" and user_choice == "r"):
        print("You win")
    else:
        print("Sorry you lose")

    # Ask if user wants to play again
    After_match = input("Do you want to play again? (y/n): ").lower()
    if After_match == "n":
        print("Thank you for playing with me")
        break  # Exit the game loop
