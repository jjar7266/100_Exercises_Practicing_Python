# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 21 - Sum of the values of a Dictionary
# ===========================================================
"""
Write a program that calculates the sum of the values
in the following dictionary:
{"Apple": 15, "Banana": 8, "Strawberry": 12, "Kiwi": 9, "Peach": 2}
"""

# --- Main Solution ----------------------------------------------------------

dict = {"Apple": 15, "Banana": 8, "Strawberry": 12, "Kiwi": 9, "Peach": 2}

# Sum all values in the dictionary
total = sum(dict.values())
print(total)


# --- Additional Learning Examples ------------------------------------------

# 1. Manual accumulator loop
total_manual = 0
for value in dict.values():
    total_manual += value
print(total_manual)

# 2. Looping through keys instead of values
total_keys = 0
for key in dict:
    total_keys += dict[key]
print(total_keys)

# 3. Visualizing the values as a list
values_list = list(dict.values())
print(values_list)

# ---------------------------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------------------------
# Dictionaries store data as key → value pairs. To calculate the sum of all
# values, you can use several approaches:
#
# 1. Using sum() with dict.values()
#    - total = sum(dict.values())
#    - Fast, clean, and the most Pythonic method.
#
# 2. Manual Accumulator Loop
#    - total = 0
#      for value in dict.values():
#          total += value
#    - Helps you understand how summation works internally.
#
# 3. Looping Through Keys
#    - total = 0
#      for key in dict:
#          total += dict[key]
#    - Shows that looping through a dictionary iterates over keys by default.
#
# Key Idea:
# The values of a dictionary can be treated like a list of numbers. Once you
# extract them (using dict.values()), you can apply any numeric operation you
# want — including summing them.
# ---------------------------------------------------------------------------