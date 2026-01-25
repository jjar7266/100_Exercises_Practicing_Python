# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 29

# ===========================================================
"""
Write a program that randomly shuffles the elements of a list L.
For example, let's consider the list L = [3, 6, 8, 7, 2, 's', 'ch', 'd'].
"""

# Write your code here:

import random

L = [3, 6, 8, 7, 2, 's', 'ch', 'd']

random.shuffle(L)

print(L)

# ============================
# Teaching Notes (Exercise 29)
# ============================

# 1. The random.shuffle() function randomly reorders the elements of a list.
#    It modifies the list *in place* and does not return a new list.

# 2. Because shuffle() returns None, assigning it to a variable will not
#    give you the shuffled list. You must print the list itself after shuffling.

# 3. Correct usage:
#       random.shuffle(L)
#       print(L)

# 4. Each run produces a different order because the shuffle is random.

# Summary:
#    - Import the random module
#    - Call random.shuffle(list_name)
#    - Print the list to see the shuffled result



