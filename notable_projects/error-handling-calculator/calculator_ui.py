"""
calculator_ui.py - User Interface for Modular Calculator

This script serves as the interactive command-line interface for the calculator
application. It prompts the user to input two numbers and select a mathematical operation.

Primary goals:
    - Build a calculator with robust error handling.
    - Practice writing a modular program.
    - Write my first unit test suite.
    - To get into the habit of writing quality comments and docstrings.

Error handling is achieved using try/except blocks to gracefully manage:
    - Invalid input types (ValueError)
    - Division by zero (ZeroDivisionError)
    - Overflow from very large float results (result > 1.8e308) (OverflowError)
    - User input cancellations via keyboard interrupt (Ctrl+C) (KeyboardInterrupt)
    - End-Of-File errors (Ctrl+D/Ctrl+Z) (EOFError)
    - Unexpected errors (default Exception)
Official documentation: https://docs.python.org/3/library/exceptions.html#bltin-exceptions

Dependencies:
    - calculator_ops.py: Core arithmetic logic
    - calculator_unittest.py: Unit test suite (optional)
    - sys module: To exit program (https://docs.python.org/2/library/sys.html)

Author: Jordan Rodger
Date: 23/05/2025
"""

from calculator_ops import calculate
import sys

while True:
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        # Strip whitespace from operator input
        operation = input("Choose an operation from the following: +, -, *, /, //, %, **\n> ").strip() 

        # Handle empty operation input
        if not operation:
            print("No operation entered. Please choose a valid operator.")
            continue

        result = calculate(num1, num2, operation)

    # Handles non-numeric inputs
    except ValueError as ve:
        print(f"\nInput error: {ve}")

    # Handles division by zero
    except ZeroDivisionError:
        print("\nOops! Division by 0 is undefined in our number system.")

    # Handles extremely large number operations
    except OverflowError:
        print("\nNumber is too large to calculate.")
    
    # Handles user cancelling input using Ctrl+C
    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting...")
        break

    # Handles End-Of-File input errors (Ctrl+D (Linux/Mac) / Ctrl+Z (Windows))
    except EOFError:
        print("\nNo input received (EOF). Exiting...")
        break

    # Handles unexpected errors - though keep in mind that a default exception
    # may silently 'swallow' bugs, hide code errors, and make it harder to debug.
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

    else:
        print(f"\nResult of {num1} {operation} {num2} = {result}")

        # Ask user if they want to do another calculation - continue or exit.
        # Loop until a valid response ('y'/'yes' or 'n'/'no') is received.
        while True:
            cont = input("\nWould you like to perform another calculation? (y/n): ").strip().lower()
            if cont in ('y', 'yes'):
                break 
            elif cont in ('n', 'no'):
                print("Thanks for using the calculator. Have a great day!")
                sys.exit() # Successfully terminates program, with exit status code 0 (default)
            else:
                print("\nInvalid input. Please enter 'y' for yes, or 'n' for no.")