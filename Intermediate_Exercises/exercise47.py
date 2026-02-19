# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 47 - Capitalization Check

"""
Write a function checkCapitals(sentence) which takes a sentence as a
parameter and checks if the sentence contains at least one uppercase
letter. If that's the case, the function should return True; otherwise, it
should return False

Verification tests:
>> checkCapitals("Vegetables are good for health")
True

>> checkCapitals("this is the best book in python")
False
"""

def checkCapitals(sentence):
    for char in sentence:
        if char.isupper():
            return True
    return False

print(checkCapitals("Vegetables are good for health"))

print(checkCapitals("this is the best book in python"))

# ==========================================================================
"""
📘 Teaching Notes — Exercise 47: Capitalization Check

1. What this exercise teaches

This exercise reinforces several foundational string‑processing skills:
• Scanning a string character by character
• Using .isupper() to detect uppercase letters
• Returning early when a condition is met
• Boolean logic patterns (True/False conditions)

These skills are essential for text validation, password checking,
and general string analysis.

2. Key idea: What counts as uppercase?

Python considers uppercase letters to be:
• A–Z
• Uppercase letters in other alphabets (Unicode aware)

The method char.isupper() automatically handles all valid uppercase characters.

3. The scanning pattern

This is the universal pattern for checking if a string contains something:

    for char in sentence:
        if condition(char):
            return True
    return False

You will reuse this pattern for:
• Checking for digits
• Checking for punctuation
• Checking for vowels
• Checking for forbidden characters
• Password validation rules

4. Why return early?

As soon as an uppercase letter is found, the result is known.
Returning immediately:
• Avoids unnecessary looping
• Makes the function faster
• Keeps the logic clean and readable

5. Alternate Solutions

A. Using any() — Pythonic and compact:

    def checkCapitals(sentence):
        return any(char.isupper() for char in sentence)

B. Using a list comprehension (less efficient but educational):

    def checkCapitals(sentence):
        caps = [char for char in sentence if char.isupper()]
        return len(caps) > 0

C. Using a flag variable (beginner‑friendly):

    def checkCapitals(sentence):
        found = False
        for char in sentence:
            if char.isupper():
                found = True
        return found

6. Common Mistakes

• Using .upper() instead of .isupper()
• Checking only the first character
• Returning inside the loop incorrectly
• Forgetting to return False at the end
• Confusing uppercase letters with titlecase words

7. Pattern Summary

This exercise reinforces the classic boolean‑search pattern:

    scan → test → early return → fallback return

This pattern appears in many real‑world programs, including:
• Input validation
• Searching for matches
• Text filtering
• Password rules
• Data cleaning

"""