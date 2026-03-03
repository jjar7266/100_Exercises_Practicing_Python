# 100 Exercises for Practicing PYTHON

# Author: Laurentine K. Masson

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 56 - Filter words by length

"""
Write a function filterWords(sentence, minLength) which takes a
sentence as a parameter and filters out words with a length strictly
less than the parameter minLength. The function should return the
same sentence without the filtered words.

Note: It is assumed that words in a sentence are separated by spaces.

Verification tests:
>> filterWords("Hello how are you?", 4)
Hello you?

>> filterWords("Where do you come from?", 5)
Where from?
"""

def filterWords(sentence, minLength):
    result = []
    words = sentence.split()

    for word in words:
        if len(word) >= minLength:
            result.append(word)
    return " ".join(result)

# -------------------- TEACHING NOTES --------------------
# Topic: Filtering items in a list based on a condition
#
# 1. Splitting the sentence:
#       words = sentence.split()
#    This converts the sentence into a list of individual words.
#
# 2. Filtering condition:
#       len(word) >= minLength
#    Only words meeting this requirement are kept.
#
# 3. Collecting results:
#       result.append(word)
#    We build a new list containing only the valid words.
#
# 4. Rebuilding the sentence:
#       " ".join(result)
#    Joins the filtered words back into a single string.
#
# 5. Punctuation:
#    Punctuation remains attached to words because split() does not remove it.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> filterWords("Hello how are you?", 4)
# "Hello you?"
#
# Example 2:
# >>> filterWords("Where do you come from?", 5)
# "Where from?"
#
# Example 3:
# >>> filterWords("A quick brown fox jumps", 5)
# "quick brown jumps"
#
# Example 4:
# >>> filterWords("tiny words go", 4)
# ""   # All words filtered out → empty string


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Returning inside the loop:
#    This stops the function after the first word.
#
# 2. Forgetting to append:
#    Checking the condition but never storing the word.
#
# 3. Using replace() incorrectly:
#    This is a filtering problem, not a character removal problem.
#
# 4. Misunderstanding punctuation:
#    "you?" counts as length 4 because punctuation is part of the word.
#
# 5. Forgetting to join:
#    Returning the list instead of a sentence is incorrect.


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner (explicit loop):
#     def filterWords(sentence, minLength):
#         result = []
#         for word in sentence.split():
#             if len(word) >= minLength:
#                 result.append(word)
#         return " ".join(result)
#
# Intermediate (list comprehension):
#     def filterWords(sentence, minLength):
#         return " ".join([w for w in sentence.split() if len(w) >= minLength])
#
# Advanced (functional style):
#     def filterWords(sentence, minLength):
#         return " ".join(filter(lambda w: len(w) >= minLength, sentence.split()))
#
# Notes:
# - Beginner version is the clearest for learning.
# - List comprehension is the most Pythonic.
# - Functional version is concise but less readable for beginners.


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "Split → Filter → Join" Pattern
#    - Extremely common in text processing.
#
# 2. Filtering based on conditions
#    - A core skill for list manipulation.
#
# 3. Rebuilding transformed sequences
#    - join() is the standard way to reconstruct strings.
#
# 4. Handling edge cases
#    - If all words are filtered out, the result is an empty string.
#
# 5. Punctuation as part of tokens
#    - split() does not strip punctuation, so filtering includes it.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does split() return?
# A1: A list of words separated by spaces.
#
# Q2: Why is the return placed after the loop?
# A2: Because we must finish filtering all words before joining them.
#
# Q3: What happens to punctuation?
# A3: It stays attached to the word and counts toward its length.
#
# Q4: What does join() do?
# A4: Rebuilds the filtered list of words into a sentence.
#
# Q5: What happens if no words meet the minimum length?
# A5: The function returns an empty string.
#
# ---------------------------------------------------------------
