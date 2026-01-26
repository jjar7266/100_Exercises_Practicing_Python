# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 39 - Adding elements to a dictionary

# ===========================================================

"""
Write a function name addElementDict(key, value, d) that takes three
parameters as input: a dictionary d, a key and it's associated value.
The function should add this key and value to the dictionary d. Finally,
the function should return the modified dictionary d with the new
key-value pair.

Verification tests:

  >> addElementDict("baptitse", 29, {"julien": 14, "laurent": 31})
{"julien": 14, "laurent": 31, "baptitse": 29}

  >> addElementDict("weight", 65.3, {})
{"weight": 65.3}
"""
# ---------------------------------------------------------------
# TEACHING NOTES — Adding elements to a dictionary
#
# Goal:
#   Add a new key/value pair to an existing dictionary and return it.
#
# Strategy:
#   1. Use dictionary assignment:
#          d[key] = value
#      This creates the key if it doesn't exist, or updates it if it does.
#
#   2. Return the modified dictionary.
#
# This exercise reinforces:
#   - how to modify dictionaries inside a function
#   - how return values work
# ---------------------------------------------------------------

# Method 1

# def addElementDict(key, value, d):
#     d[key] = value     # Add or update the key/value pair
#     return d           # Return the modified dictionary

# Method 2 - Pythonic Version

def addElementDict(key, value, d):
    d[key] = value
    return d

print(addElementDict("baptitse", 29, {"julien": 14, "laurent": 31}))
# Expected: {"julien": 14, "laurent": 31, "baptitse": 29}

print(addElementDict("weight", 65.3, {}))
# Expected: {"weight": 65.3}

# -------------------- SUMMARY --------------------
# Add the key/value pair using d[key] = value, return d.
# -------------------------------------------------