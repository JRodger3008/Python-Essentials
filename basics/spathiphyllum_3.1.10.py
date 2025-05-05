# 3.1.10 LAB - Comparison operators and conditional execution.
# This is another one of my earlier works for the Python Essentials course.
# Note: *Spathiphyllum* is a genus that contains ~60 species of Peace Lily.
# Because it's a genus name, "Spathiphyllum" should be spelt with an upper-case 'S'.

# This program takes a user-inputted string and evaluates it using conditional statements.


user_input = str(input("Please enter a word: "))

# If user inputs "Spathiphyllum", prints successful message
if user_input == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best!")
# If user inputs "spathiphyllum" in lower-case
elif user_input == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
# If the input doesn't match either of the conditions above
else:
    print(f"Spathiphyllum! Not {user_input}!")
