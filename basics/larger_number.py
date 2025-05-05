# This program takes two user-inputted numbers, compares them, and returns the larger
# number

number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))

if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

print(f"The larger number is: {larger_number}")
