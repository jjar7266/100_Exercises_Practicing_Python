# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 48 - List Concatenation
"""
Write a function concatList(L1, L2, L3) which takes three lists L1, L2, L3
as parameters and returns the concatenation of these three lists.

Verification tests:
>> concatList([0, 9, 8], [2, 6, 9], [True, False, "abc"])
[0, 9, 8, 2, 6, 9, True, False, "abc"]

>> concatList([[38, -1], 3, -9], ["xz", "France"], [])
[[38, -1], 3, -9, "xz", "France"]
"""
def concatList(L1, L2, L3):
    return L1 + L2 + L3

print(concatList([0, 9, 8], [2, 6, 9], [True, False, "abc"]))

print(concatList([[38, -1], 3, -9], ["xz", "France"], []))

# ======================================================================
# ------------------------------------------------------------
# Exercise 48 — List Concatenation
# Goal:
#   Write a function concatList(L1, L2, L3) that returns the
#   concatenation of the three lists.
#
# Key Concept:
#   The + operator joins lists together. It does NOT modify
#   the originals — it creates a new list.
#
# Pattern:
#   listA + listB + listC
#
# Why this works:
#   Python evaluates left to right:
#       (L1 + L2) → new list
#       (new list + L3) → final list
#
# Common Mistakes:
#   • Forgetting to return the result
#   • Trying to concatenate non-lists (e.g., integers)
#   • Using append() instead of extend() or +
#
# Alternative Teaching Version:
#   Using extend() shows the mechanics explicitly:
#
#       result = []
#       result.extend(L1)
#       result.extend(L2)
#       result.extend(L3)
#       return result
#
# Verification Tests:
#   concatList([0, 9, 8], [2, 6, 9], [True, False, "abc"])
#       → [0, 9, 8, 2, 6, 9, True, False, "abc"]
#
#   concatList([[38, -1], 3, -9], ["xz", "France"], [])
#       → [[38, -1], 3, -9, "xz", "France"]
# ------------------------------------------------------------




