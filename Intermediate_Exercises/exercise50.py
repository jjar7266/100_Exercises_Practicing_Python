# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 50 - Concatenation of dictionaries
"""
Write a function concatDict(d1, d2) which takes two dictionaries d1 and 
d2 as parameters and returns the concatenation of these two dictionaries d1 and d2.

Verification tests:
>> concatDict({"a": 3, "b": 6}, {"c": 2, "d": -1})
{"a": 3, "b": 6, "c": 2, "d": -1}

>> concatDict({"d": [2.9, 4.1]}, {"p": []})
{"d": [2.9, 4.1], "p": []}
"""

def concatDict(d1, d2):
    result = d1.copy()      # Make a copy so we don't modify d1
    result.update(d2)       # Add all key/value pairs from d2
    return result           # Return the merged dictionary


# -------------------- TEACHING NOTES --------------------
# Topic: Concatenating (Merging) Dictionaries in Python
#
# 1. Why we copy d1 first:
#    - Using d1.copy() creates a NEW dictionary object.
#    - Prevents accidental modification of the original d1.
#    - Safe practice for reusable functions and predictable behavior.
#
#    Example:
#        d1 = {"a": 1}
#        d2 = {"b": 2}
#        result = d1.copy()
#        # result is now {"a": 1}, separate from d1
#
# 2. How update() works:
#    - result.update(d2) adds all key/value pairs from d2 into result.
#    - If a key exists in BOTH dictionaries, the value from d2 overwrites d1.
#
#    Example (overwrite behavior):
#        d1 = {"x": 10}
#        d2 = {"x": 99}
#        result = d1.copy()
#        result.update(d2)
#        # result → {"x": 99}
#
# 3. Behavior with lists or other mutable values:
#    - update() does NOT deep-copy nested structures.
#    - It copies references, not the underlying data.
#
#    Example:
#        d1 = {"nums": [1, 2]}
#        d2 = {"extra": d1["nums"]}
#        merged = concatDict(d1, d2)
#        # Both dictionaries point to the SAME list object.
#
# 4. This function returns a NEW merged dictionary:
#    - d1 and d2 remain unchanged.
#    - The returned dictionary contains all keys from both.
#
#    Example:
#        d1 = {"a": 1}
#        d2 = {"b": 2}
#        merged = concatDict(d1, d2)
#        # merged → {"a": 1, "b": 2}
#        # d1 and d2 stay the same.
#
# 5. Python 3.9+ alternative (not used here, but good to know):
#       merged = d1 | d2
#    - Same overwrite rules as update()
#    - Very compact, but less explicit for teaching.
#
# -------------------- EXAMPLES --------------------
#
# Example 1: Basic merge
# >>> concatDict({"a": 3, "b": 6}, {"c": 2, "d": -1})
# {"a": 3, "b": 6, "c": 2, "d": -1}
#
# Example 2: Lists as values
# >>> concatDict({"d": [2.9, 4.1]}, {"p": []})
# {"d": [2.9, 4.1], "p": []}
#
# Example 3: Overlapping keys (d2 overwrites d1)
# >>> concatDict({"a": 1, "b": 2}, {"b": 99})
# {"a": 1, "b": 99}
#
# Example 4: Empty dictionary cases
# >>> concatDict({}, {"x": 10})
# {"x": 10}
#
# >>> concatDict({"x": 10}, {})
# {"x": 10}
#
# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to copy d1:
#    - If you do: result = d1
#      then update(result) will ALSO modify d1.
#
# 2. Assuming update() returns a new dictionary:
#      Wrong:
#          merged = d1.update(d2)   # merged becomes None
#      Correct:
#          merged = d1.copy()
#          merged.update(d2)
#
# 3. Expecting deep copies:
#    - update() copies references for nested structures.
#
# 4. Overwriting keys unintentionally:
#    - If both dictionaries share a key, d2 overwrites d1.
#
# 5. Keys must be hashable:
#    - Strings, ints, tuples are fine.
#    - Lists or dicts as keys → TypeError.
#
# ---------------------------------------------------------------


# -------------------- BEGINNER vs. ADVANCED SOLUTIONS --------------------
#
# Beginner (explicit, readable, safe):
#     def concatDict(d1, d2):
#         result = d1.copy()
#         result.update(d2)
#         return result
#
# Intermediate (dict unpacking, Python 3.5+):
#     def concatDict(d1, d2):
#         return {**d1, **d2}
#
# Advanced (Python 3.9+ merge operator):
#     def concatDict(d1, d2):
#         return d1 | d2
#
# Notes:
# - All three methods behave the same for this exercise.
# - The merge operator is the cleanest but less explicit for teaching.
# - Dict unpacking is widely used in real-world codebases.
#
# ---------------------------------------------------------------


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. "Copy → Modify → Return" Pattern
#    - Very common in Python when you want to avoid mutating inputs.
#
# 2. "Overwrite on collision" Pattern
#    - Many Python merge operations follow this rule:
#        - dict.update()
#        - {**d1, **d2}
#        - d1 | d2
#
# 3. "Shallow vs. Deep" Pattern
#    - Python defaults to shallow copies.
#    - Deep merging requires manual logic or copy.deepcopy().
#
# 4. "Functional style" Pattern
#    - Returning new objects instead of mutating inputs is clean and predictable.
#
# ---------------------------------------------------------------


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What happens if you forget to copy d1 before updating?
# A1: d1 gets modified because update() mutates the dictionary in place.
#
# Q2: What does update() return?
# A2: None. It modifies the dictionary directly.
#
# Q3: If both dictionaries share a key, which value wins?
# A3: The value from d2 overwrites the value from d1.
#
# Q4: Does update() deep-copy nested structures?
# A4: No. It copies references (shallow copy).
#
# Q5: What is the most compact modern way to merge dictionaries?
# A5: Using the merge operator: d1 | d2 (Python 3.9+).
#
# ---------------------------------------------------------------