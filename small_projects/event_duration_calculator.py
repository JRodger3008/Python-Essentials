# Operators and expressions LAB 2.6.11

# This program takes an inputted time in hours and minutes, and the duration
# of an event, to output the finishing time

# Get the starting time and event duration from the user
hours = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event Duration (in minutes): "))

# Add the event duration to the current minutes
mins += dura

# Adjust hours for any overflow of minutes
hours += mins // 60

# Calculate the new minutes and adjust hours for 24-hour format
mins %= 60
hours %= 24

print(f"{hours:02d}:{mins:02d}")
# :02d is a format specifier:
# 0: Pads the number with leading 0s (e.g., 01:05)
# 2: Ensures the number is at least 2 digits wide
# d: Formats the number as a decimal integer
