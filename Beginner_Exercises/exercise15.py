# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 15 - List Comprehension

# ===========================================================
"""
Write a program that creates the list L and assigns it the value
[1, 2, 3 ,4, 5, 6, 7, 8, 9, 10], then creates a new list L1 that takes every
third element from the list L.

In this case, we should end up with the following list : [1, 4, 7, 10].
"""
# The goal:
#     - Take every third element from the list.
#     - The elements you want are:
#     -    1(index 0)
#     -    4(index 3)
#     -    7(index 6)
#     -    10(index 9)

# So the pattern is:
# start at index 0, then jump by 3 each time.

# Write your code here :-)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L1 = [L[i] for i in range(0, len(L), 3)]

print(L1)
# ---------------------------------------------------

# [start : stop : step]

## 2nd Solution (Slicing)

L1 = L[0: len(L) : 3]

print(L1)
# --------------------------------------------------

## 3rd Solution (Slicing)

L1 = L[::3]

print(L1)

