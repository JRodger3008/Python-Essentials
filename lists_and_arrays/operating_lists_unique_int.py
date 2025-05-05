# 3.6.6 LAB Operating with lists - basics
# Your task is to write a program which removes all the number repetitions from
# the list. The goal is to have a list in which all the numbers appear not more
# than once.

# Note: assume that the source list is hard-coded inside the code ‒ you don't
# have to enter it from the keyboard. Of course, you can improve the code and
# add a part that can carry out a conversation with the user and obtain all
# the data from her/him.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print(f"my_list: {my_list}")

unique_list = []

for number in my_list:
    # Checks if number is not already in unique_list, if not, add to unique_list
    if number not in unique_list:
        unique_list.append(number)

print(f"unique_list: {unique_list}") # [1, 2, 4, 6, 9]
