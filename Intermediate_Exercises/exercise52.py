# 100 Exercises for Practicing PYTHON

# Author: Laurentine K. Masson

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 52 - Divisors & Multiples

"""
Write a function divisorMult(n, a, threshold) that finds the numbers
(from 0 up to a given threshold) divisible by n and not multiples of a.

Verification tests:
>> divisorMult(5, 2, 100)
[5, 15, 25, 35, 45, 55, 65, 75, 85, 95]

>> divisorMult(11, 3, 85)
[11, 22, 44, 55, 77]
"""

def divisorMult(n, a, threshold):
    result = []

    for x in range(0, threshold + 1):
        if x % n == 0 and x % a != 0:
            result.append(x)

    return result

# -------------------- TEACHING NOTES --------------------
# Topic: Filtering numbers using multiple conditions
#
# 1. Divisible by n:
#       x % n == 0
#    Means the remainder is zero → x is a multiple of n.
#
# 2. NOT a multiple of a:
#       x % a != 0
#    Means the remainder is NOT zero → x is NOT a multiple of a.
#
# 3. Looping through a range:
#       range(0, threshold + 1)
#    Includes 0 and includes the threshold.
#
# 4. Combining conditions:
#       if condition1 and condition2:
#    Both must be true for the number to be added.
#
# 5. Appending results:
#       result.append(x)
#    Adds the number to the final list.
#
# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> divisorMult(5, 2, 30)
# [5, 15, 25]
#
# Example 2:
# >>> divisorMult(3, 4, 20)
# [3, 6, 9, 15, 18]
#
# Example 3:
# >>> divisorMult(7, 5, 40)
# [7, 14, 21, 28, 35]
#
# Example 4:
# >>> divisorMult(4, 2, 20)
# []   # all multiples of 4 are also multiples of 2
#
# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to combine conditions:
#       if x % n == 0:
#       if x % a != 0:
#    These must be combined into ONE if statement.
#
# 2. Using OR instead of AND:
#       if x % n == 0 or x % a != 0:
#    This would include numbers that fail one of the rules.
#
# 3. Forgetting threshold + 1:
#    range(0, threshold) stops too early.
#
# 4. Misunderstanding modulo:
#    x % n == 0 means divisible.
#    x % n != 0 means NOT divisible.
#
# 5. Starting the range at 1:
#    The exercise includes 0, even though 0 will usually be excluded
#    because it is a multiple of every number.
#
# ---------------------------------------------------------------


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner (explicit, readable):
#     def divisorMult(n, a, threshold):
#         result = []
#         for x in range(threshold + 1):
#             if x % n == 0 and x % a != 0:
#                 result.append(x)
#         return result
#
# Intermediate (list comprehension):
#     def divisorMult(n, a, threshold):
#         return [x for x in range(threshold + 1)
#                 if x % n == 0 and x % a != 0]
#
# Advanced (functional style with filter):
#     def divisorMult(n, a, threshold):
#         return list(filter(lambda x: x % n == 0 and x % a != 0,
#                            range(threshold + 1)))
#
# Notes:
# - List comprehension is the most Pythonic.
# - Beginner version is the clearest for learning.
#
# ---------------------------------------------------------------


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "Loop → Check → Append" Pattern
#    - Very common in filtering problems.
#
# 2. "Multiple conditions" Pattern
#    - Use AND when all conditions must be true.
#
# 3. "Modulo logic" Pattern
#    - x % n == 0 → divisible
#    - x % n != 0 → not divisible
#
# 4. "Inclusive range" Pattern
#    - range(0, threshold + 1) includes the threshold.
#
# ---------------------------------------------------------------


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does x % n == 0 mean?
# A1: x is divisible by n.
#
# Q2: What does x % a != 0 mean?
# A2: x is NOT a multiple of a.
#
# Q3: Why do we use AND in the condition?
# A3: Both conditions must be true for x to be included.
#
# Q4: What does range(0, threshold + 1) generate?
# A4: All numbers from 0 through threshold.
#
# Q5: Why is 0 usually excluded from the results?
# A5: Because 0 is a multiple of every number.
#
# ---------------------------------------------------------------