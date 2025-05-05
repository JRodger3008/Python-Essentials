# This program evaluates if a user-inputted integer is a prime number, and handles invalid inputs.

import math

try:
    user_input = int(input("Please enter a whole number: "))

    def is_prime(n):
        if n <= 1: # Not prime if less than or equal to 1
            return False
    
        # Only checks divisors up to square root of n
        for i in range(2, int(math.sqrt(n)) + 1):
        
            # If n has any divisors other than 1 and itself, it's not prime
            if n % i == 0: 
                return False
        return True # If no divisors are found, n is prime

    # Call function and pass user_input to return result
    if is_prime(user_input):
        print(user_input, "is a prime number")
    else:
        print(user_input, "is NOT a prime number")

# Handle invalid inputs
except ValueError:
    print("Invalid input. Please enter a whole number: ")
