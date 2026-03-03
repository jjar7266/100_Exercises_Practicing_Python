# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 58 - Number of Occurrences in a List

"""
Write a function occurrenceCount(L) which takes a list L as a
parameter and returns a list of tuples, where each tuple corresponds to
an element from list L along with its number of occurrences in the list.

Verification tests:

>> occurrenceCount([-4, 8, -3, 2, 1, 2, 7, 9, -3, 8, 1])
[(-4, 1), (8, 2), (-3, 2), (2, 2), (1, 2), (7, 1), (9, 1)]

>> occurrenceCount(["a", 3, 4, "b", "a", 3])
[("a", 2), (3, 2), (4, 1), ("b", 1)]
"""

def occurrenceCount(L):
    counts = {}

    # First pass: count occurrences of each element
    for item in L:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    # Second pass: build result in order of first appearance
    result = []
    seen = set()

    for item in L:
        if item not in seen:
            result.append((item, counts[item]))
            seen.add(item)

    return result


# -------------------- TEACHING NOTES --------------------
# Topic: Counting occurrences and preserving order
#
# 1. Counting with a dictionary:
#       counts = {}
#       for item in L:
#           if item in counts:
#               counts[item] += 1
#           else:
#               counts[item] = 1
#    This pattern appears everywhere in frequency counting problems.
#
# 2. Why two passes?
#    - First pass: compute how many times each element appears.
#    - Second pass: preserve the order of first appearance from the original list.
#
# 3. Using a set to track "seen" elements:
#       seen = set()
#       if item not in seen:
#           ...
#           seen.add(item)
#    This ensures each element is added to the result only once.
#
# 4. Output structure:
#    The result is a list of tuples: (element, count).


# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> occurrenceCount([-4, 8, -3, 2, 1, 2, 7, 9, -3, 8, 1])
# [(-4, 1), (8, 2), (-3, 2), (2, 2), (1, 2), (7, 1), (9, 1)]
#
# Example 2:
# >>> occurrenceCount(["a", 3, 4, "b", "a", 3])
# [("a", 2), (3, 2), (4, 1), ("b", 1)]
#
# Example 3:
# >>> occurrenceCount([])
# []
#
# Example 4:
# >>> occurrenceCount([1, 1, 1])
# [(1, 3)]


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Losing order:
#    Using only counts.keys() or converting to a set loses the original order.
#
# 2. Adding duplicates:
#    Forgetting the "seen" set can cause the same element to appear multiple times.
#
# 3. Confusing element vs. index:
#    We count the elements themselves, not their positions.
#
# 4. Trying to do everything in one pass:
#    It's possible but more complex; two passes are clearer and easier to reason about.


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner (two-pass, explicit):
#     def occurrenceCount(L):
#         counts = {}
#         for item in L:
#             if item in counts:
#                 counts[item] += 1
#             else:
#                 counts[item] = 1
#         result = []
#         seen = set()
#         for item in L:
#             if item not in seen:
#                 result.append((item, counts[item]))
#                 seen.add(item)
#         return result
#
# Intermediate (using collections.OrderedDict in older Python):
#     from collections import OrderedDict
#     def occurrenceCount(L):
#         counts = OrderedDict()
#         for item in L:
#             counts[item] = counts.get(item, 0) + 1
#         return list(counts.items())
#
# Advanced (using dict + get):
#     def occurrenceCount(L):
#         counts = {}
#         for item in L:
#             counts[item] = counts.get(item, 0) + 1
#         result = []
#         seen = set()
#         for item in L:
#             if item not in seen:
#                 result.append((item, counts[item]))
#                 seen.add(item)
#         return result


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Frequency counting with dictionaries.
# 2. Using a second pass to preserve order.
# 3. Using a set to avoid duplicates.
# 4. Separating "compute data" and "format output" into clear steps.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why do we need a second loop over L?
# A1: To preserve the order of first appearance from the original list.
#
# Q2: What does the counts dictionary store?
# A2: For each element, how many times it appears in the list.
#
# Q3: Why do we use a set called seen?
# A3: To ensure each element is added to the result only once.
#
# Q4: What is the shape of the final result?
# A4: A list of tuples: (element, number_of_occurrences).
#
# ---------------------------------------------------------------
