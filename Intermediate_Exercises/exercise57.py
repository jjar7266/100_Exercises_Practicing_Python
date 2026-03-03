# 100 Exercises for Practicing PYTHON

# Author: Laurentine K. Masson

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 57 - Reverse the Order of Words

"""
Write a function reverseSentence(sentence) which takes a sentence as
a parameter and reverses the order of words in the sentence. The function
should return the sentence with the words reversed.

Note: It is assumed that words in a sentence are separated by spaces.

Verification tests:

>> reverseSentence("could you get me a coffee?")
coffee? a me get you could

>> reverseSentence("Apple")
Apple
"""

def reverseSentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

# -------------------- TEACHING NOTES --------------------
# Topic: Reversing the order of words in a sentence
#
# 1. Splitting the sentence:
#       words = sentence.split()
#    Produces a list of words separated by spaces.
#
# 2. Reversing the list:
#       reversed_words = words[::-1]
#    Slicing with -1 reverses the order of elements.
#
# 3. Rebuilding the sentence:
#       " ".join(reversed_words)
#    Joins the reversed list back into a single string.
#
# 4. Punctuation:
#    Punctuation stays attached to the word it belongs to.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> reverseSentence("could you get me a coffee?")
# "coffee? a me get you could"
#
# Example 2:
# >>> reverseSentence("Apple")
# "Apple"
#
# Example 3:
# >>> reverseSentence("Python is fun")
# "fun is Python"


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Reversing characters instead of words:
#    This exercise is about word order, not letter order.
#
# 2. Forgetting to join:
#    Returning the list instead of a string is incorrect.
#
# 3. Using split("") by mistake:
#    That splits characters, not words.
#
# 4. Overthinking punctuation:
#    split() keeps punctuation attached to the word.


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner:
#     def reverseSentence(sentence):
#         words = sentence.split()
#         reversed_words = words[::-1]
#         return " ".join(reversed_words)
#
# Intermediate (using reversed()):
#     def reverseSentence(sentence):
#         return " ".join(reversed(sentence.split()))
#
# Advanced (one-liner):
#     reverseSentence = lambda s: " ".join(s.split()[::-1])


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "Split → Transform → Join" Pattern
#    - Very common in text manipulation.
#
# 2. List slicing with negative steps
#    - A powerful Python technique for reversing sequences.
#
# 3. Word-level vs. character-level operations
#    - Important distinction in string processing.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does split() return?
# A1: A list of words separated by spaces.
#
# Q2: What does words[::-1] do?
# A2: Reverses the order of the list.
#
# Q3: Why do we use join()?
# A3: To rebuild the reversed list into a sentence.
#
# Q4: Does punctuation get separated?
# A4: No, it stays attached to the word.
#
# ---------------------------------------------------------------
