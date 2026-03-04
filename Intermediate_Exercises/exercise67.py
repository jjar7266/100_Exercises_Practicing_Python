# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 67 - The key with the maximum number of unique values

"""
Write a function maxKeyUniqueValuesDict(d) which takes a dictionary d as a
parameter and returns the key with the highest number of unique values.

Note: in this exercise, we assume that the values of all keys are in the form
of lists.

Verification tests:

>> maxKeyUniqueValuesDict({"a": [9, 10, 9, 7, 3, 1], "b": [5, 3, 2, 2, 2], "c": [1, 1, 1, 1, 1, 1, 8, 2]})
a

>> maxKeyUniqueValuesDict({"dtg": [6, 8, 1], "fgb": [2.5, "a"], "kim": ["p", 3, 3]})
dtg
"""

def maxKeyUniqueValuesDict(d):
    max_key = None
    max_unique_count = -1

    for key, values in d.items():
        unique_count = len(set(values))

        if unique_count > max_unique_count:
            max_unique_count = unique_count
            max_key = key

    print(max_key)
    return max_key


# -------------------- TEACHING NOTES --------------------
# Topic: Counting Unique Values in Dictionary Lists
#
# 1. Using set() to remove duplicates:
#    set(values) keeps only unique elements.
#
# 2. Counting unique values:
#    len(set(values)) gives the number of distinct items.
#
# 3. Tracking the maximum:
#    We compare each key's unique count to the current maximum.
#
# 4. Returning the key:
#    The function returns the key with the highest number of unique values.
#
# 5. Ties:
#    If two keys have the same number of unique values, the first one encountered wins.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# d = {"a": [9, 10, 9, 7, 3, 1], "b": [5, 3, 2, 2, 2], "c": [1, 1, 1, 1, 1, 1, 8, 2]}
# Unique counts:
#   a → {9, 10, 7, 3, 1} → 5
#   b → {5, 3, 2} → 3
#   c → {1, 8, 2} → 3
#
# >>> maxKeyUniqueValuesDict(d)
# a
#
# Example 2:
# d = {"dtg": [6, 8, 1], "fgb": [2.5, "a"], "kim": ["p", 3, 3]}
# Unique counts:
#   dtg → 3
#   fgb → 2
#   kim → 2
#
# >>> maxKeyUniqueValuesDict(d)
# dtg


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to use set():
#    Counting the list directly includes duplicates.
#
# 2. Mixed data types:
#    set() works fine with ints, floats, and strings together.
#
# 3. Empty lists:
#    len(set([])) → 0, which is valid.
#
# 4. Ties:
#    The first key with the maximum unique count is returned.


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     def maxKeyUniqueValuesDict(d):
#         max_key = None
#         max_unique = 0
#         for key in d:
#             unique = len(set(d[key]))
#             if unique > max_unique:
#                 max_unique = unique
#                 max_key = key
#         return max_key
#
# Intermediate (My implementation):
#     def maxKeyUniqueValuesDict(d):
#         max_key = None
#         max_unique_count = -1
#         for key, values in d.items():
#             unique_count = len(set(values))
#             if unique_count > max_unique_count:
#                 max_unique_count = unique_count
#                 max_key = key
#         return max_key
#
# Advanced (returning all keys tied for max):
#     def maxKeyUniqueValuesDict(d):
#         counts = {k: len(set(v)) for k, v in d.items()}
#         max_val = max(counts.values())
#         return [k for k, v in counts.items() if v == max_val]


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Using set() to remove duplicates.
# 2. Looping through dictionary items.
# 3. Tracking maximum values.
# 4. Returning keys based on computed metrics.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does set(values) do?
# A1: Removes duplicates and keeps only unique elements.
#
# Q2: How do we count unique values?
# A2: len(set(values))
#
# Q3: What happens if two keys have the same number of unique values?
# A3: The first key encountered is returned.
#
# ---------------------------------------------------------------
