# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 84

"""
Write a function codeSum(number) that takes a positive integer number
greater than 100 as a parameter and allows determining a code from this
number, following the steps below:

    - Step 1: Sum the digits of the number passed as a parameter.
    - Step 2: Repeat the calculation of the obtained sum (in Step 1) until it
    falls between 1 and 9.

The code will be the original number with the last obtained sum added to its left.

Verification tests:
>> codeSum(69810)
669810

>> codeSum(3201)
63201
"""

def codeSum(number):
    # Step 1 & 2: Repeated digit sum until result is between 1 and 9
    total = sum(int(d) for d in str(number))

    while total > 9:
        total = sum(int(d) for d in str(total))

    # Step 3: Prepend the final digit-sum to the original number
    return int(str(total) + str(number))

# -------------------- TEACHING NOTES --------------------
# Topic: Repeated Digit Sum (Digital Root)
#
# 1. Summing digits:
#    sum(int(d) for d in str(number))
#
# 2. Repeating the sum:
#    Keep summing until the result is a single digit (1–9).
#
# 3. This repeated digit-sum is known as the "digital root".
#
# 4. Final step:
#    Prepend the final single-digit sum to the original number.
#    Example:
#       number = 69810
#       digit sum = 6 + 9 + 8 + 1 + 0 = 24
#       repeat: 2 + 4 = 6
#       final code = "6" + "69810" = 669810

# -------------------- EXAMPLES --------------------
#
# >>> codeSum(69810)
# 669810
#
# >>> codeSum(3201)
# 63201
#
# >>> codeSum(999)
# 9999   # 9+9+9=27 → 2+7=9 → "9" + "999" = 9999

# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to repeat the digit sum:
#    69810 → 24 → must continue → 6
#
# 2. Returning the sum instead of the final code:
#    The exercise requires prepending the digit.
#
# 3. Using math instead of string concatenation:
#    String concatenation is simpler and avoids digit shifting.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     Use loops to sum digits manually.
#
# Intermediate (My implementation):
#     Use generator expressions and string concatenation.
#
# Advanced:
#     Use digital root formula:
#         digital_root = 1 + ((number - 1) % 9)
#     But the exercise expects repeated summing, not the formula.

# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Converting numbers to strings for digit manipulation.
# 2. Repeated reduction until a base condition is met.
# 3. Constructing new numbers by concatenating strings.

# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What is the repeated digit sum called?
# A1: The digital root.
#
# Q2: When do we stop summing digits?
# A2: When the result is between 1 and 9.
#
# Q3: How is the final code formed?
# A3: Prepend the final digit-sum to the original number.
#
# ---------------------------------------------------------------
