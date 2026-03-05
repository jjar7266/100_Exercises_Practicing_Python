# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 70 - Generate a Password Randomly

"""
Write a function generatePassword(characters, passwordLength) which takes a
list of characters characters and the length of the password
passwordLength as parameters, then randomly generates a password with
the specified length and characters. The function should return the password
as a string.
"""

import random

def generatePassword(characters, passwordLength):
    # Randomly choose characters from the list
    password_chars = [random.choice(characters) for _ in range(passwordLength)]

    # Join list into a final string
    password = "".join(password_chars)

    return password

# -------------------- TEACHING NOTES --------------------
# Topic: Random Password Generation
#
# 1. random.choice():
#    Picks ONE random element from a list.
#    Example: random.choice(['a','b','c']) → 'b'
#
# 2. List comprehension:
#    [random.choice(characters) for _ in range(passwordLength)]
#    This repeats the random selection passwordLength times.
#
# 3. Joining characters:
#    "".join(list_of_chars) converts ['a','b','c'] → "abc"
#
# 4. Why this works:
#    The function does not enforce rules (uppercase, digits, etc.).
#    It simply uses whatever characters the caller provides.
#
# 5. Flexibility:
#    If the caller passes letters, digits, symbols, or any mix,
#    the function will generate a password from that pool.

# -------------------- EXAMPLES --------------------
#
# Example 1:
# chars = ['a','b','c','1','2','3']
# >>> generatePassword(chars, 6)
# 'b2c1a3'
#
# Example 2:
# chars = list("ABC123")
# >>> generatePassword(chars, 4)
# '1A3C'

# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Passing an empty list:
#    random.choice([]) will raise an IndexError.
#
# 2. Passing a negative length:
#    range(-5) produces no characters → returns "".
#
# 3. Forgetting to join:
#    Without join(), you'd return a list instead of a string.
#
# 4. Using random.randint incorrectly:
#    randint gives numbers, not characters — wrong tool for this task.


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     password = ""
#     for i in range(passwordLength):
#         password += random.choice(characters)
#     return password
#
# Intermediate (My implementation):
#     def generatePassword(characters, passwordLength):
#         password_chars = [random.choice(characters) for _ in range(passwordLength)]
#         return "".join(password_chars)
#
# Advanced (validation + cryptographic randomness):
#     import secrets
#     def generatePassword(characters, passwordLength):
#         if not characters:
#             raise ValueError("Character list cannot be empty.")
#         return "".join(secrets.choice(characters) for _ in range(passwordLength))

# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Using random.choice() to pick random elements.
# 2. Using list comprehension to repeat an action N times.
# 3. Joining a list of characters into a string.
# 4. Returning the final password as a string.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does random.choice() do?
# A1: Selects one random element from a list.
#
# Q2: Why do we use join()?
# A2: To convert a list of characters into a single string.
#
# Q3: What happens if characters is empty?
# A3: random.choice() raises an IndexError.
#
# ---------------------------------------------------------------




