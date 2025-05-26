"""
Triangle Classification Tool

This program evaluates whether three given sides can form a valid triangle, using
the Triangle Inequality Theorem. If the triangle is valid, classifies it based on:
    - Side lengths: Equilateral, Isosceles, or Scalene
    - Angles: Acute, Right-angled, or Obtuse

Key features:
    - Uses floating-point tolerant comparison (math.isclose()) to accurately detect
      Right-angled Isosceles triangle.
    - Includes test cases for valid and invalid triangles, including edge cases.
    - Highlights how floating-point precision errors can affect geometric calculations.

Author: Jordan Rodger
Date: 12/05/2025 (Last Edit: 26/05/2025)
"""

import math # For math.isclose()


def is_a_triangle(a: float, b: float, c: float) -> bool:
    """Determines if a triangle is valid using Triangle Inequality Theorem."""
    return a + b > c and b + c > a and c + a > b


def triangle_classification(a: float, b: float, c: float) -> str:
    """
    Classifies a triangle based on its side lengths and angles.

    Params:
        a, b, c (float): Lengths of the three sides of the triangle.
    Returns:
        str: A string describing the triangle type (e.g., "Right-Angled Isosceles Triangle")
             or "Invalid Triangle" if the sides do not form a valid triangle.
    """
    if not is_a_triangle(a, b, c):
        return "Invalid Triangle"
    
    # Side classification
    if a == b == c:
        side_type = "Equilateral"
    elif a == b or b == c or c == a:
        side_type = "Isosceles"
    else:
        side_type = "Scalene"

    # Angle classification
    sides = sorted([a, b, c]) # Sorts sides in ascending order
    a2, b2, c2 = sides[0] ** 2, sides[1] ** 2, sides[2] ** 2 # Example of unpacking

    # Use math.isclose() to handle floating-point errors (e.g., Right-angled Isosceles)
    if math.isclose(c2, a2 + b2, rel_tol=1e-9):
        angle_type = "Right-angled"
    elif c2 < a2 + b2:
        angle_type = "Acute"
    else:
        angle_type = "Obtuse"
    
    return f"{angle_type} {side_type} Triangle"


# Test cases
print(f"Sides (4, 4, 4): {triangle_classification(4, 4, 4)}") # Acute Equilateral Triangle
print(f"Sides (6, 6, 9): {triangle_classification(6, 6, 9)}") # Obtuse Isosceles Triangle
print(f"Sides (4, 5, 6): {triangle_classification(4, 5, 6)}") # Acute Scalene Triangle
print(f"Sides (3, 4, 5): {triangle_classification(3, 4, 5)}") # Right-angled Scalene Triangle
print()
print(f"Sides (90, 12, 10): {triangle_classification(90, 12, 10)}") # Invalid Triangle
print(f"Sides (-1, 8, -2): {triangle_classification(-1, 8, -2)}") # Invalid Triangle
print()

# Right-Angled Isosceles triangle: hypotenuse = √2 * a
# hyp = √2 * 5 = 7.071067811865475

# Without math.isclose, the following would evaluate as an Acute Isosceles Triangle, 
# due to floating-point precision error.
print(f"Sides (5, 5, 7.071067811865475): {triangle_classification(5, 5, 7.071067811865475)}") 
# Right-angled Isosceles Triangle