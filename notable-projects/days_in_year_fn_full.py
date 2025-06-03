"""
4.3.6 LAB - Day of the year: writing and using your own functions.

Scenario:
    Your task is to write and test a function which takes three arguments (a year,
    a month, and a day of the month) and returns the corresponding day of the year,
    or returns None if any of the arguments is invalid.

Like in my other projects, I've tried to go beyond the lab requirements by implementing:
    - Graceful error handling
    - Modular helper functions
    - Comprehensive edge case testing with a test/debug loop

Notable Improvements:
    - Simplified leap year logic (is_year_leap())
    - Used 'enumerate(zip(...))' for cleaner iteration in test loops
    - Added type checking and robust validation to avoid silent failures

Author: Jordan Rodger
Date: 08/05/2025 (Last Edit: 28/05/2025)
"""


# Number of days in month
month_lengths = [31, # Jan
                 28, # Feb
                 31, # Mar
                 30, # Apr
                 31, # May
                 30, # June
                 31, # July
                 31, # Aug
                 30, # Sept
                 31, # Oct
                 30, # Nov
                 31  # Dec
                 ]


# Function to determine if a year is a leap year
def is_year_leap(year: int) -> bool:
    """
    Determines if a given year is a leap year.
    A year is a leap year if:
        - It is divisible by 4, and
        - If divisible by 100, it must also be divisible by 400.
    Leap years have 366 days, whereas regular years have 365.

    Args:
        year (int): The year to check for leap year status.

    Returns:
        bool: True if the year is leap year, False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Function to determine number of days in a given month
def days_in_month(year: int, month: int) -> int | None:
    """
    Returns the number of days in a given month of a given year.
        - Handles leap years for February (28 -> 29).
        - Handles invalid month and year inputs.

    Args:
        year (int): The year of interest.
        month (int): The month (1-12) for which the number of days is determined.

    Returns:
        int or None: The number of days in a given month; None for invalid input.
    """
    
    # Type validation (int)
    if not isinstance(year, int) or not isinstance(month, int):
        return None # Return None if year or month is not an integer
    
    # Acceptable ranges
    # If month is less than 1 or more than 12, or year is less than 1582 (start of Gregorian calendar)
    if not(1 <= month <= 12) or year < 1582:
        return None # Invalid month or invalid year

    # Adjust February if it's a leap year
    if month == 2 and is_year_leap(year):
        return 29 # Return 29 for Feb leap year days
    
    return month_lengths[month - 1] # Return the regular number of days for the month



# Function to determine day of year
def day_of_year(year: int, month: int, day: int) -> int | None:
    """
    Returns the day of the year for a given date, or None if inputs are invalid.
        - Validates year, month, and day.
        - Uses days_in_month() to account for leap years.

    Args:
        year (int): The year of interest.
        month (int): The month (1-12) for which the day of the year is to be calculated.
        day (int): The day of the month (1-31) for which the day of the year is to be calculated

    Returns: 
        int or None: The day of the year; None for invalid inputs.
    """

    # Type validation (int)
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        print(f"Invalid type: year={type(year)}, month={type(month)}, day={type(day)} ")
        return None # Year, month, and day must be integers
    
    # Acceptable ranges; return None
    if not (1 <= month <= 12) or year < 1582:
        return None
    
    # Sum current days in month
    current_month_days = days_in_month(year, month)
    if current_month_days is None or not (1 <= day <= current_month_days):
        return None # Invalid day (out of range for month)
    
    total_days = 0
    for m in range(1, month):
        days = days_in_month(year, m)

        # Error handling in case of silent accumulation
        if days is None:
            return None
        
        total_days += days # Accumulate days from previous months
    
    return total_days + day # Adds days from current month



# Test data
test_year = [2000, 2020, 1789]
test_month = [1, 12, 3]
test_day = [1, 30, 22]
test_result = [1, 365, 81]


# Edge cases - Invalid type, values outside of acceptable range, etc.
test_year += [2021, 1999, 1700, 2020, 2022, "2010", 2020, 1500, 2001]
test_month += [2, 9, 13, 12, 12, 4, 2, 9, 9.7]
test_day += [29, 100, 25, 31, 31, 9, 29, 10, 12]
test_result += [None, None, None, 366, 365, None, 60, None, None]


# Test loop to verify day_of_year() against a set of test cases,
# printing 'OK' or 'FAILED' with expected and actual results for debugging.

# zip(...) combines elements from the three lists into (year, month, day) tuples.
# enumerate(...) adds an index (i) to each tuple for accessing expected results.
for i, (yr, mo, dy) in enumerate(zip(test_year, test_month, test_day)):
    result = day_of_year(yr, mo, dy)

    # Converts None type to string to avoid TypeError in f-string formatting
    expected = str(test_result[i]) if test_result[i] is not None else "None"
    actual = str(result) if result is not None else "None"

    # Match case: both expected and actual are None
    if result is None and test_result[i] is None:
        print(f"(Y: {yr:<6}, M: {mo:<4}, D: {dy:<4}) -> {expected} -> {result} -> 'OK'\n")

    # Match case: expected and actual values match
    elif result == test_result[i]:
        print(f"(Y: {yr:<6}, M: {mo:<4}, D: {dy:<4}) -> {expected:<6} -> {result:<6} -> 'OK'\n")

    # Mismatch case: expected and actual differ
    else:
        print(f"(Y: {yr:<6}, M: {mo:<4}, D: {dy:<4}) -> {expected:<6} -> {result:<6} -> 'FAILED'\n")