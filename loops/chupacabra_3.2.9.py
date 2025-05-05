# The break statement - Stuck in a loop 3.2.9 LAB

# This program repeatedly asks the user to enter the secret word.
# It uses a `while` loop for continuous input and the `break` statement to
# exit when the correct word is entered.

secret_word = "chupacabra"

# Infinite loop until the user enters the correct word
while True:
    user_input = input("Please enter the secret word: ")

    # Compare the user input with the secret word, ignoring case
    if user_input.lower() == secret_word:
        print("You've successfully left the loop!")
        break # Exit the loop when the correct word is entered
    else:
        print("Ha Ha! You're stuck in my loop!") # Incorrect input - keeps user in the loop
