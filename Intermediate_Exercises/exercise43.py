# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 43 - Recreation of the min function

"""
Write a function minimum(L) which takes a list of integers L as a
parameter and returns the smallest value.

Verification tests:
  
   >> minimum([-9, 2, 4, 1, 8])
-9

   >> minimum([-3, 1, 7, 6, 2, 3])
-3

"""
# ===========================================================

import os

os.system('cls')

# Write your code here :-)

def minimum(L):
    min_value = L[0]
    for num in L[1:]:
        if num < min_value:
            min_value = num
    return min_value

print(minimum([-9, 2, 4, 1, 8]))
print(minimum([-3, 1, 7, 6, 2, 3]))

# ===========================================================
# Teaching Notes — Exercise 43 (Recreating the min() function)
# ===========================================================
#
# Core Concept:
# This exercise uses the classic "best‑so‑far" pattern.
# You start by assuming the first element is the smallest,
# then scan through the list and update your answer whenever
# you find a smaller value.
#
# Why this matters:
# This pattern appears everywhere in programming:
#   - finding the max/min
#   - finding the longest string
#   - finding the highest score
#   - finding the earliest/latest date
#   - finding the smallest positive number
#
# Mental Model:
# If someone handed you a list of numbers on paper and asked
# for the smallest value, you would:
#   1. Look at the first number and assume it's the smallest
#   2. Compare it with the next number
#   3. If the next number is smaller, update your answer
#   4. Repeat until the list is finished
#
# Common Mistakes:
#   - Using ">" instead of "<" (accidentally finding the max)
#   - Forgetting to start with the first element
#   - Returning inside the loop by accident
#   - Not handling empty lists (optional for this exercise)
#
# Pattern Summary:
#   smallest = first element
#   loop through list
#       if current < smallest:
#           update smallest
#   return smallest
#
# This is the same logic as Exercise 40 (max), just reversed.
# ===========================================================

# Alternative Example Solutions

"""
** Full-List Loop: This version compares the first element to itself

def minimum_full_loop(L):
    smallest = L[0]
    for num in L:
        smallest = num
    return smallest

# =============================================================

** While Loop Version

def minimum_while(L):
    smallest = L[0]
    i = 1

    while i < len(L):
        if L[i] < smallest:
            smallest = L[i]
        i += 1

    return smallest

# ============================================================
    
** Defensive Version(handles empty lists)

def minimum_safe(L):
    if not L:
        return None  # or raise ValueError("List is empty")

    smallest = L[0]
    for num in L:
        if num < smallest:
            smallest = num
    return smallest

# ===========================================================

** Pythonic Version

def minimum_pythonic(L):
    return sorted(L)[0]

# Or simply:

def minimum_builtin(L):
    return min(L)
"""