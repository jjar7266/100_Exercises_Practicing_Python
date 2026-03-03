# 100 Exercises for Practicing PYTHON

# Author: Laurentine K. Masson

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 55 - Position of an Element in a List

"""
Write a function EltPositionList(L, x) which takes a list of elements L
and an element x as parameters, then returns the index (or indices)
where the element x is located in the list L. The function should return a
list of indices. If the element x is not in the list L, then the program will
display on the console: "Element x is not in this L".

Verification tests:
>> EltPositionList([1, 2, 3, 6, 8, 7, 3], 3)
[2, 6]

>> EltPositionList([6, 8, 9, 1, 3, 7], -1)
Element -1 is not in list [6, 8, 9, 1, 3, 7]
"""

def EltPositionList(L, x):
    positions = []

    for i in range(len(L)):
        if L[i] == x:
            positions.append(i)

    if positions:
        return positions
    else:
        print(f"Element {x} is not in the list {L}")

# -------------------- TEACHING NOTES --------------------
# Topic: Searching for all occurrences of an element in a list
#
# 1. Looping with indices:
#       for i in range(len(L)):
#    This gives access to both the index (i) and the element (L[i]).
#
# 2. Checking for a match:
#       if L[i] == x:
#    When the element matches x, we record the index.
#
# 3. Collecting results:
#       positions.append(i)
#    We store every index where x appears.
#
# 4. Returning after the loop:
#    We must finish scanning the entire list before deciding what to return.
#
# 5. Handling "not found":
#    If the list of positions is empty, we print the required message instead
#    of returning a list.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> EltPositionList([1, 2, 3, 6, 8, 7, 3], 3)
# [2, 6]
#
# Example 2:
# >>> EltPositionList(["a", "b", "c", "a"], "a")
# [0, 3]
#
# Example 3:
# >>> EltPositionList([10, 20, 30], 40)
# Element 40 is not in list [10, 20, 30]
#
# Example 4:
# >>> EltPositionList([], 5)
# Element 5 is not in list []


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Returning too early:
#       return positions
#    If placed inside the loop, it stops after the first match.
#
# 2. Forgetting to append:
#    Checking the element but never storing the index.
#
# 3. Using list.index():
#    This only returns the *first* occurrence, not all of them.
#
# 4. Confusing element with index:
#    L[i] is the element; i is the index.
#
# 5. Not handling the "not found" case:
#    The exercise requires printing a message, not returning [].


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner (explicit and clear):
#     def EltPositionList(L, x):
#         positions = []
#         for i in range(len(L)):
#             if L[i] == x:
#                 positions.append(i)
#         if positions:
#             return positions
#         else:
#             print(f"Element {x} is not in list {L}")
#
# Intermediate (using enumerate):
#     def EltPositionList(L, x):
#         positions = [i for i, value in enumerate(L) if value == x]
#         if positions:
#             return positions
#         else:
#             print(f"Element {x} is not in list {L}")
#
# Advanced (functional style):
#     def EltPositionList(L, x):
#         positions = list(filter(lambda i: L[i] == x, range(len(L))))
#         if positions:
#             return positions
#         else:
#             print(f"Element {x} is not in list {L}")
#
# Notes:
# - enumerate() is the cleanest for index/value loops.
# - Beginner version is best for learning the pattern.


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "Scan → Check → Collect" Pattern
#    - Very common in search problems.
#
# 2. Using indices vs. values
#    - Some problems require the index, not the element.
#
# 3. Post-loop decision making
#    - Only after scanning do we decide what to return.
#
# 4. Multiple matches
#    - Unlike index(), this exercise expects ALL occurrences.
#
# 5. Empty result handling
#    - A required part of many search functions.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why can't we return inside the loop?
# A1: Because we would stop after the first match and miss the others.
#
# Q2: What does positions.append(i) store?
# A2: The index where x appears in the list.
#
# Q3: What does enumerate(L) provide?
# A3: Both the index and the value at the same time.
#
# Q4: What should the function do if x is not found?
# A4: Print the message: "Element x is not in list L".
#
# Q5: Why can't we use L.index(x)?
# A5: It only returns the first occurrence, not all of them.
#
# ---------------------------------------------------------------






