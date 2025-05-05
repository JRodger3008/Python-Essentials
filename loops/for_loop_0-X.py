# This program replaces 0's in a number with "x" and prints the result

for digit in "0165031806510":
    if digit == "0": # Checks if digit is 0
        print("x", end="") # Replace 0 with 'x'
        continue # Skip printing the digit (0) and move to the next iteration
    print(digit, end="") # Print all other digits as they are
