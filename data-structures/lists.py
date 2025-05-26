# This is purely my own experimentation with lists


numbers = [60, 80, 33, 49, 799]

print(f"Initial list (numbers):  {numbers}") # [60, 80, 33, 49, 799]

numbers[0] = 233 # Overwrites 60 with 233

print(f"number[0] = 233:         {numbers}") # [233, 80, 33, 49, 799]

numbers[1] = numbers[4] # Index position 4 to copy 799 to position 1

print(f"numbers[1] = numbers[4]: {numbers}") # [233, 799, 33, 49, 799]
print(f"numbers[3]:  {numbers[3]}") # 49
print(f"List length: {len(numbers)}") # 5

del numbers[4]

print(f"del(numbers[4]):         {numbers}") # [233, 799, 33, 49]
print(f"New list length: {len(numbers)}") # 4

# numbers[4] = 1 IndexError: list assignment index out of range
# print(numbers[4]) will cause a runtime error

print(f"numbers[-1] and numbers[-2]: {numbers[-1], numbers[-2]}") # (49, 33)

# print(numbers[-5]) IndexError

numbers.append(3) # This will add 3 to the end of the list
print(f"numbers.append(3):       {numbers}") # [233, 799, 33, 49, 3]

numbers.insert(0, 99) # Insert 99 at position 0
# Notice how it shifts all numbers following position 0 to the right when
# 99 is inserted at the first element
print(f"numbers.insert(0, 99):   {numbers}") # [99, 233, 799, 33, 49, 3]
print()
print()



# --- APPEND AND INSERT WITH LOOPS --- 
my_list = []
my_list_2 = []

print("--- APPEND AND INSERT WITH LOOPS ---")

# Append example
for i in range(10):
    my_list.append(i + 1) # Appends numbers 1 through 10 sequentially

print(f"my_list.append: {my_list}") # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Insert example
for i in range(10):
    my_list_2.insert(0, i + 1) # Reversing order by always inserting at index[0]

print(f"my_list_2.insert: {my_list_2}") # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print()



# --- INSERTING AT SPECIFIC POSITIONS ---
print("--- INSERTING AT SPECIFIC POSITIONS ---")
my_list_3 = []

for i in range(10):
    my_list_3.insert(3, i + 2)

print(f"my_list3.insert(3, i + 2): {my_list_3}") # [2, 3, 4, 11, 10, 9, 8, 7, 6, 5]
# The first 3 inserts(3, ...) calls act like append() because the list is too
# short. From the 4th insertion onward, values are inserted at index 3, pushing
# everything after it one position to the right.

# So the list ends up with the first 3 values in order, and the rest are
# inserted in reverse order just after index 2.



my_list_4 = []

for i in range(5):
    my_list_4.insert(i, i * 2) # Insert i * 2 at index[i]

print(f"my_list_4.insert(i, i * 2): {my_list_4}") # [0, 2, 4, 6, 8]

my_list_5 = []

for i in range(5):
    my_list_5.insert(1, i) # Always insert at index[1]

print(f"my_list_5.insert(1, i): {my_list_5}") # [0, 4, 3, 2, 1]
print()



# --- SUMMING ELEMENTS IN LISTS ---
print("--- SUMMING ELEMENTS IN LISTS ---")
my_list_6 = [10, 1, 8, 3, 5]
print(f"my_list_6: {my_list_6}")
total = 0

for i in range(len(my_list_6)): # Loops through my_list_6 indices (5)
    total += my_list_6[i] # Adds each element at index[i] to total
print(f"Total of my_list_6: {total}") # 27
print()



# --- SUMMING EVEN ELEMENTS ---
print("--- SUMMING EVEN ELEMENTS ---")
my_list_7 = [4, 9, 5, 6, 10]
print(f"my_list_7: {my_list_7}")

total_2 = 0

for i in my_list_7:
    if i % 2 == 0: # Checks if number is even
        total_2 += i # If even, adds to total_2

print(f"Total even numbers of my_list_7 {total_2}") # 20
print()



# --- SUMMING SPECIFIC ELEMENTS BASED ON CONDITIONAL STATEMENTS ---
print("--- SUMMING SPECIFIC ELEMENTS BASED ON CONDITIONAL STATEMENTS --- ")

my_list_8 = [12, 5, 8, 7, 3, 10, 1]
print(f"my_list_8: {my_list_8}")
total_3 = 0

# Checks if i is even, and if my_list_8 elements are odd - adds these elements together
for i in range(len(my_list_8)):
    if i % 2 == 0 and my_list_8[i] % 2 != 0: 
        total_3 += my_list_8[i]

print(f"Total my_list_8, if i is even and my_list_8 element is odd: {total_3}") # 4
print()



# --- SWAPPING ELEMENTS ---
print("--- SWAPPING ELEMENTS ---")
my_list_9 = [7, 9, 30, 65, 21]
print(f"my_list_9:                  {my_list_9}")

# Swap first and last elements
my_list_9[0], my_list_9[-1] = my_list_9[-1], my_list_9[0]
print(f"my_list_9 0 and -1 swapped: {my_list_9}") # [21, 9, 30, 65, 7]

# Swap second and second-last elements
my_list_9[1], my_list_9[3] = my_list_9[3], my_list_9[1]
print(f"my_list_9 1 and 3 swapped:  {my_list_9}") # [21, 65, 30, 9, 7]
print()



# --- SWAPPING ELEMENTS WITH LOOP ---

# This is a way of manually swapping the first with last, second with penultimate,
# etc. without altering the element in the centre of the list.

# It can be used with both even and odd-length lists.
my_list_10 = [8, 6, 2, 5, 9]
print(f"my_list_10: {my_list_10}")

for i in range(len(my_list_10) // 2):
    my_list_10[i], my_list_10[len(my_list_10) - i - 1] = my_list_10[len(my_list_10) - i - 1], my_list_10[i]

print(f"my_list_10 swaps: {my_list_10}")
