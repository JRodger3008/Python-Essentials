# A very short program using max() and min() functions

# Get user input for 3 numbers
number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
number3 = int(input("Please enter the third number: "))

# Uses max() and min() to find the largest and smallest number respectively
largest_number = max(number1, number2, number3)
smallest_number = min(number1, number2, number3)

# Output result
print("The largest number is: " , largest_number)
print("The smallest number is: " , smallest_number)
