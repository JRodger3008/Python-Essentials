# This program evaluates n! (factorial) for numbers 1 through 10 using a custom function.
# I've also included an example of recursion (factorial_recursive()), while keeping the
# original iterative functionality.

def factorial_function(n):
    """
    Function to calculate factorial of n (int).

    Returns:
        int: Factorial of n (1 if n is 0 or 1).
        None: For negative values.
    """

    # Return None for negative values; return 1 for 1! and 0!
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1

    # Loops from 2 to n + 1 and multiplies product by i
    for i in range(2, n + 1):
        product *= i
    return product


# Loops from 1 to 10, and displays factorial product of n!
for n in range(1, 11):
    print(f"{n}! = {factorial_function(n)}")

# Output:
# 1! = 1, 2! = 2, 3! = 6, ..., 10! = 3628800


# Recursive factorial definition: n! = n * (n - 1)!
# Example of recursion - however keep in mind that recursion can greatly affect performance,
# and raises the risk of stack overflow.
def factorial_recursive(n):
    """
    Function to calculate factorial of n (int) using recursion.

    Returns:
        int: Factorial of n (1 if n is 0 or 1).
        None: For negative values.
    
    Note:
        Recursion depth limit (~1000) may be reached for very large n, raising a RecursionError.
    """
    # Base cases - terminate recursion when n < 2
    if n < 0:
        return None
    if n < 2:
        return 1
    
    # Recursion (self-referential function call)
    return n * factorial_recursive(n - 1)