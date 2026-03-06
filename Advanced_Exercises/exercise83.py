# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 83 - Number with distinct digits

"""
Write a function isDistinct(number) that takes a positive integer as a parameter
and checks if all the digits in this number are distinct. The function should
return True if the number contains only distinct digits and False otherwise.

Verification tests:
>> isDistinct(9647)
True

>> isDistinct(1343)
False
"""

def isDistinct(number):
    s = str(number)

    # A set automatically removes duplicates
    # If all digits are distinct, the set size equals the string length
    return len(s) == len(set(s))

# -------------------- TEACHING NOTES --------------------
# Topic: Distinct Digits
#
# 1. Converting to string:
#    Makes it easy to treat each digit as a character.
#
# 2. Using a set:
#    A set contains only unique elements.
#    Example:
#       set("9647") -> {'9','6','4','7'}  (4 items)
#       set("1343") -> {'1','3','4'}      (3 items)
#
# 3. Core logic:
#    If the number has no repeated digits:
#       len(string) == len(set(string))
#
# 4. This is a classic Python pattern:
#       "check uniqueness using a set"

# -------------------- EXAMPLES --------------------
#
# >>> isDistinct(9647)
# True
#
# >>> isDistinct(1343)
# False
#
# >>> isDistinct(2024)
# False   # repeated '2'
#
# >>> isDistinct(5078)
# True

# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting that sets remove duplicates:
#    This is the entire trick.
#
# 2. Negative numbers:
#    str(-123) -> "-123"
#    The '-' would be treated as a character.
#    The exercise assumes positive integers only.
#
# 3. Overthinking:
#    No need for loops or counters — the set does the work.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     seen = []
#     for digit in str(number):
#         if digit in seen:
#             return False
#         seen.append(digit)
#     return True
#
# Intermediate (My implementation):
#     return len(str(number)) == len(set(str(number)))
#
# Advanced:
#     Use bitmasking for digit tracking (common in competitive programming).

# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Using sets to detect duplicates.
# 2. Comparing lengths to check uniqueness.
# 3. Converting numbers to strings for digit manipulation.

# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why does set("1343") have length 3?
# A1: Because sets remove duplicates, leaving only {'1','3','4'}.
#
# Q2: What condition tells us all digits are unique?
# A2: len(s) == len(set(s))
#
# ---------------------------------------------------------------
