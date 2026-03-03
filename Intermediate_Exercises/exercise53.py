# 100 Exercises for Practicing PYTHON

# Author: Laurentine K. Masson

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 53 - Presence of a Vowel in a String

"""
Write a function hasVowel(sentence) which takes a sentence as a
parameter and checks if a sentence contains a vowel or not. If the
sentence contains a vowel, the function returns True; otherwise, it
returns False.

Note: we will assume that the vowels in English are as follows:
(a, e, i, o, u, y)

Verification tests:
>>> hasVowel("I'm going to take my shower")
True

>>> hasVowel("rbhpm")
False
"""

def hasVowel(sentence):
    vowels = "aeiouyAEIOUY"

    for char in sentence:
        if char in vowels:
            return True
        
    return False

# -------------------- TEACHING NOTES --------------------
# Topic: Detecting vowels in a string
#
# 1. Vowel set:
#       vowels = "aeiouyAEIOUY"
#    Includes lowercase and uppercase vowels.
#
# 2. Membership test:
#       if char in vowels:
#    Checks if the character is one of the vowels.
#
# 3. Early return:
#       return True
#    As soon as a vowel is found, no need to continue scanning.
#
# 4. Final return:
#       return False
#    Only reached if no vowel was found in the entire sentence.
#
# 5. Why include 'y':
#    The exercise explicitly defines it as a vowel.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> hasVowel("sky")
# True   # 'y' counts as a vowel here
#
# Example 2:
# >>> hasVowel("bcd fgh")
# False
#
# Example 3:
# >>> hasVowel("HELLO")
# True   # uppercase vowels included
#
# Example 4:
# >>> hasVowel("Python")
# True   # 'y' is considered a vowel


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting uppercase vowels:
#    Only checking lowercase will miss "A", "E", etc.
#
# 2. Incorrect OR usage:
#       if char == 'a' or 'e' or 'i' ...
#    This always evaluates to True. Use membership instead.
#
# 3. Not returning early:
#    Some beginners scan the whole string unnecessarily.
#
# 4. Misunderstanding 'y':
#    It is included as a vowel *for this exercise*.


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner (clear and explicit):
#     def hasVowel(sentence):
#         vowels = "aeiouyAEIOUY"
#         for char in sentence:
#             if char in vowels:
#                 return True
#         return False
#
# Intermediate (normalize case):
#     def hasVowel(sentence):
#         vowels = "aeiouy"
#         for char in sentence.lower():
#             if char in vowels:
#                 return True
#         return False
#
# Advanced (Pythonic using any):
#     def hasVowel(sentence):
#         return any(char.lower() in "aeiouy" for char in sentence)
#
# Notes:
# - any() is compact and Pythonic.
# - Beginner version is best for learning clarity.


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "Scan → Check → Return" Pattern
#    - Common for "does this string contain X?" problems.
#
# 2. Membership test ("in")
#    - Cleaner than chaining comparisons.
#
# 3. Case normalization
#    - Using .lower() avoids needing uppercase vowels.
#
# 4. Early exit
#    - Stop scanning once the answer is known.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does char in vowels check?
# A1: Whether the character is one of the defined vowels.
#
# Q2: Why include uppercase vowels?
# A2: To ensure the function works regardless of letter case.
#
# Q3: Why return early?
# A3: Once a vowel is found, the result is known.
#
# Q4: What Python function can replace the loop?
# A4: any() with a generator expression.
#
# Q5: Why does "y" count as a vowel here?
# A5: The exercise explicitly defines it as one.
#
# ---------------------------------------------------------------

