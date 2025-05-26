# 4.3.4 LAB - A leap year: writing your own functions
# Your task is to write and test a function which takes one argument (a year)
# and returns True if the year is a leap year, or False otherwise.


# Function to determine if a year is a leap year
def is_year_leap(year):
    # Not divisible by 4 -> not a leap year
    if year % 4 != 0:
        return False

    # Divisible by 100, check if divisible by 400
    elif year % 100 == 0:
        if year % 400 == 0:
            return True # Divisible by 100 and 400 -> leap year
        else:
            return False # Divible by 100, but not 400 -> not a leap year
    else:
        return True # Divisible by 4, but not 100 -> leap year


# Test data to verify the function
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]


# Loop through each test case and compare result to expected outcome
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)

    # Compares function output with expected results
    if result == test_results[i]:
        print("OK") # Function output matches expected result
    else:
        print("Failed") # Function output does not match expected result
