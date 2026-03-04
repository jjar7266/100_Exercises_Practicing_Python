# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 62 - Number of Occurrences of a Word in a File

"""
Write a function countOccFile(filePath, word) which takes the file path filePath
and a word as parameters. The function should return the number of
occurrences of the word in the file provided as a parameter.

Note: we assume that words are separated by spaces.

Verification tests:

>> countOccFile("test.txt", "the")
****Number of occurrences of "the" in your file****
"""

def countOccFile(filePath, word):
    count = 0
    with open(filePath, "r") as file:
        for line in file:
            words = line.split()
            for w in words:
                if w == word:
                    count += 1

    print(f'****Number of occurrences of "{word}" in your file****')
    print(count)
    return count


# -------------------- TEACHING NOTES --------------------
# Topic: Counting Word Occurrences in a File
#
# 1. Splitting lines:
#    line.split() breaks a line into a list of words using spaces as separators.
#
# 2. Exact match:
#    The comparison w == word checks for exact matches only.
#    "the" is different from "The" or "there".
#
# 3. Case sensitivity:
#    This solution is case-sensitive by default.
#    To make it case-insensitive, convert both sides to lower():
#        if w.lower() == word.lower():
#
# 4. Why iterate line-by-line?
#    It avoids loading the entire file into memory and works for large files.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# test.txt contains:
#   the cat sat on the mat
#   the dog barked
#
# >>> countOccFile("test.txt", "the")
# ****Number of occurrences of "the" in your file****
# 3
#
# Example 2:
# >>> countOccFile("notes.txt", "Python")
# ****Number of occurrences of "Python" in your file****
# 0


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Punctuation:
#    "the," is not equal to "the".
#    You may need to strip punctuation for more advanced exercises.
#
# 2. Case sensitivity:
#    "The" and "the" are different unless normalized.
#
# 3. Word boundaries:
#    "there" contains "the" but is NOT counted.
#
# 4. File not found:
#    A wrong path will raise FileNotFoundError.


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner:
#     def countOccFile(filePath, word):
#         count = 0
#         file = open(filePath, "r")
#         for line in file:
#             for w in line.split():
#                 if w == word:
#                     count += 1
#         file.close()
#         print(count)
#         return count
#
# Intermediate (your version):
#     def countOccFile(filePath, word):
#         count = 0
#         with open(filePath, "r") as file:
#             for line in file:
#                 for w in line.split():
#                     if w == word:
#                         count += 1
#         print(count)
#         return count
#
# Advanced (case-insensitive + punctuation handling):
#     import string
#     def countOccFile(filePath, word):
#         word = word.lower()
#         count = 0
#         with open(filePath, "r") as file:
#             for line in file:
#                 cleaned = line.translate(str.maketrans("", "", string.punctuation))
#                 for w in cleaned.split():
#                     if w.lower() == word:
#                         count += 1
#         print(count)
#         return count


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "Read → Split → Compare → Count" pattern.
# 2. Using nested loops for line-level and word-level processing.
# 3. Normalizing text (lowercasing, stripping punctuation).
# 4. Returning the count while also printing formatted output.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does line.split() return?
# A1: A list of words separated by spaces.
#
# Q2: Why might "the" not match "The"?
# A2: The comparison is case-sensitive unless normalized.
#
# Q3: Why is punctuation a problem?
# A3: "the," is not equal to "the" unless punctuation is removed.
#
# ---------------------------------------------------------------
