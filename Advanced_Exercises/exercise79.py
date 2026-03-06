# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 79 - Recreating the isdigit() method

"""
Write a function isdigit(string) that checks whether the string is a number or not.
The function returns True if the string is a number and False otherwise.

Verification tests:
>> isdigit("125920")
True

>> isdigit("edgte9be")
False
"""

def isdigit(string):
    # Recreate Python's isdigit() behavior manually
    if string == "":
        return False

    for ch in string:
        if ch < "0" or ch > "9":   # ASCII range check
            return False

    return True

# -------------------- TEACHING NOTES --------------------
# Topic: Recreating Python's isdigit() method
#
# 1. What is a digit?
#    Characters between '0' and '9' in ASCII.
#
# 2. Manual digit check:
#    Instead of using ch.isdigit(), we compare ASCII ranges:
#        '0' <= ch <= '9'
#
# 3. Empty string:
#    Python's "123".isdigit() → True
#    "".isdigit() → False
#
# 4. Why this works:
#    Every character must be a digit for the whole string to be numeric.

# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> isdigit("125920")
# True
#
# Example 2:
# >>> isdigit("edgte9be")
# False
#
# Example 3:
# >>> isdigit("007")
# True
#
# Example 4:
# >>> isdigit("12 34")
# False   # space is not a digit

# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Negative numbers:
#    "-123" → False
#    Python's isdigit() also returns False for negatives.
#
# 2. Decimal numbers:
#    "12.5" → False
#
# 3. Leading/trailing spaces:
#    " 123" → False
#    "123 " → False
#
# 4. Empty string:
#    Should return False.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     for ch in string:
#         if not ch.isdigit():
#             return False
#     return string != ""
#
# Intermediate (My implementation):
#     def isdigit(string):
#         if string == "":
#             return False
#         for ch in string:
#             if ch < "0" or ch > "9":
#                 return False
#         return True
#
# Advanced (Unicode-aware):
#     def isdigit(string):
#         return string.isdigit()

# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Checking characters one by one.
# 2. Using ASCII comparisons instead of built-in methods.
# 3. Returning False early when a non-digit is found.
# 4. Handling empty strings explicitly.

# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why do we check ch < "0" or ch > "9"?
# A1: To ensure the character is within the ASCII digit range.
#
# Q2: Should "-123" return True?
# A2: No — the minus sign is not a digit.
#
# Q3: What does isdigit("") return?
# A3: False.
#
# ---------------------------------------------------------------
