# Collatz' Conjecture LAB 3.2.15

# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, go back to point 2.


import time

c0 = int(input("Please enter a number: "))

steps = 0

print(f"Starting number: {c0}")

while c0 != 1: # Providing the c0 is not 1, while loop will execute
    if c0 % 2 == 0: # Checks if c0 is even
        c0 = c0 // 2
    else: # Condition for odd numbers
        c0 = (3 * c0) + 1
    steps += 1
    print(c0)
    time.sleep(.5) # Failsafe to keyboard interrupt, if necessary


print(f"Number of Steps: {steps}")
