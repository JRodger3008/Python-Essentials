# This program evaluates hypotenuse, c
# a^2 + b^2 = c^2
a = float(input("Please enter value for side a: "))
b = float(input("Please enter a value for side b: "))

# If the user inputs a number that is less than or equal to 0
if a <= 0 or b <= 0:
    print("Both sides must be a positive value")
else:
    c = ((a ** 2 + b ** 2) ** 0.5) # ** 0.5 to find square root
    # {a:.4f}: references variable a 
    # ':' is format specifier, 
    # '.' separates the whole number from the decimal part 
    # '4' is the number of desired decimal places (4 d.p)
    # 'f' references a floating-point number
    print(f"a = {a:.4f}") # example: 3.0000
    print(f"b = {b:.4f}") # example: 4.0000
    print(f"c = {c:.4f}") # example: c = 5.0000
