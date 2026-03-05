# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 73

"""
In this exercise, we will revisit the solution from exercise 37, which involves
writing a function calculateSum(L).
The goal of the exercise is to recreate the same function, but this time using a
recursive approach.
"""

def calculateSum_recursive(L):
    # Base case: empty list -> sum is 0
    if len(L) == 0:
        return 0

    # Recursive case:
    # sum of list = first element + sum of the rest
    return L[0] + calculateSum_recursive(L[1:])

# -------------------- TEACHING NOTES --------------------
# Topic: Recursion with lists
#
# 1. Recursion definition:
#    A recursive function calls itself with a smaller version of the problem.
#
# 2. Base case:
#    Every recursive function MUST stop at some point.
#    For a list, the natural stopping point is when the list becomes empty.
#
# 3. Recursive step:
#    Break the list into:
#       - the first element: L[0]
#       - the rest of the list: L[1:]
#
#    Then:
#       sum(L) = L[0] + sum(L[1:])
#
# 4. Why recursion works here:
#    Each call reduces the list size by 1.
#    Eventually, the list becomes empty → base case → recursion unwinds.
#
# 5. Performance note:
#    Recursion is elegant but less efficient than loops in Python.
#    This exercise is about understanding recursion, not optimization.

# -------------------- EXAMPLES --------------------
# >>> calculateSum_recursive([3, 2, 6, 9, -1, 5])
# 24
#
# >>> calculateSum_recursive([-3, -6, 0, 1, 2, 7])
# 1
#
# >>> calculateSum_recursive([])
# 0

# -------------------- COMMON PITFALLS --------------------
# - Forgetting the base case → infinite recursion.
# - Using L.pop(0) instead of slicing → modifies the original list.
# - Confusing L[1:] with L[:-1].
# - Thinking recursion is faster (it’s not in Python).
# - Not understanding that each recursive call returns a value.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     Use a loop and an accumulator:
#         total = 0
#         for num in L:
#             total += num
#         return total
#
# Intermediate (My implementation):
#     Use recursion with a clear base case and recursive step.
#
# Advanced:
#     Add type hints, input validation, and tail‑recursion style (conceptually):
#
#     def calculateSum_recursive(L: list[int]) -> int:
#         if not L:
#             return 0
#         return L[0] + calculateSum_recursive(L[1:])

# -------------------- PATTERNS TO RECOGNIZE --------------------
# - Base case + recursive case structure.
# - Breaking a list into head and tail.
# - Thinking of problems in terms of smaller subproblems.
# - Recursion as an alternative to loops.

# -------------------- MINI-QUIZ --------------------
# Q1: What is the base case for summing a list recursively?
# Q2: Why must the recursive call use L[1:]?
# Q3: What happens if you forget the base case?
# Q4: How does recursion “unwind”?
#
# ---------------------------------------------------------------



