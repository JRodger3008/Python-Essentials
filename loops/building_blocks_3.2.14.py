# Pyramid Layer Calculator 3.2.14 LAB

# This program calculates how many full layers of a pyramid can be built
# using a given number of blocks. Each layer contains one more block than the one above.

# The user inputs the total number of available blocks.
# The program returns the maximum number of complete layers that can be built.
# Any leftover blocks that aren't enough to complete the next layer are ignored.
# It then prints the pyramid using very simple ASCII-art.

blocks = int(input("Please input the number of blocks: "))

height = 0

# Calculate the number of complete layers using the formula for the
# sum of the first n natural numbers: n(n + 1)/2
while True:
    total_blocks_required = (height + 1) * (height + 2) // 2 
    if total_blocks_required > blocks: # # If the total exceeds the available blocks, break the loop
        break
    height += 1 # Increase height if there are enough blocks for the current layer

print(f"The height of the pyramid is: {height}")

print("Here is your pyramid:\n")

# Draw the pyramid with '*', and center the blocks for symmetry
for i in range(1, height + 1):
    spaces = ' ' * (height - i) # Number of spaces before the '*' to center the pyramid
    layer_blocks = '*' * (2 * i - 1) # Generate an odd number of stars for a symmetrical pyramid shape
    print(spaces + layer_blocks)
