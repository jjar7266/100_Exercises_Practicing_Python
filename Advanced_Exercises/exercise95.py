# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 95 - Operator overload

"""
Write a class ComplexNumber that represents complex numbers (in the
mathematical sense). This class will have two attributes: real and img

Reminder: a complex number consists of a real component and an
imaginary component. This number is written in the form 5 + 3i, where
the number 5 represents the real part and the number 3 represents the
imaginary part.

In this exercise, we want the following results when calling an instance
of the class or using print() with this instance:

Verification tests:
>> nbr1 = ComplexNumber(2, 7)
>> nbr1
2 + 7i
>> print(nbr1)
2 + 7i

To achieve this, we need to create the following special methods:

    - __str__(self) which allows us to have the correct display using print()
    - __repr__(self) which allows us to have the correct display when calling instance.
"""

class ComplexNumber:
    def __init__(self, real, img):
        self.real = float(real)
        self.img = float(img)

    def __str__(self):
        return f"{self.real:.0f} + {self.img:.0f}i"

    def __repr__(self):
        return f"{self.real:.0f} + {self.img:.0f}i"


# -------------------- TEACHING NOTES --------------------
# Topic: __str__ vs __repr__
#
# 1. __str__ is used when calling print(obj).
# 2. __repr__ is used when evaluating obj directly in the interpreter.
# 3. In this exercise, both methods return the same string.
# 4. The format "a + bi" matches the mathematical representation.
# 5. Using .0f ensures integers display cleanly (2 instead of 2.0).


# -------------------- EXAMPLES --------------------
#
# >>> nbr1 = ComplexNumber(2, 7)
# >>> nbr1
# 2 + 7i
#
# >>> print(nbr1)
# 2 + 7i
#
# >>> nbr2 = ComplexNumber(5.3, 1.8)
# >>> nbr2
# 5 + 2i


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to implement __repr__, causing unreadable output.
# 2. Returning None instead of a string.
# 3. Using print() inside __str__ or __repr__ (never do this).
# 4. Forgetting to convert values to float.
# 5. Not formatting the output consistently.


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------

# Beginner Version (very explicit)
class ComplexNumber_Beginner:
    def __init__(self, real, img):
        self.real = float(real)
        self.img = float(img)

    def __str__(self):
        text = f"{self.real:.0f} + {self.img:.0f}i"
        return text

    def __repr__(self):
        text = f"{self.real:.0f} + {self.img:.0f}i"
        return text


# Intermediate Version (my implementation)
class ComplexNumber_Intermediate:
    def __init__(self, real, img):
        self.real = float(real)
        self.img = float(img)

    def __str__(self):
        return f"{self.real:.0f} + {self.img:.0f}i"

    def __repr__(self):
        return f"{self.real:.0f} + {self.img:.0f}i"


# Advanced Version (adds sign handling + formatting)
class ComplexNumber_Advanced:
    def __init__(self, real, img):
        self.real = float(real)
        self.img = float(img)

    def __str__(self):
        sign = "+" if self.img >= 0 else "-"
        return f"{self.real:.0f} {sign} {abs(self.img):.0f}i"

    def __repr__(self):
        sign = "+" if self.img >= 0 else "-"
        return f"{self.real:.0f} {sign} {abs(self.img):.0f}i"


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. __str__ and __repr__ often return the same string.
# 2. __repr__ is the fallback when __str__ is missing.
# 3. Formatting output is part of object design.
# 4. Advanced version handles negative imaginary parts.
# 5. Clean string formatting improves readability.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What is the purpose of __str__?
# A1: To define how the object appears when printed.
#
# Q2: What is the purpose of __repr__?
# A2: To define how the object appears when evaluated in the interpreter.
#
# Q3: Why use abs(self.img) in the advanced version?
# A3: To avoid printing double signs like "5 + -3i".
#
# Q4: What does ComplexNumber(2, 7) display?
# A4: "2 + 7i"
#
# ---------------------------------------------------------------
