# Program to check if a user-inputted number is even or odd

user_input = int(input("Please input a number: "))


def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0 # Uses modulus (%) to determine if a number is even


if is_even(user_input):
    print(f"{user_input} is even")
else:
    print(f"{user_input} is odd")
    


