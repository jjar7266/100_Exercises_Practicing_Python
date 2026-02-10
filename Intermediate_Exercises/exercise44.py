# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 44 - Recreation of the len function

"""
Write a function length(L) which takes a list of integers L as a
parameter and returns the number of elements in this list.

Verification tests:

>> length([3, 6, 7, "abde", [1, 3, 5, 7], True])
6

>> length([])
0
"""

import os

os.system('cls')

# Write your code here :-)

def length(L):
    count = 0
    for _ in L:
        count += 1
    return count

print(length([3, 6, 7, "abde", [1, 3, 5, 7], True]))
print(length([]))

# ===============================================================

# Teaching Notes — Exercise 44 (Recreating the len() function)

# ===============================================================

"""
Core Concept:

This exercise reinforces the idea that Python’s built‑in functions are just
abstractions of simple logic. To recreate len(), you manually count how many
items appear in the list.

Mental Model:

Imagine someone hands you a stack of index cards and asks, “How many cards are here?”
You would:
1. 	Start at zero
2. 	Pick up each card one by one
3. 	Add one to your count each time
4. 	Stop when you reach the end
That’s exactly what your loop does.

Why This Matters
This pattern shows up everywhere:
• 	counting items in a list
• 	counting characters in a string
• 	counting occurrences in a dataset
• 	counting nodes in a tree or graph
It’s foundational logic.

Common Mistakes
• 	Forgetting to initialize the counter at 0
• 	Returning inside the loop
• 	Trying to use len() inside the function (defeats the purpose)
• 	Confusing list length with numeric sum

Pattern Summary: This is the simplest form of an accumulator pattern.

count = 0
loop through list:
    count += 1
return count
"""

# Example 1: While-loop version

def length_while(L):
    count = 0
    i = 0
    while i < len(L):  # using len() here is allowed for the loop condition

        count += 1
        i += 1
    return count

# Example 2: Index-based for-loop

def length_index(L):
    count = 0
    for i in range(len(L)):  # again, allowed for iteration

        count += 1
    return count

# Example 3: Pythonic version

def length_builtin(L):
    return len(L)

