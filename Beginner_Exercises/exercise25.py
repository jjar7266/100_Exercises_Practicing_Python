# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 25

# ===========================================================
"""
Write a program that displays the directory where the current
Python script is located
"""

# Write your code here:

import os

directory = os.path.dirname(__file__)
print(directory)

# ============================
# Teaching Notes (Exercise 25)
# ============================

# 1. Python always knows the full path of the script that is running.
#    This path includes both the directory and the filename.

# 2. The built-in variable __file__ stores that full path automatically.
#    You don't create it — Python provides it for every script.

# 3. The os.path.dirname() function takes a full path and returns
#    only the directory portion. This is exactly what the exercise asks for.

# 4. By combining __file__ with os.path.dirname(), we can extract
#    the folder where the current script lives, no matter where it is run from.

# Summary:
#    - __file__ gives the full path of the script
#    - os.path.dirname() extracts the directory
#    - This pattern is essential for real-world projects that load files
#      relative to the script's location (assets, configs, resources, etc.)