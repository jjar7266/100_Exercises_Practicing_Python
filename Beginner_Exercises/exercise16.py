# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 16 - Sorting a String

# ===========================================================
"""
Write the instructions to sort a string in ascending alphabetical order.
For testing, let's take the string c = "france".
The program should output "acefnr"
"""

# Write your code here :-)

c = "france"

test = list(c)
test.sort()

test_result = "".join(test)

print(test_result)

# ================================================================
# 1. 	String → list of characters
# 2. 	Sort the list in place
# 3. 	Join the characters back into a string
# 4. 	Print the final result


