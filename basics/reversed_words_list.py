# This is a program that reverses each word in a list.
# The second part reverses words with more than 3 letters.

words = ["python", "loop", "challenge", "fun"]
reversed_words = []

for i in range(len(words)):
    reversed_words.append(words[i][::-1]) # [::-1] reverses the word

print(words)
print(reversed_words) # ['nohtyp', 'pool', 'egnellahc', 'nuf']
print()

# The following will only reverse words with more than 3 letters
words_2 = ["python", "loop", "challenge", "fun", "go", "yes"]
print(words_2)
reversed_words_2 = []

for word in words_2:
    if len(word) > 3:
        reversed_words_2.append(word[::-1])

print(reversed_words_2) # ['nohtyp', 'pool', 'egnellahc']
