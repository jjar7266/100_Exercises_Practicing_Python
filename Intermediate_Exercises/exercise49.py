# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 49 - Calculating the Number of Values in a Dictionary

"""
Write a function valueCountDict(d) which takes a dictionary d as a
parameter and returns the number of values contained in the lists
associated with the keys.

Note: for the purpose of this exercise, it is assumed that all values
associated with keys are in the form of lists.

Verification tests:
>> valueCountDict({"a": [1, 2, 3], "b": [3, "p"], "c": [8]})
6

>> valueCountDict({"Julie": [12, 60.1], "Fred": [26, 75.6], "David": []})
4
"""
def valueCountDict(d):
    total = 0

    for value in d.values():
        total += len(value)

    return total

print(valueCountDict({"a": [1, 2, 3], "b": [3, "p"], "c": [8]}))

print(valueCountDict({"Julie": [12, 60.1], "Fred": [26, 75.6], "David": []}))

# ===========================================================================

# ------------------------------------------------------------
# Exercise 49 — Calculating the Number of Values in a Dictionary
#
# Goal:
#   Write a function valueCountDict(d) that returns the total
#   number of items contained in all the lists stored as values
#   in the dictionary.
#
# Key Concepts:
#   • d.values() returns each value in the dictionary.
#   • In this exercise, every value is guaranteed to be a list.
#   • len(list) gives the number of items in that list.
#   • We accumulate these lengths into a running total.
#
# Pattern:
#   total = 0
#   for value in d.values():
#       total += len(value)
#   return total
#
# Why this works:
#   The loop visits each list once. Since each list may have a
#   different number of elements, we count them individually and
#   add them together. Returning after the loop ensures we count
#   *all* lists, not just the first one.
#
# Common Mistakes:
#   • Using len(d), which counts keys, not list items.
#   • Returning inside the loop (exits too early).
#   • Forgetting to initialize a counter before the loop.
#
# Alternative Teaching Version:
#   You can also use a comprehension with sum():
#
#       return sum(len(v) for v in d.values())
#
#   This is more compact but relies on understanding generator
#   expressions, so the loop version is clearer for beginners.
#
# Verification Tests:
#   valueCountDict({"a": [1, 2, 3], "b": [3, "p"], "c": [8]})
#       → 6
#
#   valueCountDict({"Julie": [12, 60.1], "Fred": [26, 75.6], "David": []})
#       → 4
# ------------------------------------------------------------