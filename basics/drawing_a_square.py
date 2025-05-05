# A very basic program that uses ASCII characters and print() functions to draw a hollow square

# Set width and height variables so the square size can be easily changed
width = 10
height = 5

print("+" + width * "-" + "+")
print(("|" + " " * width + "|\n") * height , end="")
print("+" + width * "-" + "+")
