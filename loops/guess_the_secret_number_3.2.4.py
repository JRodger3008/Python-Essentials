# LAB 3.2.4 - Guess the secret number.

# A junior magician has picked a secret_number variable (777) that the user has to guess.
# Step 1: Ask user to enter an integer.
# Step 2: Use a while loop to check if the inputted number is 777, if incorrect the loop will continue.
# Step 3: Once guessed correctly, exit the loop.

# Additionallty I've included error/exception handling for non-integer inputs (ValueError).

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# If the user enters a non-integer value, it will prompt them again without crashing the program.

while True:
    try:
        number = int(input("Guess Away: ")) # Prompts user to guess a number, and convert input to integer
        if number == secret_number: # Compares input number with secret_number (777)
            print("Well done, muggle! You are free now")
            break # Exit loop if the user guesses correctly
        else:
            print("Ha ha! You're stuck in my loop!") # Incorrect input
    except ValueError:
        print("That's not a valid number!") # Handles non-integer inputs


# The block below was my original code without error handling, but I decided to combine ValueError handling
# within the main while loop:

# while number != 777:
#    print("Ha ha! You're stuck in my loop!")
#    number = int(input("Try again: "))
#else:
#    print("Well done, muggle! You are free now")
