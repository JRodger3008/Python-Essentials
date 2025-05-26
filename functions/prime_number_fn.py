# 4.3.7 LAB - Prime numbers - How to find them.

# Your task is to write a function checking whether a number is prime or not.
# The function:
#   - Is called is_prime;
#   - Takes one argument (the value to check)
#   - Returns True if the argument is a prime number, and False otherwise.  


def is_prime(n):
    # Any number less than 2 is not prime by definition
    if n < 2:
        return False
    
    # Only check up to the square root of n (inclusive) for efficiency.
    # If n is divisible by any number greater than its square root,
    # the corresponding factor will be smaller and already checked.
    # Example: 49 = 7 × 7 -> sqrt(49) = 7
    for i in range(2, int(n ** 0.5) + 1):

        # If divisible by any number in range, it's not prime
        if n % i == 0:
            return False
        
    # If no divisors found, it's a prime number
    return True

# Test and print all prime numbers between 2 and 100.
for i in range(1, 100):
    if is_prime(i + 1):
        print(i + 1, end=" ")