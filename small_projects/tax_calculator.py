# 3.1.11 LAB - Essentials of the if-else statement.

# The following is a breakdown of the conditions:
# 1. If the person's income was not higher than 85,528 thalers, the tax was equal to 18% of the income 
# minus 556 thalers and 2 cents.
# 2. If the person's income was higher than this amount, the tax was equal to
# 14,839 thalers and 2 cents, plus 32% of the surplus above 85,528 thalers.

# This program should accept one floating-point value: the income.
# The tax should be rounded to full thalers.

income = float(input("Please enter the annual income: "))

# If income is less than 85,528 thalers calculate tax at 18% minus 556.02 thalers
if income < 85528:
    tax = income * 0.18 - 556.02
else:
    # If income exceeds 85,528 thalers, base tax is 14,839.02 thalers,
    # plus 32% of the surplus above 85,528 thalers.
    tax = (14839.02) + (income - 85528) * 0.32

# Ensure tax isn't negative
if tax < 0.0:
    tax = 0.0
    
# Round tax to the nearest full thaler (integer)
tax = round(tax)

# Print calculated tax
print(f"The tax is: {tax} thalers")
