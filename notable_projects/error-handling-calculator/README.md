![Python](https://img.shields.io/badge/Python-3.13-blue)

# Modular Calculator

A Python modular calculator with robust arithmetic operations, CLI interface, and Unit Tests.

---

## Table of Contents

-   [Project Structure](#project-structure)
-   [Features](#features)
-   [Usage](#usage)
-   [Example](#example)
-   [Requirements](#requirements)
-   [Author](#author)

---

## Project Structure

-   **'calculator_ops.py'** - Core logic for arithmetic calculations (`+`, `-`, `*`, `/`, `//`, `%`, `**`).
-   **'calculator_ui.py'** - Command-line user interface to interact with the calculator.
-   **'calculator_unittest.py'** - Unit tests validating core logic and error handling.

---

## Features

-   Supports 7 arithmetic operations.
-   Handles invalid operations and division by zero.
-   Detects overflow and NaN results and raises errors.
-   Interactive CLI with robust input and error handling.
-   Includes Unit Tests covering normal and edge cases.

---

## Usage

### Run the calculator UI (CLI)

```bash
python calculator_ui.py
```

### Run Unit Tests

```bash
python -m unittest -v calculator_unittest.py
```

## Example

Here's a sample interaction with the Calculator UI:

```bash
$ python calculator_ui.py
Enter your first number: 22
Enter your second number: 3
Choose an operation from the following: +, -, *, /, //, %, **
> *

Result of 22.0 * 3.0 = 66.0

Would you like to perform another calculation? (y/n): y
Enter your first number: 9
Enter your second number: 0
Choose an operation from the following: +, -, *, /, //, %, **
> /

Oops! Division by 0 is undefined in our number system.
```

## Requirements

-   Python 3.6+ (Version used: Python 3.13.3)
-   No external libraries required (only standard Python libraries)

## Author

Jordan Rodger - [GitHub Profile](https://github.com/JRodger3008)
