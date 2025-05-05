# LAB 3.4.6 - Hat List
# This program changes a list by inserting a user-inputted integer, and deleting the last element
# The steps can be seen below:


hat_list = [1, 2, 3, 4, 5]
print(f"Initial hat_list:        {hat_list}")
print()

# Step 1: Replace the middle number in the list with an integer number entered by user
user_input = int(input("Please input a number: "))
hat_list[2] = user_input # Replace element at index 2 with user-input (3 -> user_input)
print(f"hat_list[2] = user_input:{hat_list}") # [1, 2, user_input, 4, 5]

# Step 2: Remove the last element from the list
del hat_list[-1] # Uses negative indexing [-1] to delete the last element in list
print(f"del hat_list[-1]:        {hat_list}") # [1, 2, user_input, 4]
print()

# Step 3: Print the length of the existing list
print(f"List Length: {len(hat_list)}") # 4
