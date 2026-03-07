# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 90 - Rectangle class

"""
Write a class Rectangle that has two attributes: width (in cm) and
length (in cm).

The Rectangle class should contain the following methods:
    - Perimeter(self) which calculates the perimeter of the rectangle.
    - Area(self) which calculates the area of the rectangle.

Verification tests:
>> rectangle1 = Rectangle(10, 15)
>> rectangle1.width
10
>> rectangle1.length
15
>> rectangle1.Perimeter()
50
>> rectangle1.Area()
150
"""


class Rectangle:
    def __init__(self, width, length):
        self.width = float(width)
        self.length = float(length)

    def Perimeter(self):
        return 2 * (self.width + self.length)

    def Area(self):
        return self.width * self.length


# -------------------- TEACHING NOTES --------------------
# Topic: Modeling Shapes with Classes
#
# 1. Why use a class?
#    A rectangle has properties (width, length) and behaviors (area, perimeter).
#
# 2. Why store width/length as floats?
#    Allows decimal measurements (e.g., 12.5 cm).
#
# 3. Why capitalize method names?
#    The exercise uses Perimeter() and Area() explicitly.
#    In real-world Python, lowercase is preferred, but we follow the spec.
#
# 4. Why no rounding?
#    Rectangle area/perimeter are exact for integer/float inputs.


# -------------------- EXAMPLES --------------------
#
# >>> r = Rectangle(10, 15)
# >>> r.width
# 10.0
#
# >>> r.length
# 15.0
#
# >>> r.Perimeter()
# 50.0
#
# >>> r.Area()
# 150.0
#
# >>> Rectangle(3.5, 2).Area()
# 7.0


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to convert width/length to float.
# 2. Using perimeter formula incorrectly (should be 2*(w + l)).
# 3. Using multiplication instead of addition inside Perimeter().
# 4. Misspelling method names (Perimeter vs. perimeter).
# 5. Returning strings instead of numeric values.


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------

# Beginner Version (very explicit, step-by-step)
class Rectangle_Beginner:
    def __init__(self, width, length):
        self.width = float(width)
        self.length = float(length)

    def Perimeter(self):
        p = 2 * (self.width + self.length)
        return p

    def Area(self):
        a = self.width * self.length
        return a


# Intermediate Version (My implementation)
class Rectangle_Intermediate:
    def __init__(self, width, length):
        self.width = float(width)
        self.length = float(length)

    def Perimeter(self):
        return 2 * (self.width + self.length)

    def Area(self):
        return self.width * self.length


# Advanced Version (adds validation + computed properties)
class Rectangle_Advanced:
    def __init__(self, width, length):
        if width <= 0 or length <= 0:
            raise ValueError("Width and length must be positive numbers.")
        self.width = float(width)
        self.length = float(length)

    @property
    def Perimeter(self):
        return 2 * (self.width + self.length)

    @property
    def Area(self):
        return self.width * self.length

    def describe(self):
        return (
            f"Rectangle: width={self.width} cm, length={self.length} cm, "
            f"perimeter={self.Perimeter} cm, area={self.Area} cm²"
        )


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Modeling geometric shapes with classes.
# 2. Using attributes to store dimensions.
# 3. Using methods to compute derived values.
# 4. Adding validation in advanced versions.
# 5. Using @property for clean attribute-like access.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What is the formula for the perimeter of a rectangle?
# A1: 2 * (width + length)
#
# Q2: What is the formula for the area of a rectangle?
# A2: width * length
#
# Q3: Why convert width/length to float?
# A3: To support decimal measurements.
#
# Q4: What happens if width or length is negative?
# A4: The advanced version raises a ValueError.
#
# ---------------------------------------------------------------
