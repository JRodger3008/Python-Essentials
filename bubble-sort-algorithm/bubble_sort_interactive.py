# This program demonstrates Bubble Sort by sorting a list of user-entered numbers
# in ascending order.

my_list = []

num = int(input("How many elements do you want to sort: "))

# Prompts user to add numeric (float) elements to empty array via .append()
for i in range(num): # Loop runs 'num' times, determined by user
    val = float(input(f"Please enter value #{i+1}: "))
    my_list.append(val) # Add value(s) to list

# Display original unsorted list
print(f"\nOriginal list: {my_list}")

# Function to sort a list in ascending order using Bubble Sort Algorithm
def ascending_order(array):
    swapped = True # Flag to control while loop

    # Continue looping until no swaps occur
    while swapped:
        swapped = False # Reset flag at the start of each pass

        # Compare adjacent elements in the list, and swap as required
        for i in range(len(array)-1):
            if array[i] > array[i + 1]:
                # Swap using tuple unpacking
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True # Swap occured, continue to next loop iteration
    return array # Return sorted list

print(f"Sorted list:      {ascending_order(my_list.copy())}")
