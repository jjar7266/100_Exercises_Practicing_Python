# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 64 - Presence of a Number in a File

"""
Write a function presenceNumber(filePath) which takes the file path
filePath as a parameter and checks if the file contains a number.
The function returns True if the file contains a number and False
otherwise.

Verification tests:
>> presenceNumber("test.txt")
****True or False****
"""

def presenceNumber(filePath):
    try:
        with open(filePath, "r") as file:
            words = file.read().split()

        for word in words:
            if word.isdigit():
                print("****True****")
                return True

        print("****False****")
        return False

    except FileNotFoundError:
        print("File not found.")
        return False


# -------------------- TEACHING NOTES --------------------
# Topic: Detecting Numeric Tokens in Text Files
#
# 1. Splitting file content:
#    file.read().split() breaks the text into words separated by spaces.
#
# 2. Using isdigit():
#    word.isdigit() returns True only if the word contains digits only.
#
# 3. Returning early:
#    As soon as a number is found, the function returns True immediately.
#
# 4. Error handling:
#    If the file does not exist, the function prints a message and returns False.
#
# 5. Definition of "number":
#    The exercise assumes whole numbers only (e.g., "42"), not floats or negatives.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# test.txt contains:
#   hello world 42 python
#
# >>> presenceNumber("test.txt")
# ****True****
#
# Example 2:
# test.txt contains:
#   hello world python
#
# >>> presenceNumber("test.txt")
# ****False****


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Floats are not detected:
#    "3.14".isdigit() → False
#
# 2. Negative numbers are not detected:
#    "-5".isdigit() → False
#
# 3. Words with punctuation fail:
#    "42,".isdigit() → False
#
# 4. Hidden whitespace:
#    Extra spaces do not matter because split() handles them.


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner:
#     def presenceNumber(filePath):
#         file = open(filePath, "r")
#         content = file.read()
#         file.close()
#         for word in content.split():
#             if word.isdigit():
#                 return True
#         return False
#
# Intermediate (your version):
#     def presenceNumber(filePath):
#         with open(filePath, "r") as file:
#             words = file.read().split()
#         for word in words:
#             if word.isdigit():
#                 return True
#         return False
#
# Advanced (Pythonic one-liner):
#     def presenceNumber(filePath):
#         with open(filePath, "r") as file:
#             return any(word.isdigit() for word in file.read().split())


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "Read → Process → Return" workflow.
# 2. Using split() to tokenize text.
# 3. Using isdigit() for numeric detection.
# 4. Early returns to improve efficiency.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does word.isdigit() check?
# A1: That the word contains only digits.
#
# Q2: What does split() do?
# A2: Breaks the file content into a list of words separated by whitespace.
#
# Q3: What happens if no number is found?
# A3: The function returns False.
#
# ---------------------------------------------------------------
