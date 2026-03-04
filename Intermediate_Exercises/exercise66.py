# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 66 - Write in a file

"""
Write a function writeFile(fileName, text) which takes the file name fileName
and the text that you want to write to the file as parameters.
The function will allow us to have a file containing the text provided as a parameter.

Note: we assume in this exercise that the text file is initially empty.

Verification tests:

>> writeFile("test.txt", "Hello, my name is Gregory and I am 30 years old")
****The file should contain the text provided as a parameter****
"""

def writeFile(fileName, text):
    try:
        with open(fileName, "w") as file:
            file.write(text)

        print("****The file should contain the text provided as a parameter****")
        print(text)
        return text

    except Exception as e:
        print("An error occurred while writing to the file.")
        print(f"Error: {e}")
        return None


# -------------------- TEACHING NOTES --------------------
# Topic: Writing Text to a File
#
# 1. Opening a file in "w" mode:
#    This creates the file if it does not exist, or overwrites it if it does.
#
# 2. Writing text:
#    file.write(text) writes the exact string provided.
#
# 3. No need to close the file manually:
#    The with-statement handles closing automatically.
#
# 4. Overwriting behavior:
#    "w" mode replaces the entire file content. This matches the exercise requirement.
#
# 5. Error handling:
#    A try/except block prevents crashes if the file cannot be written.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> writeFile("test.txt", "Hello world")
# ****The file should contain the text provided as a parameter****
# Hello world
#
# Example 2:
# >>> writeFile("notes.txt", "Python is fun!")
# ****The file should contain the text provided as a parameter****
# Python is fun!


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Overwriting existing files:
#    "w" mode erases previous content. Use "a" to append instead.
#
# 2. Missing file extension:
#    If the user forgets ".txt", Python will still create the file.
#
# 3. Writing non-string data:
#    file.write() requires a string. Convert numbers with str().
#
# 4. File permissions:
#    Writing may fail if the folder is protected.


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     def writeFile(fileName, text):
#         file = open(fileName, "w")
#         file.write(text)
#         file.close()
#
# Intermediate (My implementation):
#     def writeFile(fileName, text):
#         with open(fileName, "w") as file:
#             file.write(text)
#         return text
#
# Advanced (append mode + timestamp):
#     from datetime import datetime
#     def writeFile(fileName, text):
#         with open(fileName, "a") as file:
#             file.write(f"{datetime.now()}: {text}\n")
#         return text


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Using "w" mode to overwrite files.
# 2. Using with open(...) for safe file handling.
# 3. Returning the written text for verification.
# 4. Printing confirmation messages for debugging.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does opening a file in "w" mode do?
# A1: Creates the file or overwrites it if it already exists.
#
# Q2: Why use with open(...)?
# A2: It automatically closes the file after writing.
#
# Q3: What happens if the file cannot be written?
# A3: The function prints an error message and returns None.
#
# ---------------------------------------------------------------
