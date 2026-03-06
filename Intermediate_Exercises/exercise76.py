# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 76 — Recreating the join method

"""
Write a function join(L, character) that transforms a list L into a string using
the separator character passed as a parameter.

Verification tests:
>> join(["Hello", "Aurelie"], " ")
"Hello Aurelie"

>> join(["Hi", " How are you?"], ",")
"Hi, How are you?"
"""

def join(L, character):
    """
    Recreate Python's built-in str.join() behavior.
    Takes a list L and a separator character, and returns a single string.
    """
    result = ""
    for i in range(len(L)):
        result += L[i]
        # Add separator only between elements, not after the last one
        if i < len(L) - 1:
            result += character
    return result


# -----------------------------
# Verification Tests
# -----------------------------

print(join(["Hello", "Aurelie"], " "))          # Expected: "Hello Aurelie"
print(join(["Hi", " How are you?"], ","))       # Expected: "Hi, How are you?"
print(join(["a", "b", "c"], "-"))               # Expected: "a-b-c"
print(join(["one"], ","))                       # Expected: "one"
print(join([], ","))                            # Expected: ""


# -----------------------------
# Teaching Notes
# -----------------------------
"""
This exercise recreates the behavior of Python's built-in "separator.join(list)".

Key ideas:
- You build the final string manually.
- You must avoid adding the separator after the last element.
- Using indexing (range + len) makes it easy to detect the last element.

Why not use Python's built-in join?
    Because the goal is to understand how join *works internally*.

Edge cases:
- A list with one element → return that element unchanged.
- An empty list → return an empty string.
"""

# -----------------------------
# Alternative Approach (More Pythonic)
# -----------------------------
"""
def join(L, character):
    return character.join(L)
"""

