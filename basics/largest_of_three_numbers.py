# Sequential Comparison, without using max() function.
# This program finds the largest number among three user-inputted numbers.

# Take three integer inputs from user
number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
number3 = int(input("Please enter the third number: "))

# Assume the first number is the largest
largest_number = number1 

# The largest_number variable is updated based on the comparison results (if statements)
if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3
    
print(f"The largest number is: {largest_number}")
