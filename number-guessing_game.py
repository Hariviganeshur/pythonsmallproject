import random  # Importing random module to generate a random number

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Infinite loop to keep asking the user until they guess correctly
while True:
    try:
        # Ask the user for their guess and convert it to an integer
        user_guess = int(input("Guess a number between 1 and 100: "))

        # Compare the guess with the actual number
        if user_guess < number_to_guess:
            print("Too low")  # User's guess is too small
        elif user_guess > number_to_guess:
            print("Too high")  # User's guess is too large
        else:
            print("Correct, You won!")  # User guessed the correct number
            break  # Exit the loop

    except ValueError:
        # If user enters something that's not a number
        print("Please enter a number between 1 and 100:")
