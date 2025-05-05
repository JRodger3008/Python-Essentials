# This program will take a user input number and square it.
# The second part demonstrates two iterations of Pythagorean Theorem, with cleaner code at the end
# to eliminate unnecessary variables.

# Note: float() is used to type cast input (type conversion).
# If an integer is input, it works fine. However, if a float is inputted and int() was used instead
# of float(), it would raise a ValueError: "invalid literal for int()".

input_number = float(input("Please enter a number: "))
power_2 = input_number ** 2
print(input_number, "To the power of 2, is: ", power_2)

# Pythagorean Theorem: Calculates the hypotenuse given two leg lengths
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5 # ** 0.5 is equivalent to square root
print("Hypotenuse length is", hypo)

# Cleaner code without 'hypo' variable:
# The print() function directly calculates the hypotenuse without storing it in a separate variable.
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)                     
