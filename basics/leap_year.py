# LAB 3.1.12 - Essentials of the if-elif-else statements

# Since the introduction of the Gregorian calendar (in 1582), the following rule is used
# to determine the kind of year:
# 1. If the year number isn't divisible by four, it's a common year;
# 2. Otherwise, if the year number isn't divisible by 100, it's a leap year;
# 3. Otherwise, if the year number isn't divisible by 400, it's a common year;
# 4. Otherwise, it's a leap year.

year = int(input("Please input a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    # Checks if year is not divisible by 4
    if year % 4 != 0: 
        print("Common Year")
    # Checks if year is divisible by 4, but not 100
    elif year % 100 != 0: 
        print("Leap Year")
    # Checks if year is divisible by 100, but not 400
    elif year % 400 != 0: 
        print("Common Year")
    # If all conditions above fail, the year is a leap year
    else:
        print("Leap Year") 
