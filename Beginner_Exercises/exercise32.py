# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 32

# ===========================================================
"""
Write a program that creates the variable L and assigns it the list
[3, 6, 9, 12, 15, 18, 21, 24], then creates a new list L1 using
list comprehension that contains the numbers from L divided by 3.
The program should display the list L1 on the console.
"""

# Write your code here:

L = [3, 6, 9, 12, 15, 18, 21, 24]

L1 = [x // 3 for x in L]

print(L1)

# ============================
# Teaching Notes (Exercise 32)
# ============================

# 1. List comprehensions provide a concise way to transform each element
#    of an existing list and build a new list from the results.

# 2. The general pattern is:
#       [expression for item in list]
#    In this exercise, the expression is x // 3 and the list is L.

# 3. Using // (integer division) returns whole numbers instead of floats.
#    Since every element in L is divisible by 3, integer division works cleanly.

# 4. The comprehension:
#       [x // 3 for x in L]
#    loops through each element of L, divides it by 3, and collects the results
#    into a new list L1.

# Summary:
#    - Start with the original list L
#    - Apply a transformation (divide by 3)
#    - Use list comprehension to build L1 in one clean line



