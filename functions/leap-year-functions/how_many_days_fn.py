# 4.3.5 LAB - How many days: writing and using your own functions.

# Scenario:
#   Your task is to write and test a function which takes two arguments
#   (a year and a month) and returns the number of days for the given year-month
#   pair (while only February is sensitive to the year value, your function should
#   be universal).

# I've tried to go beyond what the lab required for this task, so I've included
# test edge cases, error handling (None values), input validation (int check,
# Gregorian Calendar check, and valid month range).


def is_year_leap(year):
    """
    Determines if a given year is a leap year.
    A year is a leap year if:
        - It is divisible by 4, and;
        - If divisible by 100, it must also be divisible by 400.
    Leap years have 366 days, whereas regular years have 365.
    """
    
    if year % 4 != 0:
        return False # Not divisible by 4 -> not a leap year
    
    # Divisible by 100, check if divisible by 400
    elif year % 100 == 0:
        if year % 400 == 0:
            return True # Divisible by 100 and 400 -> leap year
        else:
            return False # Divible by 100, but not 400 -> not a leap year
    else:
        return True # Divisible by 4, but not 100 -> leap year



def days_in_month(year, month):
    """
    Returns the number of days in a given month of a given year.
        - Handles leap years for February (28 -> 29).
        - Handles invalid month and year inputs.
    Returns None for invalid inputs.
    """
    
    # Handle invalid types or out of range values for years and months
    if not isinstance(year, int) or not isinstance(month, int):
        return None # Return None if year or month is not an integer
    
    # If month is less than 1 or more than 12, or year is less than 1582 (start of Gregorian calendar)
    if not(1 <= month <= 12) or year < 1582:
        return None # Invalid month or invalid year

    # Days in month using tuples (month, days)
    days_in_month = [
        (1, 31), # Jan
        (2, 28), # Feb (28 days for regular year)
        (3, 31), # Mar
        (4, 30), # Apr
        (5, 31), # May
        (6, 30), # June
        (7, 31), # July
        (8, 31), # Aug
        (9, 30), # Sept
        (10, 31), # Oct
        (11, 30), # Nov
        (12, 31) # Dec
        ]

    # Loop through days_in_month to find correct number of days in a given month
    for m, days in days_in_month:
        if m == month:
            # If month is Feb, check if leap year
            if month == 2 and is_year_leap(year):
                return 29 # Return 29 for Feb if it's a leap year
            return days # Return the regular number of days for the month
    

# Initial test data
test_years = [1900, 2000, 2016, 1987] 
test_months = [2, 2, 1, 11] 
test_results = [28, 29, 31, 30] 

# Edge cases - Invalid types, year < 1582, 12 >= month >= 1, etc.
test_years += [1581, 1999, 2024, 1582, "1800", 1942, 1859, 1799]
test_months += [11, 13, 2, 2, 7, -1, 12, 0]
test_results += [None, None, 29, 28, None, None, 31, None]


# Loop through each test case and compare result to expected outcome
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]

    result = days_in_month(yr, mo)

    # Handle None values, and convert to string for output
    expected = str(test_results[i]) if test_results[i] is not None else "None"
    actual = str(result) if result is not None else "None"

    if result == test_results[i]:
        # Formatted strings to produce a table-like output
        # If test_results match result, print OK
        print(f"{yr:<6}, {mo:<4} -> Expected: {expected:<4}, Got: {actual:<4} -> OK\n")
         
    else:
        # If test_results don't match result, print Failed
        print(f"{yr:<6}, {mo:<4} -> Expected: {expected:<4}, Got: {actual:<4} -> Failed\n")