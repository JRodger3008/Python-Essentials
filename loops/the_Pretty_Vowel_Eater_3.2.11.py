# 3.2.11 LAB - The Pretty Vowel Eater

# The following is a breakdown of conditions:
# 1. Use a for loop.
# 2. Use conditional execution (if-elif-else).
# 3. Use the continue statement to skip vowels.

# This program takes a user input word, and "eats" the vowels, leaving the
# consonants, which is printed on the same line using concatenation operator.

# Prompt user to enter word
user_word = input("Please input any word: ")

# Initialise an empty string to store the word without vowels
word_without_vowels = ""

# Convert user word to upper-case
user_word = user_word.upper()

# Loop through each letter in the word
for letter in user_word:
    # If the letter is a vowel, skip it
    if letter in 'AEIOU':
        continue # Skip vowels
    # Concatenate the consonants to word_without_vowels
    word_without_vowels += letter

# Print the word without vowels
print("The word without vowels is: ", word_without_vowels)