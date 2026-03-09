# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 96 - Customized list class

"""
Write a class CustomList which is a custom list class.
Our custom list should only contain numbers and not strings or
booleans. In our custom list, duplicates are not allowed.

In this exercise, you need to create methods that allow us to perform the
following operations:

Verification tests:
>> L1 = CustomList(5, 2, 3, 7, 9)
>> print(L1)
[5, 2, 3, 7, 9]
>> L1.append(2)
The number 2 already exists in the list [5, 2, 3, 7, 9]
>> L1.append("abc")
Forbidden operation: It is not possible to add type < class 'str' > to the list
>> L1.append(10)
>> print(L1)
[5, 2, 3, 7, 9, 10]
"""

class CustomList:
    def __init__(self, *args):
        self.data = []
        for value in args:
            self.append(value)

    def append(self, value):
        # Reject booleans explicitly (since bool is a subclass of int)
        if type(value) is bool:
            print(f"Forbidden operation: It is not possible to add type < class 'bool' > to the list")
            return

        # Reject non-numeric types
        if not isinstance(value, (int, float)):
            print(f"Forbidden operation: It is not possible to add type < class '{type(value).__name__}' > to the list")
            return

        # Reject duplicates
        if value in self.data:
            print(f"The number {value} already exists in the list {self.data}")
            return

        self.data.append(value)

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)


# -------------------- TEACHING NOTES --------------------
# Topic: Custom container classes
#
# 1. Why use *args in __init__?
#    Allows passing any number of initial values.
#
# 2. Why store values in self.data?
#    Keeps internal structure clean and avoids subclassing list.
#
# 3. Why check type(value) is bool?
#    Because bool is a subclass of int, so isinstance(True, int) is True.
#
# 4. Why print messages instead of raising errors?
#    The exercise requires EXACT printed output.


# -------------------- EXAMPLES --------------------
#
# >>> L1 = CustomList(5, 2, 3, 7, 9)
# >>> print(L1)
# [5, 2, 3, 7, 9]
#
# >>> L1.append(2)
# The number 2 already exists in the list [5, 2, 3, 7, 9]
#
# >>> L1.append("abc")
# Forbidden operation: It is not possible to add type < class 'str' > to the list
#
# >>> L1.append(10)
# >>> print(L1)
# [5, 2, 3, 7, 9, 10]


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting that bool is a subclass of int.
# 2. Forgetting to check duplicates.
# 3. Using print() inside __repr__ (never do this).
# 4. Mutating args directly instead of using append().
# 5. Returning None from __repr__ or __str__.


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------

# Beginner Version (very explicit)
class CustomList_Beginner:
    def __init__(self, *args):
        self.data = []
        for value in args:
            self.append(value)

    def append(self, value):
        if type(value) is bool:
            print("Forbidden operation: It is not possible to add type < class 'bool' > to the list")
            return

        if not isinstance(value, (int, float)):
            print(f"Forbidden operation: It is not possible to add type < class '{type(value).__name__}' > to the list")
            return

        if value in self.data:
            print(f"The number {value} already exists in the list {self.data}")
            return

        self.data.append(value)

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)


# Intermediate Version (my implementation)
class CustomList_Intermediate:
    def __init__(self, *args):
        self.data = []
        for value in args:
            self.append(value)

    def append(self, value):
        if type(value) is bool:
            print("Forbidden operation: It is not possible to add type < class 'bool' > to the list")
            return

        if not isinstance(value, (int, float)):
            print(f"Forbidden operation: It is not possible to add type < class '{type(value).__name__}' > to the list")
            return

        if value in self.data:
            print(f"The number {value} already exists in the list {self.data}")
            return

        self.data.append(value)

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)


# Advanced Version (adds remove, contains, and length)
class CustomList_Advanced:
    def __init__(self, *args):
        self.data = []
        for value in args:
            self.append(value)

    def _validate(self, value):
        if type(value) is bool:
            raise TypeError("Booleans are not allowed.")
        if not isinstance(value, (int, float)):
            raise TypeError(f"Only numbers allowed, not {type(value).__name__}.")

    def append(self, value):
        try:
            self._validate(value)
        except TypeError as e:
            print(f"Forbidden operation: {e}")
            return

        if value in self.data:
            print(f"The number {value} already exists in the list {self.data}")
            return

        self.data.append(value)

    def remove(self, value):
        if value in self.data:
            self.data.remove(value)

    def __contains__(self, value):
        return value in self.data

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Custom containers often wrap Python lists.
# 2. Validation logic belongs in append().
# 3. __repr__ and __str__ should return readable output.
# 4. Using *args allows flexible initialization.
# 5. Advanced version adds Pythonic behavior (__len__, __contains__).


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why reject bool explicitly?
# A1: Because bool is a subclass of int.
#
# Q2: What happens if you append a duplicate?
# A2: A message prints and nothing is added.
#
# Q3: What does __repr__ return?
# A3: A string representation of the internal list.
#
# Q4: Why use *args in __init__?
# A4: To allow any number of initial values.
#
# ---------------------------------------------------------------
