# This is a short demonstration for how lists behave:
# The name of scalar variables is the name of its content;
# The name of a list is the name of the memory location where the list is
# stored in the computers memory.

list_1 = [1]
list_2 = list_1 # This copies the name of the array, not its contents
list_1[0] = 2 # Modifying one of the lists affects the other

print(f"list_2 = list_1:    {list_2}") # [2]


list_3 = [1]
list_4 = list_3[:] # Slice which makes a brand new copy of a list, or parts of a list
list_3[0] = 2

print(f"list_4 = list_3[:]: {list_4}") # [1]


# syntax of slicing: my_list[start:end]
# Slicing makes a new (target) list, taking elements from the source list - the
# elements of the indices from start to (end - 1). This is known as a 'half-open' range.
# Thus:
# my_list = ['A', 'B', 'C', 'D', 'E']
# my_list[1:4] will output ['B', 'C', D'] and omit 'E'


# To get around the half-open range, you can leave the :end argument empty:
list_5 = [3, 99, 30, 298, 481]
print(f"\nlist_5:          {list_5}")

list_5_2 = list_5[1:]
print(f"list_5[1:]:      {list_5_2}") # [99, 30, 298, 481]

# Alternatively (though definitely NOT preferred), you can use:

list_5_3 = list_5[1:4+1]
print(f"list_5[1:4+1]:   {list_5_3}") # [99, 30, 298, 481]


# del with slicing
del list_5[1:3] # deletes [99, 30]
print(f"del list_5[1:3]: {list_5}") # [3, 298, 481]

# To delete all elements in a list:
del list_5[:]
print(f"del list_5[:]:   {list_5}") # []

# Note, if you use (del list_5) without [:], it will delete the list itself,
# not its contents. If a print() function invocation is used, it will cause a
# runtime error.


# 'in' and 'not in' operators:

my_list = [7, 9, 12, 3, 10]
print(f"\nmy_list:    {my_list}")
print(f"5 in my_list:     {5 in my_list}") # False
print(f"5 not in my_list: {5 not in my_list}") # True
print(f"12 in my_list:    {12 in my_list}") # True
