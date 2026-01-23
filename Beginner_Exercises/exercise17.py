# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 17 - Common Elements Between Two Lists

# ===========================================================
"""
Write a program that, given two lists L1 and L2, returns a list L3
containing the common elements between L1 and L2.

For testing, we will take the lists:

L1 = [9, 8, 7, 14, 3, 2, "a", "p", "hello", "b"]
L2 = ["b", 1, 9.2, 6, 3, 9, "p"]
"""

# Write your code here :-)

L1 = [9, 8, 7, 14, 3, 2, "a", "p", "hello", "b"]

L2 = ["b", 1, 9.2, 6, 3, 9, "p"]

L3 = []

for char in L1:
    if char in L2:
        L3.append(char)

print(L3)

# ==============================================================

## 2nd Solution (List Comprehension)

L3 = [char for char in L1 if char in L2]
print(L3)

## 3rd Solution (Set Intersection)

# Convert both lists into sets so we can use set operations.
# The & operator performs a set intersection, which returns only the elements
# that appear in BOTH sets. This automatically removes duplicates and ignores order.
# Finally, convert the resulting set back into a list to match the expected output type.

L3 = list(set(L1) & set(L2))  
print(L3)


