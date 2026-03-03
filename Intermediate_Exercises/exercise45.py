# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 45 - Calculating the average of a list numbers

"""
Write a function averageList(L) which takes a list of integers as a
parameter and returns the average of a list L.

Verification tests:

>> averageList([1, 2, 3, 4, 5, 6, 7])
4.0

>> averageList([3, 0, -1, 5, 6, 9, 17])
5.571428571428571

"""

def averageList(L):
    total = 0
    count = 0

    for num in L:
        total += num
        count += 1

    if count == 0:
        return 0  # or None

    return total / count

print(averageList([1, 2, 3, 4, 5, 6, 7]))
print(averageList([3, 0, -1, 5, 6, 9, 17]))

# ==================================================================

"""
📘 Teaching Notes — Exercise 45: Calculating the Average of a List

1. What this exercise teaches

This problem reinforces three core Python patterns:
• 	Accumulator pattern (building up a total)
• 	Manual counting (when you can’t use len() )
• 	Combining results to compute a final value (total ÷ count)
These patterns appear constantly in real programs, so mastering them is important.

2. Key idea: What is an average?
The average (also called the mean) is:

        average = sum of all numbers / how many numbers

So your function must compute:
• 	the total of the numbers
• 	the count of the numbers
• 	then divide them

3. The accumulator pattern (for total):

This pattern always looks like:

total = 0
for num in L:
    total += num

You start at zero and add each number one at a time.

4. The counter patter (for count)

This pattern always looks like:

count = 0
for num in L:
    count += 1

You start at zero and add one for each item you see.

5. Putting it all together

Once the loop finishes:

    - total holds the sum
    - count holds the number of items

so the average is:

    - total / count

6. Edge case: Empty list

if the list is empty:

    - total = 0
    - count = 0

    - total / count -> division by zero error

A simple fix is:

if count == 0:
    return 0

This keeps the function safe.

# ============================================================

# Alternate Solutions

# =============================================================

# A. Using Python's built-in functions

def averageList(L):
    if len(L) == 0:
        return 0
    return sum(L) / len(L)

# B. Using a while loop: Good for practicing indexing

def averageList(L):
    total = 0
    count = 0
    i = 0

    while i < len(L):
        total += L[i]
        count += 1
        i += 1

    if count == 0:
        return 0

    return total / count

# C. Using a running average (advanced concept)

# This shows how averages can be computed without storing totals:

def averageList(L):
    if len(L) == 0:
        return 0

    avg = 0
    count = 0

    for num in L:
        count += 1
        avg = avg + (num - avg) / count

    return avg
"""







