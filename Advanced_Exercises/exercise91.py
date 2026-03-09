# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 91 - Inheriting a class

from exercise90 import Rectangle, Rectangle_Advanced

# Exercise 91 - Inheriting a class

"""
Write a class Parallelepiped that inherits from the Rectangle class from the
previous exercise. The Parallelepiped class should contain, in addition to
the inherited attributes, the attribute height (in cm).

The Parallelepiped class should have the following method:
     - Volume(self) which calculates the volume of the parallelepiped

>> parallelepiped1 = Parallelepiped(9, 5, 2)
>> parallelepiped1.Perimeter()
28

>> parallelepiped1.Volume()
90
"""

class Parallelepiped(Rectangle):
    def __init__(self, width, length, height):
        super().__init__(width, length)
        self.height = float(height)

    def Volume(self):
        return self.width * self.length * self.height


# -------------------- TEACHING NOTES --------------------
# Topic: Inheritance & Extending a Base Class
#
# 1. Why inherit from Rectangle?
#    A parallelepiped is a 3D extension of a rectangle. We reuse width/length.
#
# 2. Why call super().__init__()?
#    Ensures Rectangle initializes width and length before adding height.
#
# 3. Why store height as float?
#    Supports decimal measurements.
#
# 4. Why is Volume = width * length * height?
#    A parallelepiped is a 3D box. Volume = base area * height.


# -------------------- EXAMPLES --------------------
#
# >>> p = Parallelepiped(9, 5, 2)
# >>> p.width
# 9.0
#
# >>> p.length
# 5.0
#
# >>> p.height
# 2.0
#
# >>> p.Perimeter()
# 28.0
#
# >>> p.Volume()
# 90.0


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to call super().__init__().
# 2. Misspelling "Parallelepiped".
# 3. Using addition instead of multiplication for volume.
# 4. Forgetting to convert height to float.
# 5. Overriding Rectangle methods unnecessarily.


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------

# Beginner Version (very explicit)
class Parallelepiped_Beginner(Rectangle):
    def __init__(self, width, length, height):
        super().__init__(width, length)
        self.height = float(height)

    def Volume(self):
        v = self.width * self.length * self.height
        return v


# Intermediate Version (your style)
class Parallelepiped_Intermediate(Rectangle):
    def __init__(self, width, length, height):
        super().__init__(width, length)
        self.height = float(height)

    def Volume(self):
        return self.width * self.length * self.height


# Advanced Version (adds validation + properties)
class Parallelepiped_Advanced(Rectangle_Advanced):
    def __init__(self, width, length, height):
        if height <= 0:
            raise ValueError("Height must be a positive number.")
        super().__init__(width, length)
        self.height = float(height)

    @property
    def Volume(self):
        return self.width * self.length * self.height

    def describe(self):
        return (
            f"Parallelepiped: width={self.width} cm, length={self.length} cm, "
            f"height={self.height} cm, perimeter={self.Perimeter} cm, "
            f"volume={self.Volume} cm³"
        )


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Using inheritance to extend functionality.
# 2. Reusing base class attributes and methods.
# 3. Adding new attributes in child classes.
# 4. Using super() to avoid duplication.
# 5. Adding validation in advanced versions.
# 6. Using @property for clean attribute access.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What keyword is used to inherit from another class?
# A1: class Child(Parent):
#
# Q2: Why call super().__init__()?
# A2: To initialize the parent class attributes.
#
# Q3: What is the formula for the volume of a parallelepiped?
# A3: width * length * height
#
# Q4: What happens if height is negative in the advanced version?
# A4: A ValueError is raised.
#
# ---------------------------------------------------------------
