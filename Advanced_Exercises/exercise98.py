# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 98 - Ordering a dictionary by key

"""
Write a function orderDict(d) that takes a dictionary d as a parameter
and returns a dictionary ordered in ascending order based on the keys
of the dictionary.

Guideline: the keys of the dictionary d should not be a mix of strings and numbers

Verification tests:
>> orderDict({"c": 3, "a": 9, "e": 1})
{"a": 9, "c": 3, "e": 1}

>> orderDict({8: 9, 2: 3, 9: 11})
{2: 3, 8: 9, 9: 11}
"""

def orderDict(d):
    # Safety check: keys must be all strings OR all numbers
    keys = list(d.keys())
    if not all(isinstance(k, type(keys[0])) for k in keys):
        raise TypeError("Dictionary keys must be of the same type (all strings or all numbers).")

    # Sort keys and rebuild dictionary
    sorted_keys = sorted(d)
    return {key: d[key] for key in sorted_keys}


# -------------------- TEACHING NOTES --------------------
# Topic: Sorting dictionaries by key
#
# 1. sorted(d) returns the keys in sorted order.
# 2. Rebuilding the dictionary preserves the sorted order (Python 3.7+).
# 3. The exercise requires rejecting mixed key types.
# 4. Returning a new dictionary avoids mutating the original.


# -------------------- EXAMPLES --------------------
#
# >>> orderDict({"c": 3, "a": 9, "e": 1})
# {'a': 9, 'c': 3, 'e': 1}
#
# >>> orderDict({8: 9, 2: 3, 9: 11})
# {2: 3, 8: 9, 9: 11}


# -------------------- COMMON PITFALLS --------------------
#
# 1. Forgetting that Python cannot compare strings and numbers.
# 2. Sorting items instead of keys.
# 3. Mutating the original dictionary.
# 4. Returning a list instead of a dictionary.


# -------------------- BEGINNER VERSION --------------------
def orderDict_Beginner(d):
    keys = list(d.keys())
    if not all(isinstance(k, type(keys[0])) for k in keys):
        raise TypeError("Dictionary keys must be of the same type.")

    sorted_keys = sorted(keys)
    new_dict = {}
    for key in sorted_keys:
        new_dict[key] = d[key]
    return new_dict


# -------------------- INTERMEDIATE VERSION (my implementation) --------------------
def orderDict_Intermediate(d):
    keys = list(d.keys())
    if not all(isinstance(k, type(keys[0])) for k in keys):
        raise TypeError("Dictionary keys must be of the same type.")

    return {k: d[k] for k in sorted(d)}


# -------------------- ADVANCED VERSION (adds type enforcement + docstring) --------------------
def orderDict_Advanced(d):
    """
    Orders a dictionary by ascending key order.
    Keys must all be the same type (all str or all int/float).
    """
    keys = list(d.keys())
    if not keys:
        return {}

    first_type = type(keys[0])
    if not all(isinstance(k, first_type) for k in keys):
        raise TypeError("Mixed key types are not allowed.")

    return {k: d[k] for k in sorted(keys)}
