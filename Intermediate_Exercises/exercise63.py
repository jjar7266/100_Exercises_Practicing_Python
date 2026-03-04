# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 63 - Delete a Character from a File

"""
Write a function removeChar(filePath, character) which takes the file path
filePath and a character as parameters. The function should remove the
character provided as a parameter from the specified file.

Verification tests:
>> removeChar("test.txt", ",")
****File content without ","****
"""

def removeChar(filePath, character):
    with open(filePath, "r") as file:
        content = file.read()

    new_content = content.replace(character, "")

    with open(filePath, "w") as file:
        file.write(new_content)

    print(f'****File content without "{character}"****')
    print(new_content)
    return new_content


# -------------------- TEACHING NOTES --------------------
# Topic: Modifying File Content
#
# 1. Reading the entire file:
#    file.read() loads the full text into a single string.
#
# 2. Using replace():
#    content.replace(character, "") removes all occurrences of the character.
#
# 3. Writing back to the file:
#    Opening the file in "w" mode overwrites the original content.
#
# 4. Why two open() calls?
#    - First: read the original content.
#    - Second: write the modified content back to the file.
#
# 5. This function modifies the file permanently.
#    For safety, you could write to a new file instead, but the exercise
#    expects in-place modification.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# test.txt contains:
#   Hello, world, this is a test.
#
# >>> removeChar("test.txt", ",")
# ****File content without ","****
# Hello world this is a test.
#
# Example 2:
# >>> removeChar("notes.txt", "e")
# ****File content without "e"****
# (prints the file with all 'e' removed)


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Removing more than intended:
#    replace() removes *every* occurrence of the character.
#
# 2. Removing multi-character strings:
#    replace() works with strings too, but the exercise specifies a single character.
#
# 3. Overwriting the file:
#    Opening with "w" erases the original content before writing.
#
# 4. Case sensitivity:
#    "A" and "a" are different characters.


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner:
#     def removeChar(filePath, character):
#         file = open(filePath, "r")
#         content = file.read()
#         file.close()
#         new_content = content.replace(character, "")
#         file = open(filePath, "w")
#         file.write(new_content)
#         file.close()
#         print(new_content)
#
# Intermediate (your version):
#     def removeChar(filePath, character):
#         with open(filePath, "r") as file:
#             content = file.read()
#         new_content = content.replace(character, "")
#         with open(filePath, "w") as file:
#             file.write(new_content)
#         print(new_content)
#
# Advanced (backup file + safer workflow):
#     import shutil
#     def removeChar(filePath, character):
#         shutil.copy(filePath, filePath + ".bak")
#         with open(filePath, "r") as file:
#             content = file.read()
#         new_content = content.replace(character, "")
#         with open(filePath, "w") as file:
#             file.write(new_content)
#         return new_content


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "Read → Transform → Write" workflow.
# 2. Using replace() for simple text manipulation.
# 3. Overwriting files safely with context managers.
# 4. Returning modified content for further processing.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does content.replace(character, "") do?
# A1: Removes all occurrences of the character from the string.
#
# Q2: Why open the file twice?
# A2: First to read, then to overwrite with modified content.
#
# Q3: What happens if the character is not found?
# A3: The file remains unchanged.
#
# ---------------------------------------------------------------
