# This is a short program that converts mile to kilometers, and vise versa.
# I've used two sets of test data, and created reusable conversion functions.

# First set of test data
kilometers = 12.25
miles = 7.38

# Conversion rates
# Function to convert miles to kilometers
def miles_to_kilometers(miles):
    return miles * 1.61

# Function to convert kilometers to miles
def kilometers_to_miles(kilometers):
    return kilometers / 1.61

# Output conversion results for the first set of test data
# All conversion results are rounded to 2 decimal places
print(miles, "miles is", round(miles_to_kilometers(miles), 2), "kilometers") # 7.38 miles is 11.88 kilometers
print(kilometers, "kilometers is", round(kilometers_to_miles(kilometers), 2), "miles") # 12.25 kilometers is 7.61 miles

# Second set of test data 
kilometers_2 = 30.8
miles_2 = 63.99

# Output conversion results for the second set of test data
print(miles_2, "miles is", round(miles_to_kilometers(miles_2), 2), "kilometers") # 63.99 miles is 103.02 kilometers
print(kilometers_2, "kilometers is", round(kilometers_to_miles(kilometers_2), 2), "miles") # 30.8 kilometers is 19.13 miles
