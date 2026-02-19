# 100 Exercises for Practicing PYTHON

# Author: Laurentine K. Masson

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 51 - Calculating the factorial of a number

"""
Write a function computeFactorial(n) that calculates the factorial of a
number (in the mathematical sense) and returns the result obtained 
after this calculation.

Verification tests:
>> computeFactorial(3)
6

>> computeFactorial(9)
362880

>> computeFactorial(0)
1
"""

def computeFactorial(n):
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result = result * i
    
    return result


# -------------------- TEACHING NOTES --------------------
# Topic: Calculating the Factorial of a Number
#
# 1. What is a factorial?
#    - Factorial means multiplying all whole numbers from 1 up to n.
#    - Written as n! in math.
#
#      Examples:
#          3! = 3 × 2 × 1 = 6
#          5! = 5 × 4 × 3 × 2 × 1 = 120
#
#    - Special rule: 0! = 1
#
# 2. Why check for n == 0?
#    - Because 0! is defined as 1.
#    - This is a math rule, not a Python rule.
#
# 3. Why start result at 1?
#    - Multiplying by 1 does not change the value.
#    - Starting at 0 would make everything 0.
#
# 4. Why loop from 1 to n + 1?
#    - range(1, n) stops at n-1.
#    - range(1, n + 1) includes n.
#
# 5. What does result = result * i do?
#    - It builds the factorial step-by-step.
#
#      Example for n = 4:
#          Start: result = 1
#          i = 1 → result = 1
#          i = 2 → result = 2
#          i = 3 → result = 6
#          i = 4 → result = 24
#
# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> computeFactorial(3)
# 6
#
# Example 2:
# >>> computeFactorial(5)
# 120
#
# Example 3:
# >>> computeFactorial(0)
# 1
#
# Example 4:
# >>> computeFactorial(1)
# 1
#
# Example 5:
# >>> computeFactorial(7)
# 5040
#
# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Off-by-one errors:
#    - Using range(1, n) stops too early.
#    - Must use range(1, n + 1).
#
# 2. Multiplying incorrectly:
#    Wrong:
#        result = n * n
#    Correct:
#        result = result * i
#
# 3. Forgetting the 0! case:
#    - Without handling n == 0, the loop never runs.
#
# 4. Starting result at 0:
#    - This makes all results 0.
#
# 5. Negative numbers:
#    - Factorial is not defined for negative integers.
#    - This exercise does not require handling that case.
#
# ---------------------------------------------------------------


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner (explicit, readable):
#     def computeFactorial(n):
#         if n == 0:
#             return 1
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result
#
# Intermediate (using math.prod):
#     import math
#     def computeFactorial(n):
#         return 1 if n == 0 else math.prod(range(1, n + 1))
#
# Advanced (recursive version):
#     def computeFactorial(n):
#         return 1 if n == 0 else n * computeFactorial(n - 1)
#
# Notes:
# - Recursion is elegant but less beginner-friendly.
# - Iterative version is clearer and avoids recursion limits.
#
# ---------------------------------------------------------------


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "Initialize → Loop → Accumulate → Return" Pattern
#    - Very common in algorithms involving totals or products.
#
# 2. "Special case first" Pattern
#    - Handle edge cases early (like n == 0).
#
# 3. "Off-by-one awareness" Pattern
#    - Understanding how range() works is essential.
#
# 4. "Multiplicative accumulation" Pattern
#    - Similar to summing values, but using multiplication instead.
#
# ---------------------------------------------------------------


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why does factorial start with result = 1?
# A1: Because multiplying by 1 does not change the value.
#
# Q2: Why do we check if n == 0?
# A2: Because 0! is defined as 1.
#
# Q3: What does range(1, n + 1) generate?
# A3: All integers from 1 through n.
#
# Q4: What does result = result * i do?
# A4: It multiplies the running total by each number from 1 to n.
#
# Q5: What is 5! ?
# A5: 120.
#
# ---------------------------------------------------------------