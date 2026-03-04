# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 61 - Reading a file

"""
Write a function readFile(filePath) which takes the full path of the file
filePath as a parameter and returns its content. The content of the file
should be displayed on the console.

Note: for this exercise, you should create a text file with content to test
      your function.

Verification tests:

>> readFile("test.txt")
****File content****
"""

def readFile(filePath):
    with open(filePath, "r") as file:
        content = file.read()
        print("****File content****")
        print(content)
        return content

# -------------------- TEACHING NOTES --------------------
# Topic: Reading Files in Python
#
# 1. Using `with open(...)`:
#    Ensures the file is automatically closed, even if an error occurs.
#
# 2. file.read():
#    Reads the entire file content into a single string.
#
# 3. Printing vs. Returning:
#    - Printing displays the content to the console.
#    - Returning allows the caller to reuse the content later.
#
# 4. File paths:
#    Windows paths should use forward slashes (C:/folder/file.txt)
#    or escaped backslashes (C:\\folder\\file.txt).


# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> readFile("test.txt")
# ****File content****
# Hello world!
#
# Example 2:
# >>> readFile("notes.txt")
# ****File content****
# Line 1
# Line 2
# Line 3


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Incorrect file path:
#    Leads to FileNotFoundError if the path is wrong.
#
# 2. Using print(file):
#    Prints the file object, not its contents.
#
# 3. Forgetting to return content:
#    Not required, but useful for further processing.
#
# 4. Encoding issues:
#    Rare for simple text files, but can occur with special characters.


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner:
#     def readFile(filePath):
#         file = open(filePath, "r")
#         content = file.read()
#         print("****File content****")
#         print(content)
#         file.close()
#         return content
#
# Intermediate (your version):
#     def readFile(filePath):
#         with open(filePath, "r") as file:
#             content = file.read()
#             print("****File content****")
#             print(content)
#             return content
#
# Advanced (with error handling):
#     def readFile(filePath):
#         try:
#             with open(filePath, "r") as file:
#                 content = file.read()
#                 print("****File content****")
#                 print(content)
#                 return content
#         except FileNotFoundError:
#             print("Error: File not found.")


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "Open → Read → Print → Return" workflow.
# 2. Using context managers (`with`) for safe file handling.
# 3. Understanding absolute vs. relative paths.
# 4. Returning data even when printing is the main goal.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does file.read() return?
# A1: A single string containing the entire file content.
#
# Q2: Why is `with open(...)` preferred?
# A2: It automatically closes the file and handles errors safely.
#
# Q3: What happens if the file path is wrong?
# A3: Python raises FileNotFoundError.
#
# ---------------------------------------------------------------
