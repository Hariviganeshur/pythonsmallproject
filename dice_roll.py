# Dice Rolling Game
import random  # Importing the random module to simulate dice rolls

# Infinite loop to continue rolling until the user stops
while True:
    # Ask the user if they want to roll the dice
    choice = input("Roll the dice again? (y/n): ")

    # If user chooses to roll
    if choice == 'y' or choice == 'Y':
        die1 = random.randint(1, 6)  # Roll first die
        die2 = random.randint(1, 6)  # Roll second die
        print(f'({die1},{die2})')    # Show result as a tuple

    # If user chooses to stop
    elif choice == 'n' or choice == 'N':
        print("Thank you!")
        break  # Exit the loop

    # If input is invalid
    else:
        print("Invalid choice, enter it correctly: y or n!")
