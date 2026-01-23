# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 20 - The Values of a Dictionary

# ===========================================================
"""
Write a program that displays on the console the values of the keys
"Apple" and "Banana" from the dictionary...
{"Apple": 3, "Banana": 7, "Kiwi: 1}
"""

# Write your code here :-)

dict = {"Apple": 3, "Banana": 7, "Kiwi": 1}

# Accessing dictionary values:

# Use the syntax dict_name["key"] to retrieve the value stored under that key.

print(dict["Apple"])  # Prints the value associated with "Apple"  -> 3

print(dict["Banana"]) # Prints the value associated with "Banana" -> 7

# ================================================================

# Additional Examples

# 1. Accessing dictionary values using .get()

# .get("key") returns the value if the key exists, or None (or a default) if it doesn't.

# .get() is great when you're not sure if a key exists and want to avoid errors.

print(dict.get("Apple"))    # Returns 3
print(dict.get("Banana"))   # Returns 7

# You can also provide a default value if the key is missing

print(dict.get("Orange", "Not found"))

# ----------------------------------------------------------------

# 2. Looping through specific keys

# Accessing multiple dictionary values using a loop

# useful when you want to print several keys without repeating print statements

# This pattern becomes powerful when you're working with larger dictionaries
# or dynamic key lists. 

keys_to_show = ["Apple", "Banana"]

for key in keys_to_show:
    print(dict[key])   # Prints the value for each key

# ----------------------------------------------------------------------

# 3. Printing key + value together

# This is a clean way to show both the key and its value.

# Printing both the key and its value

print("Apple:", dict["Apple"])
print("Banana:", dict["Banana"])

# ---------------------------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------------------------
# Dictionaries store data as key → value pairs.
# To access a value, use the syntax:
#     dict_name["Key"]
#
# Methods shown in this exercise:
#
# 1. Direct Access
#    - dict["Apple"]
#    - Fast and simple, but raises an error if the key doesn't exist.
#
# 2. Using .get()
#    - dict.get("Apple")
#    - Returns the value or a default if the key is missing.
#    - Safer for uncertain keys.
#
# 3. Looping Through Keys
#    - for key in ["Apple", "Banana"]:
#          print(dict[key])
#    - Useful when accessing multiple keys dynamically.
#
# Key Idea:
# A dictionary lets you retrieve values by using their associated keys.
# Once you know the pattern dict["Key"], you can access any value you need.
# ---------------------------------------------------------------------------
