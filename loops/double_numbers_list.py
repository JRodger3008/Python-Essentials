# Double each number in a list to make:
# [4, 8, 12, 16, 20]

numbers = [2, 4, 6, 8, 10]

numbers_2 = []

for i in range(len(numbers)):
    numbers_2.append(numbers[i] * 2) # Double each number and add to the new list
    
print(numbers)
print(numbers_2)


# Cleaner version
numbers_3 = [number * 2 for number in numbers]

print(numbers_3)
