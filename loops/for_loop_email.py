# This program takes an email address and prints the characters before the "@"
# symbol using a for loop and break statement

for ch in "john.smith@pythoninstitute.org":
    if ch == "@": # Checks if character is "@" symbol
        break # Breaks out of the loop when "@" is encountered
    print(ch, end="") # Prints the characters before the "@"
