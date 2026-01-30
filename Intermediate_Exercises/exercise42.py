# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 42 - Pattern Creation

# ===========================================================
"""
Write a program that displays the star pyramid below:

*
**
****
******
********
**********
"""
import os

os.system('cls')

# Write your code here :-)

for num in [1, 2, 4, 6, 8, 10]:
    print("*" * num)

# =============================================

# Example 1 - Understanding the pattern

"""
Line 1 -> 1 star
Line 2 -> 2 stars
Line 3 -> 4 stars
Line 4 -> 6 stars
Line 5 -> 8 stars
Line 6 -> 10 stars

This shows the irregular jump at the beginning (1 → 2 → 4), then a steady +2 patern.
"""

# Example 2 - Using a list to represent the pattern

"""
[1, 2, 4, 6, 8, 10]

Looping through this list gives you the exact star counts without needing a formula.
"""

# Example 3 - String multiplication
'''

"*" * 4   → "****"
"*" * 1   → "*"
"*" * 10  → "**********"

This is the key Python trick that makes the pyramid easy.
'''

# TEACHING NOTES
"""
1. Pattern recognition matters more than formulas
You tried to find a mathematical formula — which is great — but the pattern wasn’t clean enough to fit a simple equation.
Real programmers often choose the simplest representation, which in this case was a list.

2. Lists are powerful for irregular patterns
When a pattern doesn’t follow a perfect rule, a list gives you full control:

[1, 2, 4, 6, 8, 10]
You loop through it and print exactly what you want.

3. String multiplication is your friend
Python lets you multiply strings:

"*" * num
This is one of the cleanest ways to generate repeated characters.

4. Loops + lists = flexible pattern printing
This exercise teaches you a core skill:
• 	Loop through a sequence
• 	Use each value to control output
• 	Print repeated characters
This pattern shows up everywhere in beginner and intermediate Python.

SUMMARY BLOCK
Exercise Goal:
Print a star pyramid with irregular line lengths:
1,2,4,6,8,10

Key Concepts Learned:
• 	How to analyze and break down a pattern
• 	How to use a list to represent non‑uniform sequences
• 	How to loop through a list
• 	How to multiply strings to repeat characters
• 	How to build a simple output pattern using loops

Core Insight:
You don’t always need a formula.
Sometimes the simplest, cleanest solution is to store the pattern
directly and loop through it.

"""