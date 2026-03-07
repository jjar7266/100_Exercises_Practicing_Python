# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 88 - Bubble sort

"""
Write a function ascendingSort(L) that takes a list of integers L as a
parameter and sorts the list in ascending order. The function should
return the list L with integers sorted from the smallest to the largest.

Verification tests:
>> ascendingSort([6, 1, 9, -6, 1, 8, 7])
[-6, 1, 1, 6, 7, 8, 9]

>> ascendingSort([-3, 1, 2, 2.3, 5.3, 7, 9.5])
[-3, 1, 2, 2.3, 5.3, 7, 9.5]
"""

def ascendingSort(L):
    n = len(L)

    # Bubble Sort algorithm
    for i in range(n):
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                # Swap elements
                L[j], L[j + 1] = L[j + 1], L[j]

    return L


# -------------------- TEACHING NOTES --------------------
# Topic: Bubble Sort
#
# 1. Bubble Sort repeatedly compares adjacent elements.
# 2. If they are in the wrong order, they are swapped.
# 3. After each full pass, the largest remaining element "bubbles" to the end.
# 4. Time complexity: O(n^2) — simple but slow for large lists.
#
# Why this works:
#   - Each pass pushes the largest unsorted element to its correct position.
#   - After i passes, the last i elements are already sorted.

# -------------------- EXAMPLES --------------------
#
# ascendingSort([6, 1, 9, -6, 1, 8, 7])
# → [-6, 1, 1, 6, 7, 8, 9]
#
# ascendingSort([-3, 1, 2, 2.3, 5.3, 7, 9.5])
# → [-3, 1, 2, 2.3, 5.3, 7, 9.5]

# -------------------- COMMON PITFALLS --------------------
#
# 1. Forgetting to reduce the inner loop range each pass.
# 2. Forgetting to swap correctly (Python tuple swap is easiest).
# 3. Returning inside the loop by accident.
#
# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------

# Beginner Version (Basic Bubble Sort with explicit swapping)
def ascendingSort_beginner(L):
    n = len(L)
    for i in range(n):
        for j in range(0, n - 1):
            if L[j] > L[j + 1]:
                temp = L[j]
                L[j] = L[j + 1]
                L[j + 1] = temp
    return L


# Intermediate Version (My implementation — optimized inner loop)
def ascendingSort_intermediate(L):
    n = len(L)
    for i in range(n):
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L


# Advanced Version (Bubble Sort with early‑exit optimization)
def ascendingSort_advanced(L):
    n = len(L)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                swapped = True
        if not swapped:
            break  # List is already sorted — exit early
    return L

# 🧠 BUBBLE SORT — MINI QUIZ (COMMENTED OUT FOR NOTES)
#
# Q1.
# What does Bubble Sort compare on each step?
# A: Adjacent elements.
#
# Q2.
# Why is it called “Bubble” Sort?
# A: Because the largest values “bubble” to the end of the list after each pass.
#
# Q3.
# In the intermediate version, why does the inner loop run only to n - i - 1?
# A: Because after each pass, the last i elements are already sorted.
#
# Q4.
# What is the time complexity of Bubble Sort?
# A: O(n^2)
#
# Q5.
# What does the advanced version add that the beginner and intermediate versions do not?
# A: An early‑exit optimization using a swapped flag.
#
# Q6.
# What condition tells you the list is already sorted during a pass?
# A: No swaps occur.
#
# Q7.
# Does Bubble Sort sort in place or create a new list?
# A: It sorts in place (modifies the original list).
#
# Q8.
# What happens if the list is already sorted?
# A:
#   - Beginner version → still does all passes
#   - Intermediate version → still does all passes
#   - Advanced version → stops early
#
# Q9.
# What Python feature makes swapping clean and safe?
# A: Tuple unpacking:
#       L[j], L[j+1] = L[j+1], L[j]
#
# Q10.
# What is the main weakness of Bubble Sort?
# A: It’s slow for large lists because it compares every pair repeatedly.

