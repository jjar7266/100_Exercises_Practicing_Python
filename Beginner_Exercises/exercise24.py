# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 24

# ===========================================================
"""
Write a program that displays the multiplication table of the number 8.
The program should produce the following output:

8 x 0 = 0
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80
"""

# Write your code here :-)

for num in range(0, 11):
    x = num * 8
    print(f"8 x {num} = {x} ")

# ============================
# Teaching Notes (Exercise 24)
# ============================

# 1. A for-loop is perfect for repetitive, patterned output.
#    In this exercise, we need to print 11 lines (0 through 10).

# 2. range(0, 11) generates the sequence:
#       0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#    The loop variable (num) takes each of these values in order.

# 3. Inside the loop, we compute the result of:
#       8 * num
#    and store it in a variable so we can print it.

# 4. The print statement uses string formatting to display:
#       "8 x <num> = <result>"
#    This matches the exact output required by the exercise.

# Summary:
#    - Use a loop to repeat a pattern
#    - Use range() to control how many times it repeats
#    - Compute the multiplication inside the loop
#    - Print each line in the correct format