# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 18 - Sorting a List of Tuples

# ===========================================================
"""
Write a program that sorts a list of tuples, L, in ascending order based
on the second element of each tuple.
The list we will consider in this exercise is:
    - L = [("Apple", 15), ("Banana", 8), ("Strawberry", 12), ("Kiwi", 9), ("Peach", 2)]

    The resulting list L after sorting should be:
    - L = [("Peach", 2), ("Banana", 8), ("Kiwi", 9), ("Strawberry", 12), ("Apple", 15)]

"""

L = [("Apple", 15), ("Banana", 8), ("Strawberry", 12), ("Kiwi", 9), ("Peach", 2)]

#L.sort(key=lambda item: item[1])
#print(L)

def get_number(t):
    return t[1]

L.sort(key=get_number)

print(L)

