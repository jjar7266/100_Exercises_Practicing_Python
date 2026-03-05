# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 71 - Trigonometric function

"""
Write a function trigoFunct(x) that takes a parameter x and returns the result
of the function f(x) = cos(x)*sin(x) + sin(x) + 8.

Note: In this exercise, we will be using the math module.

Verification tests:
>> trigoFunct(math.pi/4)
9.207106781186548

>> trigoFunct(math.pi)
8
"""
import math

def trigoFunct(x):
    # Compute each part of the expression for clarity
    cos_x = math.cos(x)
    sin_x = math.sin(x)

    # Apply the formula: cos(x)*sin(x) + sin(x) + 8
    result = (cos_x * sin_x) + sin_x + 8

    return result

# -------------------- TEACHING NOTES --------------------
# Topic: Trigonometric Functions with the math Module
#
# 1. math.cos(x) and math.sin(x):
#    These functions expect x in radians, not degrees.
#    Example: math.sin(math.pi/2) == 1.0
#
# 2. Breaking the expression apart:
#    f(x) = cos(x)*sin(x) + sin(x) + 8
#    You can compute it in one line, but separating the steps
#    improves readability and debugging.
#
# 3. Why radians matter:
#    math.pi represents 180 degrees.
#    math.pi/4 represents 45 degrees.
#
# 4. Floating‑point precision:
#    Trigonometric functions return floating‑point numbers,
#    so results may include long decimal expansions.

# -------------------- EXAMPLES --------------------
#
# Example 1:
# >>> trigoFunct(math.pi/4)
# 9.207106781186548
#
# Example 2:
# >>> trigoFunct(math.pi)
# 8.0
#
# Example 3:
# >>> trigoFunct(0)
# sin(0) = 0, cos(0) = 1
# f(0) = 1*0 + 0 + 8 = 8

# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Using degrees instead of radians:
#    trigoFunct(45) is NOT the same as trigoFunct(math.pi/4).
#
# 2. Forgetting to import math:
#    NameError: name 'math' is not defined
#
# 3. Overwriting math:
#    Avoid naming variables "math".
#
# 4. Expecting exact integers:
#    Floating‑point math often produces long decimals.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     def trigoFunct(x):
#         return math.cos(x) * math.sin(x) + math.sin(x) + 8
#
# Intermediate (My implementation):
#     def trigoFunct(x):
#         cos_x = math.cos(x)
#         sin_x = math.sin(x)
#         return (cos_x * sin_x) + sin_x + 8
#
# Advanced (symbolic math):
#     import sympy as sp
#     x = sp.symbols('x')
#     f = sp.cos(x)*sp.sin(x) + sp.sin(x) + 8
#     sp.simplify(f)

# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Using the math module for trig functions.
# 2. Understanding radians vs. degrees.
# 3. Breaking complex expressions into readable steps.
# 4. Returning floating‑point results.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why does math.sin() expect radians instead of degrees?
# A1: Because Python’s math module follows standard mathematical conventions.
#
# Q2: What is sin(math.pi)?
# A2: 0.0 (approximately).
#
# Q3: What happens if you pass degrees instead of radians?
# A3: You get incorrect results because the input is interpreted as radians.
#
# ---------------------------------------------------------------



