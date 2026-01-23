# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 13 - Number of Occurrences of an Element

# ===========================================================
"""
Write the instructions that create the L and assign it the value
[3, 2, 2, 1, 9, 1, 2, 3, 7], then calculate the number
of occurrences of the number 1 in the list L.
"""

# Write your code here :-)

L = [3, 2, 2, 1, 9, 1, 2, 3, 7]

count = 0

for num in L:
    if num == 1:
        count += 1

print(count)



