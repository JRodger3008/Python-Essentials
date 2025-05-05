# Half of this script was written early in my learning - the additions can be recognised by f-strings.

# This script demonstrates Python type casting between str, int, float, and bool types,
# using various examples and formatted print statements for clarity.

n = "2" # String representation of number
six_value = 6 # An integer value
x = int(n) # Convert the string "2" to integer using type casting (x = 2)

# Print data types of n (string) and x (integer)
print("n data type: ", type(n)) # <class 'str'>
print("x data type: ", type(x)) # <class 'int'>

# Perform addition of x (2) and n_six (6)
oper = x + six_value 
print("x(2) + n_six(6) =", oper) # 8
print()

# Define an integer and a float
integer_number = 140 # Integer value
float_number = 12.889 # Float value

# Add the integer and float together
new_number = integer_number + float_number

# Print data types and sum of the integer and float
print("integer_number (140) data type: ", type(integer_number)) # <class 'int'>
print("Sum of integer_number (140) + float_number (12.889) = ", new_number) # 152.889
print("new_number (152.889) data type: ", type(new_number)) # <class 'float'>
print()

# Float to integer type-casting
float_val = 19.93
int_val = int(float_val) # This will round down to nearest whole integer
print(f"float_val = {float_val} | {type(float_val)}") # 19.93 | <class 'float'>
print(f"int_val = {int_val} | {type(int_val)}") # 19 | <class 'int'>
print()

# Integer to string type-casting
num = 123
str_num = str(num)
print(f"num = {num} | {type(num)}") # 123 | <class 'int'>
print(f"str_num = {str_num} | {type(str_num)}") # 123 | <class 'str'
print()

# String to float type-casting
num_str = "3.14"
num_float = float(num_str)
print(f"num_str = {num_str} | {type(num_str)}") # 3.14 | <class 'str'>
print(f"num_float = {num_float} | {type(num_float)}") # 3.14 | <class 'float'>
print()

# Boolean to integer type-casting
bool_val = True
int_from_bool = int(bool_val)
print(f"bool_val = {bool_val} | {type(bool_val)}") # True | <class 'bool'>
print(f"int_from_bool {int_from_bool} | {type(int_from_bool)}") # 1 | <class 'int'>
print()

# Boolean values from zero and non-zero variables
num_zero = 0
num_nonzero = 7
print(f"bool({num_zero}) = {bool(num_zero)}") # bool(0) = False
print(f"bool({num_nonzero}) = {bool(num_nonzero)}") # bool(7) = True
print()

# Float to string type-casting
flt = 8.239
str_flt = str(flt)
print(f"flt = {flt} | {type(flt)}") # 8.239 | <class 'float'>
print(f"str_flt = {str_flt} | {type(str_flt)}") # 8.239 | <class 'str'>
print()

# Sting to boolean (non-empty = True)
empty_str = ""
non_empty_str = "Hello"
print(f"bool({empty_str}) = {bool(empty_str)}") # bool() = False
print(f"bool({non_empty_str}) = {bool(non_empty_str)}") # bool(Hello) = True