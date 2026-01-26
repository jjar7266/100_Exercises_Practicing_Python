# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 41 - Sum of a Sublist

# ===========================================================
"""
Write the code for the function sumSubList(L, i, j), which takes three parameters
a list L, a starting calculation index i, and an ending calculation index j. The
function should return the sum of the numbers located between indices i and j
in the list.

Verification test:
  >> sumSubList([4,10,12,16,18],2,4)
46

  >> sumSubList([2,4,6,8,10,12],0,2)
12
"""
# ---------------------------------------------------------------
# TEACHING NOTES — Summing a portion of a list
#
# Goal:
#   Return the sum of elements between indices i and j (inclusive).
#
# Strategy:
#   1. Use slicing: L[i:j+1]
#        - Slices are end-exclusive, so we add +1 to include index j.
#
#   2. Use sum() to add the sliced elements.
#
# This teaches:
#   - how slicing works (start inclusive, end exclusive)
#   - how to combine slicing with sum()
# ---------------------------------------------------------------

# Method 1 - Manual Loop

"""
def sumSubList(L, i, j):
    total = 0
    for index in range(i, j + 1):
        total += L[index]
    return total
"""

# Method 2 - Pythonic Version(Using Slicing)

def sumSubList(L, i, j):
    return sum(L[i:j+1])

print(sumSubList([4,10,12,16,18], 2, 4))   # Expected: 46
print(sumSubList([2,4,6,8,10,12], 0, 2))   # Expected: 12

# -------------------- SUMMARY --------------------
# Slice the list from i to j (inclusive) and sum it.
# -------------------------------------------------