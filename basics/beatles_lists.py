# 3.4.11 LAB The basics of lists ‒ the Beatles

# This program demonstrates various list methods: append(), del(), and insert().
# It starts with an empty list and adds/removes members of the Beatles band as instructed in LAB.


# step 1: create an empty list named beatles;
beatles = []

# step 2: use the append() method to add the following members of the band to the list:
# John Lennon, Paul McCartney, and George Harrison;
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(f"append() method: {beatles}") # Print list after adding the first three members
print()

# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list:
# Stu Sutcliffe, and Pete Best;
for name in ["Stu Sutcliffe", "Pete Best"]:
    input(f"Press enter to add {name} to list.")
    beatles.append(name)

print()
print(f"After user prompt: {beatles}") # Print list after adding the user-controlled members

# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
del beatles[-2] # Delete second to last member (Stu Sutcliffe)
del beatles[-1] # Delete last member (Pete Best)
print()

print(f"del instruction(s): {beatles}") # Print list after deleting Stu and Pete
print()

# step 5: use the insert() method to add Ringo Starr to the beginning of the list.
beatles.insert(0, "Ringo Starr") # Insert Ringo Starr at the beginning (index 0)

print(f"insert() method: {beatles}") # Print final list with Ringo Starr at position 0
