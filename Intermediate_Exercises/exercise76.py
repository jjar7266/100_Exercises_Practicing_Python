# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 76 - Recreating the join method

"""
Write a function join(L, character) that transforms a list L into a string using
the separator character passed as a parameter.

Verification tests:
>> join(["Hello", "Aurelie"], " ")
"Hello Aurelie"

>> join(["Hi", " How are you?"], ",")
"Hi, How are you?"
"""

def join(L, character):
    # Build the final string manually
    result = ""
    for i in range(len(L)):
        result += L[i]
        # Add separator only between elements
        if i < len(L) - 1:
            result += character
    return result

# -------------------- TEACHING NOTES --------------------
# Topic: Recreating Python's join() method
#
# 1. Manual string building:
#    We append each element of the list to a result string.
#
# 2. Separator logic:
#    We add the separator only between elements, never after the last one.
#
# 3. Why this works:
#    It mimics how Python's built-in join() method behaves internally.
#
# 4. Flexibility:
#    Works with any list of strings and any separator.

# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> join(["Hello", "Aurelie"], " ")
# "Hello Aurelie"
#
# Example 2:
# >>> join(["Hi", " How are you?"], ",")
# "Hi, How are you?"
#
# Example 3:
# >>> join(["a", "b", "c"], "-")
# "a-b-c"

# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Adding a separator after the last element:
#    This produces strings like "a-b-c-" which is incorrect.
#
# 2. Forgetting to handle empty lists:
#    join([], ",") should return "".
#
# 3. Mixing non-string elements:
#    Python's real join() requires all elements to be strings.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     result = ""
#     for i in range(len(L)):
#         result += L[i]
#         if i < len(L) - 1:
#             result += character
#     return result
#
# Intermediate (My implementation):
#     def join(L, character):
#         result = ""
#         for i in range(len(L)):
#             result += L[i]
#             if i < len(L) - 1:
#                 result += character
#         return result
#
# Advanced (Pythonic):
#     def join(L, character):
#         return character.join(L)

# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Using indexing to detect the last element.
# 2. Building strings incrementally.
# 3. Recreating built-in behavior manually.
# 4. Handling edge cases like empty lists.

# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why do we check if i < len(L) - 1?
# A1: To avoid adding the separator after the last element.
#
# Q2: What should join([], ",") return?
# A2: An empty string "".
#
# Q3: What is the Pythonic way to join a list?
# A3: character.join(L)
#
# ---------------------------------------------------------------
