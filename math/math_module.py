# This is just some experimentation and research into the Python math module, and its functionalities.
# Many of the results you will see will exhibit floating-point errors, which is expected when working
# with irrational numbers (π, τ, and e) and equations utilising them (Trigonometric functions).
# To improve readability, some results are rounded using the round() function.

import math

# ======== CONSTANTS ========
print("\n======== CONSTANTS ========")
# The following constants have been rounded to 6 decimal places.

# Pi is widely used in Trigonometry, Geometry, Game Development, signal/audio processing, 
# and Machine Learning (e.g Gaussian functions).
print(f"Pi (π): {round(math.pi, 6)}") # 3.141593

# Tau (τ) is the ratio of a circles circumference to its radius (2π), and is also the 
# number of radians in a full circle.
print(f"Tau (τ): {round(math.tau, 6)}") # 6.283185

# Euler's number (e) is used in natural logarithms, exponential growth/decay calculations.
# It's particularly relevant in fields like Machine Learning, Neural Networks, and Cryptography
print(f"Euler's number (e): {round(math.e, 6)}") # 2.718282



# ======== LOGARITHMS AND EXPONENTIATION ========
print("\n======== LOGARITHMS AND EXPONENTIATION ========")
# Natural logarithm (log base e)
print(f"ln(e) (natural logarithm): {math.log(math.e)}") # 1.0

# Logarithm base 2 of 1024 (very useful for binary calculations)
print(f"Log₂(1024): {math.log2(1024)}") # 10.0

# Logarithm base 10 of 900
print(f"Log₁₀(900): {math.log10(900)}") # 2.954...

# Logarithm of 81 with base 3
print(f"log₃(81): {math.log(81, 3)}")  # 4.0

# Exponentiation with base e
print(f"exp(2): {math.exp(2)}") # 7.389...



# ======== ROUNDING AND NUMBER MANIPULATION ========
print("\n======== ROUNDING AND NUMBER MANIPULATION ========")

# Absolute value of float (8.9)
print(f"Absolute value of -8.9: {math.fabs(-8.9)}") # 8.9

# Power (Equivalent to ** operator)
print(f"math.pow(6, 9): {math.pow(6, 9)}") # 10077696.0

# Square root (Equivalent to ** 0.5)
print(f"math.sqrt(36): {math.sqrt(36)}") # 6.0

# Rounding down to nearest integer
print(f"math.floor(30.8): {math.floor(30.8)}") # 30

# Rounding up to nearest integer
print(f"math.ceil(30.8): {math.ceil(30.8)}") # 31

# Factorials, combinations and permutations are primarily used in statistics, probability and combinatorics.
# Note that factorials over ~20-30 become impractical and can impact performance and memory usage.
# 9 Factorial = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
print(f"Factorial of 9: {math.factorial(9)}") # 362880 (9!)

# This evaluates how many unordered combinations are in a set.
# Combination: How many ways can you pick 2 items from a set of 8, where order doesn't matter?
print(f"Combination (8 choose 2): {math.comb(8, 2)}") # 28

# In contrast, permutations count the number of ordered arrangements in a set.
# Permutations: how many ways can you arrange 2 items from a set of 8, where the order matters?
print(f"Permutations (8 P 2): {math.perm(8, 2)}") # 56



# ======== TRIGONOMETRIC FUNCTIONS ========
print("\n======== TRIGONOMETRIC FUNCTIONS ========")
# Note that these functions accept radians as the argument, not degrees

# Converting Degrees to Radians
# Incredibly simple, yet reusable function to convert from degrees to radians,
# the inverse conversion function (radians_to_degrees) follows the same logic.
def degrees_to_radians(degrees):
    return math.radians(degrees)

angle_degree_60 = 60
angle_radian_60 = degrees_to_radians(angle_degree_60)
# angle_radian = math.radians(angle_degree) # Converts 60° to radians
print(f"sin(60°): {round(math.sin(angle_radian_60), 6)}") # 0.866025


# Converting Radians to Degrees
def radians_to_degrees(radians):
    return math.degrees(radians)
radians_value = math.tau / 12 # 0.523... radians
degrees_value = radians_to_degrees(radians_value) # ≈ 29.999...°
print(f"{round(radians_value, 6)} radians = {round(degrees_value, 6)}°") # 0.523599 radians = 30.0°


# --- Sine (sin) and Cosine (cos) periodicity and demonstration of floating-point errors ---
print("--- Sine (sin) and Cosine (cos) periodicity ---")
angle_rad = math.pi

# Sine (sin) - The following are great examples of floating-point errors.
# This is because computers represent decimal numbers in binary, which often leads to small precision inaccuracies
# when handling irrational or fractional numbers.
# For example 0.1 cannot be exactly represented in binary, instead it is stored internally as something like 0.10000000000000000555.
print(f"sin(π) = {math.sin(angle_rad)} | Rounded result: {round(math.sin(angle_rad), 6)}") # 1.2246467991473532e-16 | Rounded: 0.0
print(f"sin(2π) = {math.sin(angle_rad * 2)} | Rounded result: {round(math.sin(angle_rad * 2), 6)}") # -2.4492935982947064e-16 | Rounded: -0.0
print(f"sin(3π) = {math.sin(angle_rad * 3)} | Rounded result: {round(math.sin(angle_rad * 3), 6)}") # 3.6739403974420594e-16 | Rounded: 0.0
print()

# Cosine has a very interesting application in programming and computer science:
# Discrete Cosine Transform (DCT) is used for data compression, as well as image and audio processing.
print(f"cos(π/2) = {math.cos(angle_rad / 2)} | Rounded result: {round(math.cos(angle_rad / 2), 6)}") # 6.1232...e-17 | Rounded: 0.0
print(f"cos(π) = {math.cos(angle_rad)} | Rounded result: {round(math.cos(angle_rad), 6)}") # -1.0
print(f"cos(2π) = {math.cos(angle_rad * 2)} | Rounded result: {round(math.cos(angle_rad * 2))}") # 1.0
print()

print(f"tan(π/4) = {math.tan(math.pi / 4)} | Rounded result: {round(math.tan(math.pi / 4), 6)}") # 0.9999... | Rounded: 1.0

print(f"sin(π/2) = {math.sin(angle_rad / 2)}") # 1.0

# Cosine (cos) using degrees
angle_degree_100 = 100
angle_radian_100 = degrees_to_radians(angle_degree_100) # ≈ 1.745 radians
print(f"math.cos(100°): {round(math.cos(angle_radian_100), 6)}") # 0.862319

angle_degree_30 = 30
angle_radian_30 = degrees_to_radians(angle_degree_30)
print(f"math.sin(30°): {round(math.sin(angle_radian_30), 6)}") # 0.5

# Edge cases (sin and cos with large and negative angles)
# sin(4τ) is effectively sin(0) due to periodicity, and effectively evaluates as = 0
# Periodicity also produces the characteristic sine wave behaviour, periodically oscillating.
print(f"sin(4τ): {math.sin(math.tau * 4)}") # -9.797174393178826e-16 (floating-point precision error)

# cos(-π) is the same as cos(π), which equals -1.0
print(f"cos(-π): {math.cos(-math.pi)}") # -1.0