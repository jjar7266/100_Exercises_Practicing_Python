# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 78 - Recreating the split method

"""
Write a function split(sentence, character) that transforms a sentence into a
list using the separator character.

Verification tests:
>> split("Hello Aurelie", " ")
["Hello", "Aurelie"]

>> split("Hi, how are you?", ",")
["Hi", " how are you?"]
"""

def split(sentence, character):
    # Recreate Python's split() behavior for a single-character separator
    result = []
    current = ""

    for ch in sentence:
        if ch == character:
            result.append(current)
            current = ""
        else:
            current += ch

    # Append the final segment
    result.append(current)

    return result

# -------------------- TEACHING NOTES --------------------
# Topic: Recreating Python's split() method
#
# 1. Manual token building:
#    We accumulate characters into 'current' until we hit the separator.
#
# 2. When the separator is found:
#    We append the current token to the result list and reset it.
#
# 3. End-of-string handling:
#    After the loop, we must append the final token.
#
# 4. Why this works:
#    This mimics how Python splits strings into substrings based on a delimiter.

# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> split("Hello Aurelie", " ")
# ["Hello", "Aurelie"]
#
# Example 2:
# >>> split("Hi, how are you?", ",")
# ["Hi", " how are you?"]
#
# Example 3:
# >>> split("a-b-c-d", "-")
# ["a", "b", "c", "d"]
#
# Example 4:
# >>> split("no-separators-here", ",")
# ["no-separators-here"]

# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to append the last token:
#    Without appending after the loop, the final segment is lost.
#
# 2. Multiple consecutive separators:
#    "a,,b".split(",") → ["a", "", "b"]
#    Our implementation matches this behavior.
#
# 3. Leading/trailing separators:
#    ",hello".split(",") → ["", "hello"]
#    "hello,".split(",") → ["hello", ""]
#
# 4. Only works with single-character separators:
#    Python's split() supports multi-character strings.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     result = []
#     current = ""
#     for ch in sentence:
#         if ch == character:
#             result.append(current)
#             current = ""
#         else:
#             current += ch
#     result.append(current)
#     return result
#
# Intermediate (My implementation):
#     def split(sentence, character):
#         result = []
#         current = ""
#         for ch in sentence:
#             if ch == character:
#                 result.append(current)
#                 current = ""
#             else:
#                 current += ch
#         result.append(current)
#         return result
#
# Advanced (Pythonic):
#     def split(sentence, character):
#         return sentence.split(character)

# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Building strings character-by-character.
# 2. Detecting separators and cutting tokens.
# 3. Appending the final token after the loop.
# 4. Matching Python's behavior for simple split operations.

# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why do we append the last token after the loop?
# A1: Because the loop ends without encountering a separator.
#
# Q2: What happens with consecutive separators?
# A2: We get empty strings between them, just like Python's split().
#
# Q3: Does this version support multi-character separators?
# A3: No — only single-character delimiters.
#
# ---------------------------------------------------------------
