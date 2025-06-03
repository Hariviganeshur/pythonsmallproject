import random  # Import the random module for generating random characters

# Define the set of allowed characters for the password
combination_of_password = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+"

# Display a welcome message
print("Welcome to the Password Generator!")

# Ask the user to enter the desired password length
length_of_password = int(input("How much do you want for your password? : "))

# Initialize an empty string to store the generated password
password = ""

# Loop to generate each character of the password
for i in range(1, length_of_password + 1):
    # Randomly select a character from the allowed characters
    character = random.choice(combination_of_password)
    # Append the selected character to the password
    password += character

# Print the final generated password
print(password)
