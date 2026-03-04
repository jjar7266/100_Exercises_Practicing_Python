# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 65 - Number of files in a folder

"""
Write a function fileCount(folderPath) which takes the folder path folderPath
as a parameter and returns the number of files contained in the specified folder.

Verification tests:

>> fileCount("test")
****Number of files in test folder****
"""

import os

def fileCount(folderPath):
    try:
        items = os.listdir(folderPath)

        file_count = 0
        for item in items:
            full_path = os.path.join(folderPath, item)
            if os.path.isfile(full_path):
                file_count += 1

        print(f"****Number of files in {folderPath} folder****")
        print(file_count)
        return file_count

    except FileNotFoundError:
        print("Folder not found.")
        return 0


# -------------------- TEACHING NOTES --------------------
# Topic: Counting Files in a Directory
#
# 1. os.listdir(folderPath):
#    Returns a list of all names (files + folders) inside the directory.
#
# 2. os.path.isfile(full_path):
#    Checks whether the item is a file (not a folder).
#
# 3. Joining paths:
#    os.path.join(folderPath, item) ensures correct path formatting.
#
# 4. Error handling:
#    If the folder does not exist, the function prints a message and returns 0.
#
# 5. Only files are counted:
#    Subfolders are ignored unless you extend the function.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# Folder "test" contains:
#   notes.txt
#   data.csv
#   images/   (folder)
#
# >>> fileCount("test")
# ****Number of files in test folder****
# 2
#
# Example 2:
# >>> fileCount("empty_folder")
# ****Number of files in empty_folder folder****
# 0


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Counting folders:
#    os.listdir() returns folders too — must filter with os.path.isfile().
#
# 2. Hidden files:
#    Hidden files (like .DS_Store on macOS) are counted as files.
#
# 3. Trailing slashes:
#    os.path.join() handles paths safely regardless of trailing slashes.
#
# 4. Permissions:
#    If the folder cannot be read, an exception may occur.


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner:
#     def fileCount(folderPath):
#         count = 0
#         for item in os.listdir(folderPath):
#             if os.path.isfile(folderPath + "/" + item):
#                 count += 1
#         return count
#
# Intermediate (my version):
#     def fileCount(folderPath):
#         items = os.listdir(folderPath)
#         count = sum(os.path.isfile(os.path.join(folderPath, i)) for i in items)
#         return count
#
# Advanced (recursive count):
#     def fileCount(folderPath):
#         total = 0
#         for root, dirs, files in os.walk(folderPath):
#             total += len(files)
#         return total


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Using os.listdir() to inspect directories.
# 2. Filtering items with os.path.isfile().
# 3. Building full paths with os.path.join().
# 4. Returning numeric results for folder analysis.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does os.listdir() return?
# A1: A list of names (files and folders) inside the directory.
#
# Q2: How do we check if an item is a file?
# A2: os.path.isfile(full_path)
#
# Q3: What happens if the folder does not exist?
# A3: The function prints "Folder not found." and returns 0.
#
# ---------------------------------------------------------------
