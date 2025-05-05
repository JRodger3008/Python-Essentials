# 3.2.10 LAB - The Ugly Vowel Eater.

# The following is a breakdown of conditions:
# 1. Use a for loop.
# 2. Use conditional execution (if-elif-else).
# 3. Use the continue statement.

# This program takes a user input word, and "eats" the vowels, leaving the
# consonant(s), which is printed on a new line each time.


# Asks user to input any word
user_word = input("Please input any word: ")

# Convert user_word to upper-case
user_word = user_word.upper()

# Loop through each character in user_word
for letter in user_word: 
    # Skip vowels
    if letter in 'AEIOU': 
        continue
    print(letter) # Print each consonant, capitalised and on new lines.

