# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 26

# ===========================================================
"""
Write a program that allows you to remove an element from a list.
Let's consider the list L = [1, 2, 3, 4, 5] and we want to remove the
number 1
"""

# Write your code here:

L = [1, 2, 3, 4, 5]

L.remove(1)

print(L)

# ============================
# Teaching Notes (Exercise 26)
# ============================

# 1. The list L contains the values [1, 2, 3, 4, 5].
#    The exercise asks to remove the *value* 1, not the first element by index.

# 2. The list method .remove() deletes the first occurrence of a given value.
#    It searches the list for that value and removes it if found.

# 3. After calling L.remove(1), the list becomes:
#       [2, 3, 4, 5]

# 4. Printing the list confirms the modification.

# Summary:
#    - Use .remove() when you want to delete an element by its value.
#    - Use .pop() or del when you want to delete by index.