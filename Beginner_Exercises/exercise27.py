# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 27

# ===========================================================
"""
Write a program that allows you to retrieve the extension of a file.
"""

# Write your code here:

ext = "photo.jpg"

parts = ext.split(".")

print(parts[1])

# ============================
# Teaching Notes (Exercise 27)
# ============================

# 1. A file extension is the part of a filename that comes after the dot.
#    Example: "photo.jpg" → extension is "jpg".

# 2. Strings can be split into parts using the .split() method.
#    Splitting on "." turns "photo.jpg" into ["photo", "jpg"].

# 3. The extension is the second element of the resulting list,
#    which is accessed using parts[1].

# 4. This method works for simple filenames with one dot.
#    More advanced cases (like "archive.tar.gz") require different handling,
#    but .split() is perfect for beginner-level exercises.

# Summary:
#    - Use .split(".") to separate the filename from its extension.
#    - Access the extension with index 1.