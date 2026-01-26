# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 38 - Removing Duplicates

# ===========================================================
"""
Write a function removeDuplicates(L) that takes a list of integers L as a
parameter and returns the list L without any duplicate elements in
ascending order.

Verification tests:
  >> removeDuplicates([0,3,5,7,3,5,1,-1])
[-1,0,1,3,5,7]

  >> removeDuplicates([0,5,9,10,3.2,1,-3])
[-3,0,1,3.2,5,9,10]
"""
# ======================================================

# TEACHING NOTES - Removing duplicates + sorting
#
# Goal: 
#   - Remove duplicate values from the list
#   - Return the result in ascending order
#
# Strategy:
#   1. Convert the list to a set to remove duplicates
#   2. Convert the set back to a list
#   3. Sort the list in ascending order
#
# Why a set?
#  A set automatically removes duplicates because it cannot
#  contain repeated values.
#
# Why sort afterward?
#  Sets do NOT preserve order, so we sort the list after converting.

# ================================================================

# Method 1 - Manual Loop
"""
def removeDuplicates(L):
    unique = []
    for item in L:
        if item not in unique:
            unique.append(item)
    return sorted(unique)
"""

# Method 2 - Pythonic Version

def removeDuplicates(L):
    return sorted(set(L))

# Verification Tests

print(removeDuplicates([0,3,5,7,3,5,1,-1]))     # Expected: [-1,0,1,3,5,7]
print(removeDuplicates([0,5,9,10,3.2,1,-3]))    # Expected: [-3,0,1,3.2,5,9,10]

# -------------------- SUMMARY --------------------
# Convert list to set to remove duplicates, then sort.
# -------------------------------------------------

# TEACHING NOTES — Breaking down the one‑liner
#
# One‑liner:
#       sorted(set(L))
#
# Breakdown:
#   1. set(L)
#        A set automatically removes duplicates because sets
#        cannot contain repeated values.
#        Example:
#            [0,3,5,7,3,5,1,-1] → {0,1,3,5,7,-1}
#
#   2. sorted(...)
#        The sorted() function takes the set and returns a new list
#        with all elements in ascending order.
#        Example:
#            {0,1,3,5,7,-1} → [-1,0,1,3,5,7]
#
# Why this works:
#   - set() removes duplicates
#   - sorted() puts everything in order
#   - Together, they produce a clean, duplicate‑free, sorted list
#
# This one‑liner is just a compact version of the longer method.
# ---------------------------------------------------------------






