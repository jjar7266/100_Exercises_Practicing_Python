# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 100 - Separate elements 0 and 1

"""
Write a function separateElements(L) that takes a list L as a parameter
where the elements are either 0 or 1, and separates the 0s from the 1s
by placing the 0s at the beginning of the list and the 1s afterwards.

Verification tests:
>> separateElements([0, 1, 0, 1, 1, 0, 0, 1, 0, 1])
[0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

>> separateElements([1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1])
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
"""

def separateElements(L):
    zeros = L.count(0)
    ones = L.count(1)
    return [0] * zeros + [1] * ones


# -------------------- TEACHING NOTES --------------------
# Topic: Partitioning binary lists
#
# 1. Counting is the simplest and fastest method.
# 2. L.count(0) gives the number of zeros.
# 3. L.count(1) gives the number of ones.
# 4. Rebuilding the list is O(n) and extremely efficient.
# 5. This avoids sorting, which is unnecessary overhead.


# -------------------- EXAMPLES --------------------
#
# >>> separateElements([0, 1, 0, 1, 1, 0, 0, 1, 0, 1])
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
#
# >>> separateElements([1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1])
# [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]


# -------------------- COMMON PITFALLS --------------------
#
# 1. Using sort() — it works, but it's slower and less explicit.
# 2. Using two loops instead of count().
# 3. Forgetting that the list contains ONLY 0s and 1s.
# 4. Returning None instead of a new list.


# -------------------- BEGINNER VERSION --------------------
def separateElements_Beginner(L):
    zeros = []
    ones = []
    for value in L:
        if value == 0:
            zeros.append(0)
        else:
            ones.append(1)
    return zeros + ones


# -------------------- INTERMEDIATE VERSION (my implementation) --------------------
def separateElements_Intermediate(L):
    return [0] * L.count(0) + [1] * L.count(1)


# -------------------- ADVANCED VERSION (two-pointer partitioning) --------------------
def separateElements_Advanced(L):
    L = L[:]  # copy to avoid mutating original
    left = 0
    right = len(L) - 1

    while left < right:
        if L[left] == 0:
            left += 1
        elif L[right] == 1:
            right -= 1
        else:
            L[left], L[right] = L[right], L[left]
            left += 1
            right -= 1

    return L
