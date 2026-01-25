# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 31 - Displaying Patterns

# ===========================================================
"""
Write a program that displays the following numbers on the console:

5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
"""

# Write your code here:

for row in range(8):
    for num in range(5, 21):
        print(num, end=" ")
    print()

# ============================
# Teaching Notes (Exercise 31)
# ============================

# 1. This exercise introduces nested loops, a foundational pattern for
#    generating rows and columns of output (grids, tables, matrices, etc.).

# 2. The outer loop controls how many times the entire line is printed.
#       for row in range(8):
#    This means: repeat the pattern 8 times.

# 3. The inner loop controls what appears inside each line.
#       for num in range(5, 21):
#    This prints numbers from 5 up to 20 (21 is excluded).

# 4. The print(num, end=" ") statement keeps all numbers on the same line.
#    Without end=" ", each number would print on its own line.

# 5. After the inner loop finishes, print() moves to the next line so the
#    next row can begin.

# Summary:
#    - Outer loop = number of rows
#    - Inner loop = content of each row
#    - end=" " keeps output on one line
#    - print() after the inner loop starts a new row
