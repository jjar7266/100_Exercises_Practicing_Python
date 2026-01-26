# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 37 - Sum of a list

# ===========================================================
"""
Write a function called calculateSum(L) that takes a list of integers L as
a parameter and returns the sum of the values in this list.

Verification tests:
  >> calculateSum([3,2,6,9,-1,5])
24

  >> calculateSum([-3,-6,0,1,2,7])
1
"""

# ---------------------------------------------------------------
# TEACHING NOTES — Summing values in a list
#
# This exercise uses the "accumulator pattern":
#   1. Start with total = 0
#   2. Loop through each number in the list
#   3. Add each number to the running total
#   4. Return the final total
#
# This teaches how functions process lists step-by-step.
# ---------------------------------------------------------------

# ------------------ METHOD 1 (Teaching Version) ------------------
# Manual loop using the accumulator pattern.
# This shows exactly how the sum is built internally.

# def calculateSum(L):
#     total = 0
#     for num in L:
#         total += num
#     return total


# ------------------ METHOD 2 (Pythonic Version) ------------------
# Once you understand the accumulator pattern, Python provides
# a built-in function that does the same thing cleanly.

def calculateSum(L):
    return sum(L)


# ------------------ VERIFICATION TESTS ------------------
print(calculateSum([3,2,6,9,-1,5]))     # Expected: 24
print(calculateSum([-3,-6,0,1,2,7]))    # Expected: 1


# -------------------- SUMMARY --------------------
# Loop through the list, add each number, return total.
# -------------------------------------------------