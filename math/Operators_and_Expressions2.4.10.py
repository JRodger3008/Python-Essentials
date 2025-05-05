# 2.4.10 LAB - Operators and Expressions
# This program evaluates the polynomial: 3x^3 - 2x^2 + 3x - 1
print("Initial equasion: 3x^3 - 2x^2 + 3x - 1")
print()

# x is reassigned 3 times to return y for each instance
x = 0
# x value converted to float
x = float(x)
print("x =", x) # 0.0

# initial equasion
y = ((3 * (x**3)) - (2 * (x**2)) + (3 * x) - 1)
print("y =", y) # -1.0
print()

x = 1
x = float(x)
print("x =", x) # 1.0
y = ((3 * (x**3)) - (2 * (x**2)) + (3 * x) - 1)
print("y =", y) # 3.0
print()

x = -1
x = float(x)
print("x =", x) # -1.0
y = ((3 * (x**3)) - (2 * (x**2)) + (3 * x) - 1)
print("y =", y) # -9.0
