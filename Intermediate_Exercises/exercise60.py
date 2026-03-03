# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 60 - Calculation of the GCD

"""
Write a function calculateGCD(a, b) which takes two integers a and b as
parameters and calculates the greatest common divisor (GCD) using the
Euclidean algorithm.

Reminder: The Euclidean division of a by b is written as follows:
a = b*q + r, where q is the quotient and r is the remainder of the division.

Verification tests:

>> calculateGCD(3, 5)
1

>> calculateGCD(5, 15)
5
"""

def calculateGCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# -------------------- TEACHING NOTES --------------------
# Topic: Euclidean Algorithm for GCD
#
# 1. The key identity:
#       gcd(a, b) = gcd(b, a % b)
#    This allows us to reduce the problem at each step.
#
# 2. Loop structure:
#       while b != 0:
#           a, b = b, a % b
#    - Replace (a, b) with (b, remainder)
#    - Continue until remainder becomes 0
#
# 3. Final result:
#    When b becomes 0, the current value of a is the GCD.
#
# 4. Why this works:
#    The Euclidean algorithm repeatedly removes multiples of the smaller
#    number from the larger one, preserving the common divisors.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> calculateGCD(3, 5)
# 1
#
# Example 2:
# >>> calculateGCD(5, 15)
# 5
#
# Example 3:
# >>> calculateGCD(42, 56)
# 14
#
# Example 4:
# >>> calculateGCD(12, 0)
# 12   # gcd(a, 0) = |a|


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to update both a and b:
#    The algorithm requires swapping and reducing simultaneously.
#
# 2. Using subtraction instead of modulo:
#    Works, but is much slower for large numbers.
#
# 3. Not handling zero:
#    gcd(a, 0) should return |a|.
#
# 4. Negative inputs:
#    The algorithm still works; the final GCD is always non-negative.


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner:
#     def calculateGCD(a, b):
#         while b != 0:
#             temp = b
#             b = a % b
#             a = temp
#         return a
#
# Intermediate (tuple swap):
#     def calculateGCD(a, b):
#         while b:
#             a, b = b, a % b
#         return a
#
# Advanced (recursive):
#     def calculateGCD(a, b):
#         return a if b == 0 else calculateGCD(b, a % b)


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "Reduce until remainder is zero" pattern.
# 2. Tuple swapping to update multiple variables cleanly.
# 3. Using modulo to shrink the problem quickly.
# 4. Recursion vs. iteration for mathematical algorithms.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What is the stopping condition of the Euclidean algorithm?
# A1: When the remainder (b) becomes 0.
#
# Q2: What is gcd(a, 0)?
# A2: |a|.
#
# Q3: Why does a % b reduce the problem?
# A3: Because the remainder has the same common divisors as (a, b).
#
# ---------------------------------------------------------------
