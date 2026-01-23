# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 19 - Reverse a String

# ===========================================================
"""
Write a program that allows you to reverse a string.
The program should reverse the variable ch containing the phrase
"Hello everyone"
"""

# Write your code here :-)

# Define the original string we want to reverse

# A string is just a sequence of characters stored in order

ch = "Hello everyone"

# Use slicing to reverse the string

# [start:end:step]

# Leaving start and end empty means "use the whole string"

# A step of -1 tell Python to walk through the string backwards

rev_ch = ch[::-1]

# Print the reversed string so we can see the result

print(rev_ch)

# =====================================================================

# Additional Learning Examples

# 1. Reverse using a loop (manual method)

# Builds a new string by prepending characters one by one

reversed_string = ""
for char in ch:
    reversed_string = char + reversed_string

print(reversed_string)

# ---------------------------------------------------------------

# 2. Reverse using the built-in reversed() function

# reversed() returns characters in reverse order, but not as a string

rev2 = "".join(reversed(ch))

print(rev2)

# ------------------------------------------------------------------

# 3. Reverse using a function (reusable and clean)

def reverse_string(text):
    return text[::-1]

print(reverse_string(ch))

# ---------------------------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------------------------
# Reversing a string in Python can be done in several ways, each teaching a
# different concept:
#
# 1. Slicing (text[::-1])
#    - The most Pythonic and concise method.
#    - Uses the slicing syntax [start:end:step].
#    - A step of -1 walks through the string backwards.
#
# 2. Loop Method
#    - Shows how reversing works manually.
#    - Builds a new string by prepending characters.
#    - Good for understanding string manipulation and iteration.
#
# 3. reversed() Function
#    - Uses Python’s built-in reversed() iterator.
#    - Must be combined with "".join() to rebuild a string.
#    - Helps you understand iterators and joining sequences.
#
# 4. Function Wrapper
#    - Encapsulates the logic for reuse.
#    - Encourages writing clean, modular code.
#
# Key Idea:
# A string is a sequence of characters, and reversing it simply means
# reading that sequence from the end back to the beginning. Python gives
# you multiple tools to do this, from low-level loops to high-level slicing.
# ---------------------------------------------------------------------------