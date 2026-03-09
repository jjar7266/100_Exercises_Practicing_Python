# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 94 - Operator overload

"""
Write a class Point2D that represents a point in a 2D space. Our class
should contain two attributes: x and y.

In this exercise, we want to perform some operations with instances created
from the Point2D class using standard operators such as +, -, *, etc.
To achieve this, we need to create the following special methods for the class:

    - __add__(self, p) which allows us to perform the operation p1 + p2
    - __sub__(self, p) which allows us to perform the operation p1 - p2
    - __mul__(self, p) which allows us to perform the operation p1 * p2
    - __truediv__(self, p) which allows us to perform the operation p1 / p2

Reminder: Operator overloading involves creating special methods in the
class that allows us to use standard operators such as +, -, *, /, and so on.

Verification tests:
>> p1 = Point2D(3, 2)
>> p2 = Point2D(1, 4)
>> p1 - p2
(2, -2)
>> p1 + p2
(4, 6)
>> p1/p2
(3.0, 0.5)
"""

class Point2D:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, p):
        return Point2D(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point2D(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return Point2D(self.x * p.x, self.y * p.y)

    def __truediv__(self, p):
        return Point2D(self.x / p.x, self.y / p.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


# -------------------- TEACHING NOTES --------------------
# Topic: Operator Overloading
#
# 1. Why overload operators?
#    It allows custom objects to behave like numbers or tuples.
#
# 2. Why return a new Point2D?
#    Operators should not mutate the original object.
#
# 3. Why convert x and y to float?
#    Ensures consistent numeric behavior.
#
# 4. Why implement __repr__?
#    Makes printing the object show (x, y) instead of a memory address.


# -------------------- EXAMPLES --------------------
#
# >>> p1 = Point2D(3, 2)
# >>> p2 = Point2D(1, 4)
#
# >>> p1 - p2
# (2.0, -2.0)
#
# >>> p1 + p2
# (4.0, 6.0)
#
# >>> p1 / p2
# (3.0, 0.5)
#
# >>> p1 * p2
# (3.0, 8.0)


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to return a new Point2D object.
# 2. Mutating self.x or self.y inside operators.
# 3. Forgetting __repr__, leading to unreadable output.
# 4. Dividing by zero (not handled in basic version).
# 5. Passing something that is not a Point2D instance.


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------

# Beginner Version (very explicit)
class Point2D_Beginner:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, p):
        new_x = self.x + p.x
        new_y = self.y + p.y
        return Point2D_Beginner(new_x, new_y)

    def __sub__(self, p):
        new_x = self.x - p.x
        new_y = self.y - p.y
        return Point2D_Beginner(new_x, new_y)

    def __mul__(self, p):
        new_x = self.x * p.x
        new_y = self.y * p.y
        return Point2D_Beginner(new_x, new_y)

    def __truediv__(self, p):
        new_x = self.x / p.x
        new_y = self.y / p.y
        return Point2D_Beginner(new_x, new_y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


# Intermediate Version (my implementation)
class Point2D_Intermediate:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, p):
        return Point2D_Intermediate(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point2D_Intermediate(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return Point2D_Intermediate(self.x * p.x, self.y * p.y)

    def __truediv__(self, p):
        return Point2D_Intermediate(self.x / p.x, self.y / p.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


# Advanced Version (adds validation + type checking)
class Point2D_Advanced:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def _validate(self, p):
        if not isinstance(p, Point2D_Advanced):
            raise TypeError("Operand must be a Point2D_Advanced instance.")

    def __add__(self, p):
        self._validate(p)
        return Point2D_Advanced(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        self._validate(p)
        return Point2D_Advanced(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        self._validate(p)
        return Point2D_Advanced(self.x * p.x, self.y * p.y)

    def __truediv__(self, p):
        self._validate(p)
        if p.x == 0 or p.y == 0:
            raise ZeroDivisionError("Cannot divide by zero in coordinates.")
        return Point2D_Advanced(self.x / p.x, self.y / p.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Operator overloading uses special methods (__add__, __sub__, etc.).
# 2. Always return a NEW object, not modify the original.
# 3. __repr__ makes objects readable.
# 4. Advanced version adds type checking and safety.
# 5. Overloading allows custom classes to behave like built-in types.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does __add__ return?
# A1: A new Point2D with coordinate-wise addition.
#
# Q2: Why use __repr__?
# A2: To display the object in a readable format.
#
# Q3: What happens if you divide by zero in the advanced version?
# A3: A ZeroDivisionError is raised.
#
# Q4: Why validate operand types?
# A4: To prevent invalid operations like p1 + 5.
#
# ---------------------------------------------------------------
