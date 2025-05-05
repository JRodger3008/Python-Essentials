# This program demonstrates the use of bitwise operations 
# to manipulate specific bits in a flag register using bitmasks.


# --- Bitmask Definitions ---
# Bitmasks are defined using left shift for reusability and clarity
MASK_0 = 1 << 0 # -> 0b00000001
MASK_1 = 1 << 1 # -> 0b00000010
MASK_2 = 1 << 2 # -> 0b00000100
MASK_3 = 1 << 3 # -> 0b00001000
MASK_4 = 1 << 4 # -> 0b00010000
MASK_5 = 1 << 5 # -> 0b00100000
MASK_6 = 1 << 6 # -> 0b01000000



# --- Example 1: Setting (|) and Clearing (& with ~) Bits ---
print("All values will be output as: 8-bit binary (int). \nThese values will be under 255 to conform to unsigned 8-bit numbers \n")

print("--- Example 1: Setting and Clearing Bits ---")
flag_register = 0b01011010  # Decimal: 90
# Notice :08b in the following formatted string
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



# --- Example 2: Clearing a Bit (& with ~) in Another Flag Register ---
print("--- Example 2: Clearing a Bit in Another Flag Register ---")
flag_register_2 = 0b11011110 # Decimal: 222
print(f"Initial flag_register_2 value: {flag_register_2:08b} ({flag_register_2})")
# 11011110 (222)

# Clear bit 4
flag_register_2 &= ~(MASK_4) 

print(f"After clearing bit 4:          {flag_register_2:08b} ({flag_register_2}) \n")
# 11001110 (206)



# --- Example 3: Toggling a Bit using XOR (eXclusive OR ^) ---
print("--- Example 3: Toggling a Bit using XOR (eXclusive OR) ---")
flag_register_3 = 0b10101010 # Decimal: 170
print(f"Initial flag_register_3 value: {flag_register_3:08b} ({flag_register_3})")
# 10101010 (170)

# Toggles bit 6 using XOR, adding 64 to int value
flag_register_3 ^= MASK_6 

print(f"After toggling bit 6:          {flag_register_3:08b} ({flag_register_3}) \n")
# 11101010 (234)



# --- Example 4: Set (|), Clear (& with ~), and Check (&) Specific Bits ---
print("--- Example 4: Set, Clear, and Check Specific Bits ---")
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

# Checks if bit 6 is ON
if flag_register_4 & MASK_6:
    print("Bit 6 is ON")
else:
    print("Bit 6 is NOT ON")
# Bit 6 is NOT ON

print("\nAll operations executed successfully")



