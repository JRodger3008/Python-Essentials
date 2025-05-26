"""
calculator_unittest.py - Unit tests for Modular Calculator core logic.

This test suite verifies the core functionalities and error handling of the 
'calculate()' function imported from calculator_ops.py.

Tests cover:
    - Standard arithmetic operations: addition, subtraction, multiplication, 
      division, floor division, modulo, and exponentiation.
    - Edge cases: including zero, negative numbers, and underflow scenarios.
    - Error handling, including invalid operators (ValueError), division by zero 
      (ZeroDivisionError), and overflow (OverflowError).
    - Floating-point behavior according to the IEEE 754 double-precision format.

Notes:
    - Python uses the IEEE 754 double-precision floating-point format,
      with a representable range from ~5e-324 to 1.8e308 on most 
      modern 64-bit systems. (https://www.geeksforgeeks.org/ieee-standard-754-floating-point-numbers/)
    - IEEE: acronym for 'Institute of Electrical and Electronic Engineers'.
    - Underflow to zero occurs silently for values smaller than ~5e-324, without 
      raising exceptions. 
    - Unit test official documentation: https://docs.python.org/3/library/unittest.html
    - To run test, and enable output (-v) with more detail, use: 
      'python -m unittest -v calculator_unittest.py' 

Dependencies:
    - calculator_ops.py (provides the calculate() function)
    - unittest module (Python standard library, test framework)

Author: Jordan Rodger
Date: 23/05/2025
"""


import unittest
from calculator_ops import calculate

# TestCalculator inherits the superclass unittest.TestCase (provided by the unittest module),
# which imparts access to a range of assert methods for testing.
# (quick reference: https://www.mattcrampton.com/blog/a_list_of_all_python_assert_methods/)
class TestCalculator(unittest.TestCase):
    """
    Tests for arithmetic operations and error handling in calculate().
    
    Note:
        unittest will automatically discover and run all methods in TestCalculator prefixed 
        with 'test_', due to inheritance from unittest.TestCase.
    """

    # ====== General and valid test cases (+, -, *, /, //, %, and **) ======
    def test_addition(self):
        self.assertEqual(calculate(3, 4, "+"), 7)

    def test_subtraction(self):
        self.assertEqual(calculate(22, 9, "-"), 13)
    
    def test_multiplication(self):
        self.assertEqual(calculate(4, 10, "*"), 40)

    def test_division(self):
        """Uses .assertAlmostEqual() to handle potential floating-point rounding errors."""
        self.assertAlmostEqual(calculate(20, 2, "/"), 10.0) 
    
    def test_floordiv(self):
        self.assertEqual(calculate(9, 4, "//"), 2)
    
    def test_modulo(self):
        self.assertEqual(calculate(10, 3, "%"), 1)
    
    def test_power(self):
        self.assertEqual(calculate(5, 3, "**"), 125)


    # ====== Edge cases ======
    def test_zero_plus_zero(self):
        self.assertEqual(calculate(0, 0, "+"), 0)

    def test_mult_zero(self):
        self.assertEqual(calculate(22, 0, "*"), 0)

    def test_negative_mult(self):
        self.assertEqual(calculate(-9, 2, "*"), -18)

    def test_negative_expo(self):
        self.assertEqual(calculate(2, -2, "**"), 0.25)

    def test_power_neg_expo(self):
        self.assertEqual(calculate(5, -2, "**"), 0.04)

    def test_underflow_to_zero(self):
        """Values smaller than ~5e-324 underflow to 0.0 silently, without raising exceptions."""
        result = calculate(5e-324, 2, "**")
        self.assertEqual(result, 0.0)
    

    # ====== Exception tests (using .assertRaises()) ======
    def test_invalid_op(self):
        with self.assertRaises(ValueError):
            calculate(2, 9, "$")
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(7, 0, "/")
        
    def test_overflow_error_upper(self):
        """
        1.8e308 is the largest value that can be stored as a double precision 
        floating-point number in 64-bit computing.
        """
        with self.assertRaises(OverflowError):
            calculate(1e308, 2, "**") 



# Ensures all test methods are discovered and executed only when this script is run directly,
# not when it's imported as a module into another script or test suite (if __name__ == "__main__").
if __name__ == "__main__":
    unittest.main()