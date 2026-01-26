# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 40 - Recreation of the max function

# ===========================================================

"""
Write a function maximum(L) that takes a list of integers as a parameter
and returns the largest value.

Note: The idea is not to use the already available max() function in
Python.

Verification tests:
  >> maximum([-9,2,4,1,8])
8

  >> maximum([-3,1,7,6,2,3])
7
"""
# ---------------------------------------------------------------
# TEACHING NOTES — Recreating the max() function
#
# Goal:
#   Look through the list and find the largest value manually.
#
# Strategy (Best-So-Far Pattern):
#   1. Assume the first element is the maximum.
#   2. Loop through the list.
#   3. Compare each number to the current maximum.
#   4. If the number is larger, update the maximum.
#   5. Return the final maximum after the loop ends.
#
# This teaches:
#   - comparison logic
#   - how to track values across a loop
#   - how built-in functions like max() work internally
# ---------------------------------------------------------------

# Method 1

"""
def maximum(L):
    # Start by assuming the first element is the largest

    max_value = L[0]

    # Check every number in the list

    for num in L:
        if num > max_value:
            max_value = num

    return max_value
"""

# Method 2 - Pythonic Version
# This skips re-checking the first element, but the logic is identical.

def maximum(L):
    max_value = L[0]
    for num in L[1:]:
        if num > max_value:
            max_value = num
    return max_value

print(maximum([-9,2,4,1,8]))      # Expected: 8
print(maximum([-3,1,7,6,2,3]))    # Expected: 7

# -------------------- SUMMARY --------------------
# Track the largest value seen so far and return it.
# -------------------------------------------------

