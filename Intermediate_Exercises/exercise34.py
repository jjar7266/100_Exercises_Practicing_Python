# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 34 - Mathematical function

# ===========================================================
"""
Write a function named f(a,b,x) that takes three integers a,b and x as
parameters and returns the result of the following function:

f(a,b,x) = a*(x**3) + 2*a*(x**2) + b

Verification tests:
>> f(3,0,1)
9

>> f(0,2,2)
2
"""

# Write your code here :-)

def f(a, b, x):
    return a*(x**3) + 2*a*(x**2) + b

print(f(3, 0, 1))   # Expected: 9
print(f(0, 2, 2))   # Expected: 2

# ============================
# Teaching Notes (Exercise 34)
# ============================

# 1. This exercise introduces writing a function that implements a
#    mathematical formula. The goal is to translate algebra directly
#    into Python syntax.

# 2. The function f(a, b, x) receives three integers and returns the
#    value of the expression:
#         a*(x**3) + 2*a*(x**2) + b

# 3. Python uses ** for exponentiation:
#       x**2 means x squared
#       x**3 means x cubed

# 4. The return statement sends the computed value back to the caller.
#    When testing in VS Code, print() is used to display the result.

# Summary:
#    - Define the function with parameters a, b, x
#    - Translate the algebraic formula into Python
#    - Use print() to verify the results in a script