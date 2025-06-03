"""
This program calculates and displays the first 15 Fibonacci numbers,
using the formula: FIB(n) = FIB(n-1) + FIB(n-2), where n ≥ 3.

It also compares the execution times of three different implementations:
   - Iterative Function: fib_iterative() (TC: Linear time - O(n))
   - Naive Recursive Function: fib_recursive() (TC: Exponential time - O(2^n))
   - Recursive Function with Memoization: fib_memo() (TC: Linear time - O(n))
*TC = Time Complexity

Note: Once I understand matrix exponentiation (TC: Logarithmic time - O(log n)), I'd like to 
      revisit this and add it as an example.

Author: Jordan Rodger
Date: 12/05/2025 (Last Edited: 26/05/2025)
"""

import time # For .perf_counter()
from functools import lru_cache # LRU = Least Recently Used


def fib_iterative(n):
    """
    Returns:
        int or None: The nth Fibonacci number, or None if n < 1 (invalid input).
    """
    if n < 1:
        return None # Invalid input: Fibonacci sequence is defined for n >= 1
    if n < 3:
        return 1 # FIB(1) and FIB(2) = 1
    
    a = b = 1 # Initialise FIB(1) and FIB(2)

    # Calculate Fibonacci numbers for FIB(3) to FIB(n)
    for i in range(3, n + 1):
        a, b = b, a + b # Move the window: update previous two numbers (tuple unpacking)
    return b

# Loop from 1 to 15, displaying the Fibonacci number for each n
for n in range(1, 16):
    print(f"{n:2} -> {fib_iterative(n)}")

# Expected output:
# 1 -> 1, 2 -> 1, 3 -> 2, ..., 15 -> 610



# Naive recursion becomes extremely slow for n ≥ 35 due to redundant calls,
# illustrating why recursion isn't always optimal for performance.
# That said, recursion can be elegant, intuitive, and valuable in divide-and-conquer algorithms.
def fib_recursive(n):
    """
    Returns:
        int or None: The nth Fibonacci number using naive recursion, or None if n < 1 (invalid input).
    """
    # Base cases: FIB(1) and FIB(2) = 1
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)



# Memoized recursion using @lru_cache(): caches previously computed results
# to avoid redundant calls, significantly improving performance.
# Since maxsize=None, ALL previously computed results will be stored.
# Note: Very large inputs may still hit Python's default recursion limit (~1000).
@lru_cache(maxsize=None)
def fib_memo(n):
    """
    Returns:
        int or None: The nth Fibonacci number, using memoized recursion, or None if n < 1 (invalid input).
    """
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib_memo(n - 1) + fib_memo(n - 2)



def timed(func, n):
    """
    Measures and prints the execution time of a function called with a single integer argument.

    Note:
        Uses time.perf_counter() for timing because it provides a high-resolution, monotonic
        clock (never goes backwards or jumps forward), making it ideal for benchmarking.
        Unlike time.time(), it is not affected by system clock updates and offers more precise 
        measurements for short durations: https://docs.python.org/3/library/time.html#time.perf_counter

    Args:
        func (callable): The function to be called. Must accept a single integer argument.
        n (int): The integer argument to pass to the function.

    Prints:
        str: The function name, its result, and execution time in seconds formatted to 8 decimal places.
    """
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    print(f"{func.__name__}({n}) = {result} -> took {end - start:.8f} seconds.")



# ====== PERFORMANCE COMPARISON ======
print("\n====== Performance Comparison ======")
# Note: All execution times will vary depending on system load and environment.


fib_num = 40

# fib_iterative: fast and efficient for large values of n.
timed(fib_iterative, fib_num)
# Example: fib_iterative(40) = 102334155 -> took 0.00000480 seconds.



# fib_recursive(): computationally expensive and very slow for large n, due to redundant
# calls - this is the key difference between naive recursion and recursion with memoization.

# fib_recursive becomes exponentially slower as n increases.
# n = 20 is chosen to demonstrate performance without freezing the script.
timed(fib_recursive, 20)
# Example: fib_recursive(20) = 6765 -> took 0.00112190 seconds.
# Reference: fib_recursive(40) = 102334155 -> took 18.16289960 seconds.



# fib_memo() offers an elegant recursive approach while maintaining high
# performance via caching.
timed(fib_memo, fib_num)
# Example: fib_memo(40) = 102334155 -> took 0.00009840 seconds.



# Summary:
# - fib_iterative() is best for performance and scalability.
# - fib_recursive() demonstrates how recursion can become inefficient due to repeated calls.
# - fib_memo() combines recursion and performance through caching.