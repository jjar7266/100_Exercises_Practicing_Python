# 100 Exercises for Practicing PYTHON

# Author: Laurentine K. Masson

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 54 - Removing Spaces in a Sentence

"""
Write a function removeSpaces(sentence) which takes a sentence as a
string parameter and returns the same sentence without spaces
(if they exist) between words.

Verification tests:
>> removeSpaces("France is beautiful!")
Franceisbeautiful

>> removeSpaces("I will take my bike.")
Iwilltakemybike
"""

def removeSpaces(sentence):
    return "".join(sentence.split())

# -------------------- TEACHING NOTES --------------------
# Topic: Removing characters from a string
#
# 1. split():
#       sentence.split()
#    Splits the sentence into a list of words by removing spaces.
#
# 2. join():
#       "".join(list_of_words)
#    Joins the list back into a single string with NO separator.
#
# 3. Combined pattern:
#       "".join(sentence.split())
#    Removes all spaces between words.
#
# 4. Why this works:
#    - split() removes the spaces
#    - join() glues everything back together
#
# 5. Alternative approach:
#       sentence.replace(" ", "")
#    Also valid, but split+join handles multiple spaces cleanly.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> removeSpaces("Hello world")
# "Helloworld"
#
# Example 2:
# >>> removeSpaces("  spaced   out   words  ")
# "spacedoutwords"   # split() collapses multiple spaces
#
# Example 3:
# >>> removeSpaces("NoSpacesHere")
# "NoSpacesHere"
#
# Example 4:
# >>> removeSpaces("Python is fun!")
# "Pythonisfun!"


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Returning split() directly:
#       return sentence.split()
#    This returns a LIST, not a string.
#
# 2. Forgetting the empty string in join():
#       " ".join(...)  # adds spaces back
#       "".join(...)   # correct
#
# 3. Trying to remove spaces manually with loops:
#    Works, but is unnecessary for this exercise.
#
# 4. Not understanding split():
#    split() removes ALL whitespace, not just single spaces.


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner (explicit, readable):
#     def removeSpaces(sentence):
#         words = sentence.split()
#         result = "".join(words)
#         return result
#
# Intermediate (one-liner):
#     def removeSpaces(sentence):
#         return "".join(sentence.split())
#
# Advanced (manual loop):
#     def removeSpaces(sentence):
#         result = ""
#         for char in sentence:
#             if char != " ":
#                 result += char
#         return result
#
# Notes:
# - split()+join() is the most Pythonic.
# - Beginner version is best for clarity.
# - Manual loop is educational but not necessary.


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "split → transform → join" Pattern
#    - Very common in string manipulation.
#
# 2. Removing characters by omission
#    - Instead of replacing, you rebuild the string without them.
#
# 3. One-liner transformations
#    - Python often allows compact, readable solutions.
#
# 4. Handling multiple spaces
#    - split() automatically collapses them.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does split() do?
# A1: Removes spaces and returns a list of words.
#
# Q2: What does join() do?
# A2: Combines a list of strings into one string.
#
# Q3: Why use "" in join()?
# A3: It tells Python to join the words with no separator.
#
# Q4: What happens to multiple spaces?
# A4: split() collapses them into a single separation.
#
# Q5: Why not return split() directly?
# A5: Because it returns a list, not a string.
#
# ---------------------------------------------------------------




