"""
Bitwise Operations with Simulated Flag Registers.

This program demonstrates how to use bitwise operations to manipulate specific
bits in 8-bit unsigned integers (values from 0 to 255) using bitmasks.
It began as a personal exploration and evolved into something I hope is educational.

Bitwise operators used:
    - |  (OR):    Set specific bits.
    - &  (AND):   Check or clear specific bits.
    - ~  (NOT):   Invert bits (used with AND to clear bits).
    - ^  (XOR):   Toggle bits; swap values without a temporary variable.
    - << (SHIFT): Define bitmasks using bitwise left shift.

Features:
    - Setting, clearing, and toggling individual bits using bitwise operators.
    - A bit toggle loop that iteratively toggles each bit.
    - The XOR Swap Algorithm (low-level approach), and a high-level alternative using tuple unpacking.

Author: Jordan Rodger
Date: 26/05/2025
"""

# This program demonstrates the use of bitwise operations 
# to manipulate specific bits in a flag register using bitmasks.


# ====== Bitmask Definitions ======
# Bitmasks are defined using left shift for reusability and clarity
MASK_0 = 1 << 0 # -> 0b00000001
MASK_1 = 1 << 1 # -> 0b00000010
MASK_2 = 1 << 2 # -> 0b00000100
MASK_3 = 1 << 3 # -> 0b00001000
MASK_4 = 1 << 4 # -> 0b00010000
MASK_5 = 1 << 5 # -> 0b00100000
MASK_6 = 1 << 6 # -> 0b01000000
MASK_7 = 1 << 7 # -> 0b10000000 (Included for completeness and for future use; unused)



# ====== Example 1: Setting (|) and Clearing (& with ~) Bits ======
print("All values in the output will be formatted as: 8-bit binary (int).\n"
      "All values stay within the 0-255 range to conform to 8-bit unsigned (non-negative) integers.\n")

print("====== Example 1: Setting and Clearing Bits ======")
flag_register = 0b01011010  # Decimal: 90

# Notice :08b in the following formatted string:
# 'b' formats the number as binary
# '8' ensures the output is 8 characters wide (8-bit)
# '0' pads with leading 0s if the number has fewer than 8 bits
print(f"Initial flag_register value:   {flag_register:08b} ({flag_register})") 
# 01011010 (90)

# Sets bit 2 and 3 using bitwise OR
flag_register |= (MASK_2 | MASK_3) 
print(f"After setting bits 2 and 3:    {flag_register:08b} ({flag_register})")
# 01011110 (94)

# Clear bit 1 using bitwise AND with inverted mask
flag_register &= ~(MASK_1)
print(f"After clearing bit 1:          {flag_register:08b} ({flag_register}) \n")
# 01011100 (92)



# ====== Example 2: Clearing a Bit (& with ~) in Another Flag Register ======
print("====== Example 2: Clearing a Bit in Another Flag Register ======")
flag_register_2 = 0b11011110 # Decimal: 222
print(f"Initial flag_register_2 value: {flag_register_2:08b} ({flag_register_2})")
# 11011110 (222)

# Clear bit 4
flag_register_2 &= ~(MASK_4) 

print(f"After clearing bit 4:          {flag_register_2:08b} ({flag_register_2}) \n")
# 11001110 (206)



# ====== Example 3: Toggling a Bit using XOR (eXclusive OR ^) ======
print("====== Example 3: Toggling a Bit using XOR (eXclusive OR) ======")
flag_register_3 = 0b10101010 # Decimal: 170
print(f"Initial flag_register_3 value: {flag_register_3:08b} ({flag_register_3})")
# 10101010 (170)

# Toggle bit 6 using XOR (adds 64 if bit 6 was originally 0; removes 64 if it was 1)
flag_register_3 ^= MASK_6 

print(f"After toggling bit 6:          {flag_register_3:08b} ({flag_register_3}) \n")
# 11101010 (234)



# ====== Example 4: Set (|), Clear (& with ~), and Check (&) Specific Bits ======
print("====== Example 4: Set, Clear, and Check Specific Bits ======")
flag_register_4 = 0b10110110 # Decimal: 182
print(f"Initial flag_register_4 value: {flag_register_4:08b} ({flag_register_4})")
# 10110110 (182)

# Set bit 0
flag_register_4 |= MASK_0 
print(f"After setting bit 0:           {flag_register_4:08b} ({flag_register_4})")
# 10110111 (183)

# Clear bit 5
flag_register_4 &= ~(MASK_5) 
print(f"After clearing bit 5:          {flag_register_4:08b} ({flag_register_4})")
# 10010111 (151)

# Checks if bit 6 is set (ON)
if flag_register_4 & MASK_6:
    print("Bit 6 is ON")
else:
    print("Bit 6 is NOT ON")
# Bit 6 is NOT ON


# ====== BIT TOGGLE LOOP ======
print("====== BIT TOGGLE LOOP ======")
toggle_test = 0b00000000
print(f"Start: 0b{toggle_test:08b}")

# Turning all bits ON using XOR (flips bits; running this again would flip bits OFF)
for i in range(8):
    toggle_test ^= (1 << i)
    print(f"After toggling bit {i}: 0b{toggle_test:08b}")

print()

# Turning bits OFF one by one using AND with inverted mask (forces bit i to 0)
for i in range(8):
    toggle_test &= ~(1 << i) # Forces bit i to 0
    print(f"After clearing bit {i} OFF: 0b{toggle_test:08b}")


# ====== XOR Swapping: Low-Level Approach ======
print("\n====== XOR Swapping ======")

# Initial values
a = 20 # 0b00010100
b = 2  # 0b00000010
print(f"Before XOR swap:    a = {a:08b} ({a}) ; b = {b:08b} ({b})")

# XOR Swap Algorithm — swaps values of two variables without using a temp variable.
# This technique is useful in low-level programming (e.g., C, assembly) under strict memory constraints.
a = a ^ b # a = 20 ^ 2 = 22
b = a ^ b # b = 22 ^ 2 = 20 (original a)
a = a ^ b # a = 22 ^ 20 = 2 (original b)
print(f"XOR Swap Algorithm; a = {a:08b} ({a}) ; b = {b:08b} ({b})")

# Note: The XOR swap assumes a and b are distinct values in memory.
# If they're not (e.g., a = 1 ; b = a), there is a significant risk of data loss
# or at the very least, meaningless results.


# ====== Pythonic Tuple Unpacking: High-Level Approach ======

# Reset values
c = 20
d = 2
print(f"\nBefore tuple unpacking: c = {c:08b} ({c}) ; d = {d:08b} ({d})")

# Idiomatic and Pythonic way to swap values
c, d = d, c 
print(f"After tuple unpacking:  c = {c:08b} ({c}) ; d = {d:08b} ({d})") # c = 2 ; d = 20

# This is a far more readable, concise, and Pythonic approach,
# and is preferred in high-level programming environments.

print("\nAll operations executed successfully")