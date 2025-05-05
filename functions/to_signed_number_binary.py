# This function converts an unsigned binary number to a signed (two's complement) number.
# MSB = Most Significant Bit.

# Parameters:
# n (int): The unsigned integer.
# bits (int): The number of bits representing the number.
def to_signed(n, bits):
    # This checks if the number is negative in two's complement (i.e., MSB is set)
    if n & (1 << (bits - 1)):
        # If MSB is set, convert to signed value by subtracting 2^bits
        return n - (1 << bits) # 1 << bits = 2^bits (256), so 251 - 256 = -5
    return n

# Test 1: MSB Set (interpreted as -5)
print(f"Unsigned (0b11111011): {0b11111011}") # 251 (Unsigned)
print(f"Signed (0b11111011): {to_signed(0b11111011, 8)}")  # -5 (Signed)

# Test 2: MSB Set (interpreted as -123)
print(f"Unsigned (0b10000101): {0b10000101}") # 133 (Unsigned)
print(f"Signed (0b10000101): {to_signed(0b10000101, 8)}") # -123 (Signed)
