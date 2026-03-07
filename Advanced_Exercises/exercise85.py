# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 85 - Dichotomic Search

"""
Write a function dichotomicSearch(L, elt) that takes as parameters a list L
sorted in ascending order and an element elt. The function should allow us to
find the element elt in the list L using dichotomic search. If the element is
found, the function returns True; otherwise, it returns False.

Verification tests:
>> dichotomicSearch([6, 9, 15, 36, 41, 43, 47], 41)
True

>> dichotomicSearch([-9, -1, 3, 4, 7, 11], 0)
False

Reminder of the dichotomic search algorithm:

Context: In a sorted list L of values, we are trying to determine if a value elt is
present in the L.

Dichotomy search steps:
    - We examine the element in the middle of the list L and compare it to elt.
    - If they are equal, the algorithm stops, and the element is found;
      otherwise, we continue the search in the first or second half of the array.
    - If, in the end, we have reduced the portion of the list to the point that it
    no longer contains any elements, the search stops with a failure: elt is
    not in L.
"""

def dichotomicSearch(L, elt):
    left = 0
    right = len(L) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = L[mid]

        if mid_value == elt:
            return True
        elif elt < mid_value:
            right = mid - 1
        else:
            left = mid + 1

    return False

# -------------------- TEACHING NOTES --------------------
# Topic: Binary (Dichotomic) Search
#
# 1. Works ONLY on sorted lists.
# 2. Repeatedly cuts the search space in half.
# 3. O(log n) time complexity — extremely fast.
#
# Core idea:
#   - Look at the middle element.
#   - If it's the target → success.
#   - If target < middle → search left half.
#   - If target > middle → search right half.
#   - Stop when left > right → not found.

# -------------------- EXAMPLES --------------------
#
# >>> dichotomicSearch([6, 9, 15, 36, 41, 43, 47], 41)
# True
#
# >>> dichotomicSearch([-9, -1, 3, 4, 7, 11], 0)
# False
#
# >>> dichotomicSearch([1, 2, 3, 4, 5], 5)
# True

# -------------------- COMMON PITFALLS --------------------
#
# 1. Forgetting to update left/right correctly.
# 2. Using mid = (left + right) / 2 instead of integer division.
# 3. Trying to use binary search on an unsorted list.
# 4. Infinite loops caused by incorrect boundary updates.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner Version (Linear Search):
def dichotomicSearch_beginner(L, elt):
    for item in L:
        if item == elt:
            return True
    return False


# Intermediate Version (Classic Binary Search):
def dichotomicSearch_intermediate(L, elt):
    left = 0
    right = len(L) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = L[mid]

        if mid_value == elt:
            return True
        elif elt < mid_value:
            right = mid - 1
        else:
            left = mid + 1

    return False


# Advanced Version (Recursive Binary Search):
def dichotomicSearch_advanced(L, elt, left=0, right=None):
    if right is None:
        right = len(L) - 1

    if left > right:
        return False

    mid = (left + right) // 2

    if L[mid] == elt:
        return True
    elif elt < L[mid]:
        return dichotomicSearch_advanced(L, elt, left, mid - 1)
    else:
        return dichotomicSearch_advanced(L, elt, mid + 1, right)

# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Divide-and-conquer.
# 2. Using indices to narrow search space.
# 3. Loop termination when left > right.

# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why must the list be sorted?
# A1: Because binary search relies on ordering to eliminate half the list.
#
# Q2: When does the search fail?
# A2: When left > right.
#
# Q3: What is the time complexity?
# A3: O(log n).
#
# ---------------------------------------------------------------


