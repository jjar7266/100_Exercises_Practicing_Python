# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 80 - Palindrome numbers

"""
Write a function isPalindrome(nbr) that takes a positive integer nbr as a
parameter and returns True if nbr is a palindrome, and False if it is not.

Reminder: a palindrome number is a natural number greater than 10 that
reads the same foreward as it does backwards.

For example, the numbers 69596, 4231324, 212 are palindrome numbers.

Verification tests:
>> isPalindrome(10)
False

>> isPalindrome(919)
True
"""

def isPalindrome(nbr):
    # Convert number to string to check symmetry
    s = str(nbr)

    # Numbers less than 10 are not considered palindromes
    if nbr < 10:
        return False

    # Compare string to its reverse
    return s == s[::-1]

# -------------------- TEACHING NOTES --------------------
# Topic: Palindrome Numbers
#
# 1. Converting to string:
#    str(nbr) allows us to treat the number like any other sequence.
#
# 2. Reversing a string:
#    s[::-1] creates a reversed copy of the string.
#
# 3. Palindrome logic:
#    A number is a palindrome if the forward and backward versions match.
#
# 4. Why numbers < 10 return False:
#    The exercise defines palindromes as natural numbers > 10.

# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> isPalindrome(10)
# False
#
# Example 2:
# >>> isPalindrome(919)
# True
#
# Example 3:
# >>> isPalindrome(4231324)
# True
#
# Example 4:
# >>> isPalindrome(1234)
# False

# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting the "greater than 10" rule:
#    isPalindrome(7) → False (by exercise definition)
#
# 2. Negative numbers:
#    -121 → False (minus sign breaks symmetry)
#
# 3. Leading zeros:
#    010 → invalid as an integer literal
#
# 4. Overthinking:
#    No need for math tricks — string reversal is clean and readable.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     s = str(nbr)
#     reversed_s = ""
#     for ch in s:
#         reversed_s = ch + reversed_s
#     return s == reversed_s and nbr > 10
#
# Intermediate (My implementation):
#     def isPalindrome(nbr):
#         s = str(nbr)
#         if nbr < 10:
#             return False
#         return s == s[::-1]
#
# Advanced (math-only approach):
#     def isPalindrome(nbr):
#         if nbr < 10:
#             return False
#         original = nbr
#         reversed_n = 0
#         while nbr > 0:
#             reversed_n = reversed_n * 10 + (nbr % 10)
#             nbr //= 10
#         return original == reversed_n

# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Converting numbers to strings for easier manipulation.
# 2. Using slicing to reverse sequences.
# 3. Returning early for invalid cases.
# 4. Comparing original vs reversed values.

# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why do we convert the number to a string?
# A1: Because reversing and comparing strings is simple and reliable.
#
# Q2: Why does isPalindrome(7) return False?
# A2: The exercise defines palindromes as numbers greater than 10.
#
# Q3: What does s[::-1] do?
# A3: Creates a reversed copy of the string.
#
# ---------------------------------------------------------------
