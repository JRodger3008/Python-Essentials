# This program demonstates the implementation of the Bubble Sort Algorithm.
# The first function sorts the array list in ascending order, the second in descending.
# Both functions display the number of passes (loops) and element swaps.

my_list = [8, 9, 3, 10, 22]
print(f"Original list:             {my_list}")

def ascending_order(array):
    swapped = True # Inititialises swapped flag to enter while loop
    loop_count = 0 # Use these two variables to track the number of loop passes and swaps
    swap_count = 0
    
    while swapped:
        swapped = False # Will be set to True if a swap occurs during this pass
        loop_count += 1

        # Iterate through list and compare adjacent elements
        for i in range(len(array)-1): # len(array)-1 ensures array[i + 1} is always within bounds

            # If array[i] is larger than array[i + 1], swap them using Tuple Unpacking
            if array[i] > array[i + 1]: 
                array[i], array[i + 1] = array[i + 1], array[i]
                swap_count += 1
                swapped = True # A swap occured; continue looping
    print(f"\nBubble sort (Ascending) completed in {loop_count} passes and {swap_count} swaps.")
    return array # Return the sorted list once no further swaps are needed


print(f"Sorted list (Ascending):   {ascending_order(my_list.copy())}")


def descending_order(array):
    swapped = True
    loop_count = 0
    swap_count = 0

    while swapped:
        swapped = False
        loop_count += 1
        for i in range(len(array)-1):
            # The only difference between ascending/descending is the comparison operator
            if array[i] < array[i + 1]: 
                array[i], array[i + 1] = array[i + 1], array[i]
                swap_count += 1
                swapped = True
    print(f"\nBubble sort (Descending) completed in {loop_count} passes and {swap_count} swaps.")
    return array


print(f"Sorted list (Descending):  {descending_order(my_list.copy())}")

print("\nBubble Sort Algorithm execution complete.")

# Instead of using two separate functions with only a minor difference in the comparison operator,
# it is more efficient and maintainable to use one function to sort in ascending order,
# and then reverse the result when a descending order is needed:
# sorted_asc = ascending_order(my_list.copy())
# print(f"Sorted list (Descending): {sorted_asc[::-1]}")

# However, both functions are included here - along with swap and loop counts - to gain a provide a
# clearer understanding of how the Bubble Sort algorithm works.
