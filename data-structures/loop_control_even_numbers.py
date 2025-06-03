# Write a program that removes all the odd numbers and returns a new list with
# only the even ones.

input_list = [5, 12, 7, 8, 3, 10]

even_list = []

for number in input_list:
    if number % 2 == 0: # Check if number is even
        even_list.append(number) # If even, add to even_list

print(f"even_list: {even_list}")


# Write a program that removes all even numbers from a list in place.
# That means modifying the original list instead of creating a new one.

# Notice -1,-1,-1: this means start at the end of the list, move backwards by one
# each time, and finally, stop at index 0.
for i in range(len(input_list)-1, -1, -1): # Iterate backwards 
    if input_list[i] % 2 == 0: # Check if number is even
        del input_list[i] # Delete even numbers

print(f"input_list (removed even numbers): {input_list}")
