# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 59 - Union of lists without duplication

"""
Write a function unionList(L1, L2, L3) which takes three lists of integers
L1, L2, and L3 as parameters, and returns a list in ascending order that
represents the union of these three lists without any duplicate numbers.

Verification tests:

>> unionList([3, 6, 9, 3], [1, 0, 3], [12, 6, 0])
[0, 1, 3, 6, 9, 12]

>> unionList([7, 44, -3], [], [7, 2, 7])
[-3, 2, 7, 44]
"""

def unionList(L1, L2, L3):
    combined = L1 + L2 + L3
    unique_values = set(combined)
    return sorted(unique_values)

# -------------------- TEACHING NOTES --------------------
# Topic: Union of multiple lists without duplicates
#
# 1. Combining lists:
#       combined = L1 + L2 + L3
#    This creates one long list containing all elements.
#
# 2. Removing duplicates:
#       unique_values = set(combined)
#    A set automatically removes duplicate items.
#
# 3. Sorting the result:
#       sorted(unique_values)
#    Returns a new list in ascending order.
#
# 4. Why sets?
#    Sets are ideal for uniqueness problems and run in O(1) average lookup time.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> unionList([3, 6, 9, 3], [1, 0, 3], [12, 6, 0])
# [0, 1, 3, 6, 9, 12]
#
# Example 2:
# >>> unionList([7, 44, -3], [], [7, 2, 7])
# [-3, 2, 7, 44]
#
# Example 3:
# >>> unionList([], [], [])
# []
#
# Example 4:
# >>> unionList([5], [5], [5])
# [5]


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to sort:
#    The exercise requires ascending order.
#
# 2. Using list.append() incorrectly:
#    You must combine lists, not append lists inside lists.
#
# 3. Trying to remove duplicates manually:
#    Using a set is simpler and more efficient.
#
# 4. Confusing union with intersection:
#    Union keeps all unique elements; intersection keeps only shared ones.


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner:
#     def unionList(L1, L2, L3):
#         combined = L1 + L2 + L3
#         unique_values = set(combined)
#         return sorted(unique_values)
#
# Intermediate (using unpacking):
#     def unionList(*lists):
#         combined = []
#         for lst in lists:
#             combined.extend(lst)
#         return sorted(set(combined))
#
# Advanced (one-liner):
#     unionList = lambda *L: sorted(set().union(*L))


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "Combine → Deduplicate → Sort" Pattern
#    Very common in data cleaning and preprocessing.
#
# 2. Using sets for uniqueness
#    A core Python technique for removing duplicates.
#
# 3. Converting between list and set
#    Lists preserve order; sets enforce uniqueness.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why convert to a set?
# A1: To remove duplicate values efficiently.
#
# Q2: Why convert back to a list?
# A2: Because sets cannot be sorted directly in place.
#
# Q3: What does sorted() return?
# A3: A new list in ascending order.
#
# Q4: What is the union of lists?
# A4: All unique elements from all lists.
#
# ---------------------------------------------------------------
