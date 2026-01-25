# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 30 Generate a Number Randomly

# ===========================================================
"""
Write a program that randomly returns a number between 20 and 30
"""

# Write your code here:

import random

num = random.randint(20, 30)

print(num)

# ============================
# Teaching Notes (Exercise 30)
# ============================

# 1. The random.randint(a, b) function returns a random integer
#    between a and b, including both endpoints.

# 2. To generate a number between 20 and 30:
#       random.randint(20, 30)

# 3. randint() is part of the random module, so the module must be imported:
#       import random

# 4. Each time the program runs, a different number in the range
#    may be returned.

# Summary:
#    - import random
#    - call random.randint(20, 30)
#    - print the result


