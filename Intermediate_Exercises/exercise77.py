# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 77 - Recreating the replace method

"""
Write a function replaceString(sentence, oldWord, newWord) that allows
replacing the oldWord with the word newWord in the string parameter sentence.
The function should return the sentence with the newWord replacing the oldWord.

Verification tests:
>> replaceString("Hello Aurelie", "Aurelie", "Mathilde")
"Hello Mathilde"

>> replaceString("I'm 50 years old", "50", "35")
"Im 35 years old"
"""

def replaceString(sentence, oldWord, newWord):
    # Recreate Python's replace() behavior for simple word replacement

    result = ""
    i = 0

    while i < len(sentence):
        # Check if oldWord matches starting at position 1

        if sentence[i:i+len(oldWord)] == oldWord:
            result += newWord
            i += len(oldWord)
        else:
            result += sentence[i]
            i += 1

    return result

# -------------------- TEACHING NOTES --------------------
# Topic: Recreating Python's replace() method
#
# 1. String slicing:
#    sentence[i:i+len(oldWord)] lets us check if oldWord appears at position i.
#
# 2. Manual replacement:
#    If we detect oldWord, we append newWord to the result string.
#
# 3. Incrementing the index:
#    When a match is found, we skip ahead by len(oldWord).
#    Otherwise, we move forward by one character.
#
# 4. Why this works:
#    This mimics how replace() scans through a string and substitutes matches.

# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> replaceString("Hello Aurelie", "Aurelie", "Mathilde")
# "Hello Mathilde"
#
# Example 2:
# >>> replaceString("I'm 50 years old", "50", "35")
# "Im 35 years old"
#
# Example 3:
# >>> replaceString("aaaaa", "aa", "b")
# "bba"   # Because replacements do not overlap

# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Overlapping matches:
#    "aaaaa" replacing "aa" → "bba"
#    Python's replace() also avoids overlapping matches.
#
# 2. Case sensitivity:
#    "Hello" vs "hello" → no match.
#
# 3. Replacing with an empty string:
#    replaceString("abc", "b", "") → "ac"
#
# 4. oldWord not found:
#    Should return the original sentence unchanged.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     result = sentence.replace(oldWord, newWord)
#     return result
#
# Intermediate (My implementation):
#     def replaceString(sentence, oldWord, newWord):
#         result = ""
#         i = 0
#         while i < len(sentence):
#             if sentence[i:i+len(oldWord)] == oldWord:
#                 result += newWord
#                 i += len(oldWord)
#             else:
#                 result += sentence[i]
#                 i += 1
#         return result
#
# Advanced (multiple replacements + validation):
#     def replaceString(sentence, oldWord, newWord):
#         if oldWord == "":
#             raise ValueError("oldWord cannot be empty.")
#         return newWord.join(sentence.split(oldWord))

# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Scanning through a string with an index.
# 2. Using slicing to detect substrings.
# 3. Building a new string character-by-character.
# 4. Skipping ahead when a match is found.

# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why do we check sentence[i:i+len(oldWord)]?
# A1: To see if oldWord appears starting at index i.
#
# Q2: Why do we increment i by len(oldWord) after a match?
# A2: To skip past the replaced portion and avoid overlapping matches.
#
# Q3: What happens if oldWord is not found?
# A3: The original sentence is returned unchanged.
#
# ---------------------------------------------------------------




