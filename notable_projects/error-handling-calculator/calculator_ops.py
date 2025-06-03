"""
calculator_ops.py - Core Logic for Modular Calculator

This module defines the 'calculate()' function used to perform basic arithmetic operations.
It supports the following operations: +, -, *, /, //, %, **, using Python's 'operator'
module for efficient function mapping (e.g., operator.pow == **).

It includes built-in error handling for:
    - Invalid operators (raises ValueError)
    - Division by zero (ZeroDivisionError)
    - Results that are infinite or NaN (raises OverflowError)

This module is intended for import into a UI script (calculator_ui.py), and to
be tested using calculator_unittest.py.

Dependencies:
    - operator module (standard library)
    - math module (for detecting overflow results)

Author: Jordan Rodger
Date: 23/05/2025
"""

import operator # Standard library for function-based arithmetic operations (e.g operator.add)
import math # For math.isinf() and math.nan()

# Ops dictionary function mapping
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod,
    "**": operator.pow
}

def calculate(num1, num2, operation):
    """
    Performs a calculation based on the given numbers and operation.

    Args:
        num1 (float): The first operand.
        num2 (float): The second operand.
        operation (str): One of '+', '-', '*', '/', '//', '%', '**'.

    Returns:
        float: The calculated result.

    Raises:
        ValueError: If the operation is not supported.
        ZeroDivisionError: If division by zero is attempted.
        OverflowError: If the number is too large to represent.
    """
    # Cross-reference ops dictionary to catch invalid operations
    if operation not in ops:
        raise ValueError(f"Invalid operation: '{operation}' is not supported. "
                        f"Please choose from: {', '.join(ops.keys())}") # Outputs valid operator symbols
    
    result = ops[operation](num1, num2)

    # Only check for overflow/NaN if result is a float.
    # Integers in Python do not produce inf or NaN, even when extremely large (due to Arbitrary Precision).
    if isinstance(result, float) and (math.isinf(result) or math.isnan(result)):
        raise OverflowError("Calculation resulted in an overflow (inf or NaN)")

    return result