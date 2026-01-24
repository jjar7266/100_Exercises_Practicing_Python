# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 23 - Using the format () Method

# ===========================================================
"""
Write a program that formats the string "My name is myName and i am
age years old. I am learning the language languageName"
The program should format this string by assigning the content
of the following variables:
  - myName = "Julien", age = 32, languageName = "Python"

This program will display on the console "My name is Julien and I am 32
years old. I am learning the language Python."
"""

# Write your code here :-)

myName = "Julien"
age = 32
languageName = "Python"

print("My name is {} and I am {} years old. I am learning the language {}.".format(myName, age, languageName))

# ============================
# Teaching Notes (Exercise 23)
# ============================

# 1. The .format() method replaces each {} placeholder in the string
#    with the values passed into .format() in the same order.
#
#    Example pattern:
#       "Hello {}, you are {}.".format(value1, value2)
#
#    value1 → fills the first {}
#    value2 → fills the second {}

# 2. This method is older than f-strings.
#    It’s still useful to understand because:
#       - Some older codebases use it
#       - It works well when building strings dynamically
#       - It supports advanced formatting options

# 3. Order matters.
#    If you change the order of arguments inside .format(),
#    the sentence will change accordingly.

# 4. Named placeholders also exist:
#       "My name is {name}".format(name="Julien")
#    (Not required for this exercise, but good to know.)

# Summary:
#    - {} marks where values go
#    - .format() supplies the values
#    - Order of arguments → order of replacement