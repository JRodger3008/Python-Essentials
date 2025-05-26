"""
Find the Area of a Triangle Using Heron's Formula.

Heron's Formula: A = √s(s - a)(s - b)(s - c)
Where:
    s is the semi-perimeter -> s = (a + b + c) / 2
    a, b, and c are the lengths of the triangles sides

Author: Jordan Rodger
Date: 11/05/2025 (Last Edit: 26/05/2025)
"""


# Function to determine if three sides can form a valid triangle
def is_a_triangle(a, b, c):
    """Returns True if the sides satisfy the triangle inequality theorem 
    (i.e., can form a triangle), otherwise returns False."""
    return a + b > c and b + c > a and c + a > b


# Function to determine the area of a triangle
def heron(a, b, c):
    """
    Calculates the area of a triangle using Heron's Formula.
    Assumes inputs form a valid triangle.

    Parameters: 
        Sides length a, b, and c (float) of a triangle.
    Returns:
        float: Area of a triangle (in square units e.g., m², cm², in²)."""
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


# Uses heron() and is_triangle() to return area of triangle
def area_of_triangle(a, b, c):
    """Determines area of a valid triangle; otherwise, returns None."""
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(f"area_of_triangle(7, 8, 9): {round(area_of_triangle(7, 8, 9), 4)}") # 26.8328
print(f"area_of_triangle(9, 22, 9): {area_of_triangle(9, 22, 9)}") # None (Invalid Triangle)