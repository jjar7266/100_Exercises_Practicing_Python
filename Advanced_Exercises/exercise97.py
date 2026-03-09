# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 97 - Customized string class

"""
Write a class CustomString which is a custom string class. Our custom
string should not contain numbers, commas, or periods.

In this exercise, you need to create methods that allow us to perform the
following operations:

>> string1 = CustomString("He,llo")
The created instance should only contain alphabetical letters
The character ", " will be removed

>> string1 + ","
You cannot add ',' to the string

>> string1 + "."
You cannot add '.' to the string

>> string2 = string1 + "How are you?"
>> string2
Hello How are you?
"""

class CustomString:
    def __init__(self, text):
        self.text = self._clean(text)

    def _clean(self, text):
        cleaned = ""
        for char in text:
            if char.isalpha() or char == " ":
                cleaned += char
            else:
                print(f"The character '{char}' will be removed")
        return cleaned

    def __add__(self, other):
        # Reject numbers
        if any(ch.isdigit() for ch in other):
            print(f"You cannot add '{other}' to the string")
            return self

        # Reject commas or periods
        if "," in other:
            print("You cannot add ',' to the string")
            return self

        if "." in other:
            print("You cannot add '.' to the string")
            return self

        # Otherwise, concatenate and clean the result
        new_text = self.text + " " + other
        return CustomString(new_text)

    def __repr__(self):
        return self.text

    def __str__(self):
        return self.text


# -------------------- TEACHING NOTES --------------------
# Topic: Custom string class + operator overloading
#
# 1. __add__ allows using + between two CustomString objects or a string.
# 2. The class removes forbidden characters at creation time.
# 3. The class blocks adding commas, periods, or digits.
# 4. __repr__ and __str__ return the cleaned string.
# 5. Returning self on invalid additions preserves immutability.


# -------------------- EXAMPLES --------------------
#
# >>> string1 = CustomString("He,llo")
# The character ',' will be removed
# >>> string1
# Hello
#
# >>> string1 + ","
# You cannot add ',' to the string
#
# >>> string1 + "."
# You cannot add '.' to the string
#
# >>> string2 = string1 + "How are you?"
# The character '?' will be removed
# >>> string2
# Hello How are you


# -------------------- COMMON PITFALLS --------------------
#
# 1. Forgetting to remove forbidden characters in __init__.
# 2. Forgetting to block digits in __add__.
# 3. Returning None instead of a CustomString instance.
# 4. Forgetting to print the required messages.
# 5. Forgetting to allow spaces.


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------

# Beginner Version (very explicit)
class CustomString_Beginner:
    def __init__(self, text):
        self.text = ""
        for char in text:
            if char.isalpha() or char == " ":
                self.text += char
            else:
                print(f"The character '{char}' will be removed")

    def __add__(self, other):
        if any(ch.isdigit() for ch in other):
            print(f"You cannot add '{other}' to the string")
            return self

        if "," in other:
            print("You cannot add ',' to the string")
            return self

        if "." in other:
            print("You cannot add '.' to the string")
            return self

        new_text = self.text + " " + other
        return CustomString_Beginner(new_text)

    def __repr__(self):
        return self.text

    def __str__(self):
        return self.text


# Intermediate Version (my implementation)
class CustomString_Intermediate:
    def __init__(self, text):
        self.text = self._clean(text)

    def _clean(self, text):
        cleaned = ""
        for char in text:
            if char.isalpha() or char == " ":
                cleaned += char
            else:
                print(f"The character '{char}' will be removed")
        return cleaned

    def __add__(self, other):
        if any(ch.isdigit() for ch in other):
            print(f"You cannot add '{other}' to the string")
            return self

        if "," in other:
            print("You cannot add ',' to the string")
            return self

        if "." in other:
            print("You cannot add '.' to the string")
            return self

        new_text = self.text + " " + other
        return CustomString_Intermediate(new_text)

    def __repr__(self):
        return self.text

    def __str__(self):
        return self.text


# Advanced Version (adds punctuation filtering + trimming)
class CustomString_Advanced:
    FORBIDDEN = set("0123456789,.")

    def __init__(self, text):
        self.text = self._clean(text)

    def _clean(self, text):
        cleaned = ""
        for char in text:
            if char in self.FORBIDDEN:
                print(f"The character '{char}' will be removed")
            elif char.isalpha() or char == " ":
                cleaned += char
        return cleaned.strip()

    def __add__(self, other):
        if any(ch in self.FORBIDDEN for ch in other):
            print(f"You cannot add '{other}' to the string")
            return self

        new_text = f"{self.text} {other}".strip()
        return CustomString_Advanced(new_text)

    def __repr__(self):
        return self.text

    def __str__(self):
        return self.text


# -------------------- MINI-QUIZ --------------------
#
# Q1: Why does __add__ return a new object?
# A1: To keep the class immutable like real strings.
#
# Q2: Why remove characters in __init__?
# A2: To guarantee the stored string always follows the rules.
#
# Q3: What happens if you add a comma?
# A3: A message prints and the original string is returned unchanged.
#
# ---------------------------------------------------------------
