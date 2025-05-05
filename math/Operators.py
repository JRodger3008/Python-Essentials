# Integer division (floor division) and other basic arithmetic operators

# Floor division returns float if any operand is a float
print(f"12 // 4.5 = {12 // 4.5}")  # 2.0
print(f"2 * 4.5 = {2 * 4.5}")  # 9.0
print(f"12 - 9.0 = {12 - 9.0}")  # 3.0
print(f"12 % 4.5 = {12 % 4.5}")  # 3.0

# Exponentiation (power of)
print(f"\n2 ** 3 = {2 ** 3}") # 8

# Right to left associativity in exponentiation
print(f"2 ** 2 ** 3 = {2 ** 2 ** 3}") # Equivalent to 2 ** (2 ** 3) = 256

# Negative exponentiation
# Python will interpret this as -(3 ** 2) because of exponentiation precedence:
print(f"-3 ** 2 = {-3 ** 2}")  # -9
# To properly evaluate -3 ** 2, use parenthesis:
print(f"(-3) ** 2 = {(-3) ** 2}")

# Integer to float (Type casting) and vise versa
print(f"\nInteger(8) to float: {float(8)}") # 8.0
print(f"Float(8.99998) to integer: {int(8.99998)}") # 8 (rounded down)
# To get around this rounding down behaviour when type casting from float to integer:
print(f"int(round(8.99998)): {int(round(8.99998))}") # 9


# A chain of operations involving modulus, multiplication and floor division
step1 = 25 % 13 # 12
step2 = step1 + 100 # 112
step3 = 2 * 13 # 26
step4 = step2 / step3 # 4.307...
step5 = 5 * step4 # 21.538...
step6 = step5 // 2 # 10.0

print(f"\nAnswer to print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) = {step6}") # 10.0


print(f"\n2 % -4 = {2 % -4}") # -2
print(f"2 // 4 = {2 // 4}") # 0
print(f"-1 * -4 = {-1 * -4}") # 4

print(f"\n-5 % 3 = {-5 % 3}") # 1
print(f"-5 // 3 = {-5 // 3}") # -2
print(f"-2 * 3 = {-2 * 3}") # -6
print(f"2 // -4 = {2 // -4}") # -1

# Absolute value abs() - This is especially useful when calculating distances or magnitude.
print(f"\nAbsolute value of abs(-920): {abs(-920)}") # 920