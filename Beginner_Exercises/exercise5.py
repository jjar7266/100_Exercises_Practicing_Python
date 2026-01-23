# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 5

# ===========================================================
"""
Write a sequence of Python instructions to declare a variable var and 
assign it the value "Hello", then the program should check whether the 
variable var is an integer or a string. if it's an integer, the program
should display "Integer" on the console. If it's a string, the program
will display "String".
"""

# Write your code here :-)

var = ("Hello")

if type(var) is str:
    print("String")

elif type(var) is int:
    print("Interger")

else:
    print("other type")
