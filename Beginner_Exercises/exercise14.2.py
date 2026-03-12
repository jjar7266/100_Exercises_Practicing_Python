# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution from the Author: Laurentine K. Masson

# Exercise 14 - Adding Elements to a list

# ===========================================================
"""
Write the instructions that create an empty list L and then add the
integers 10, 25, 30, 45, 90, and the strings "ab", "cd", "ef" to it.
"""

## 1st Method
## Empty List
L = []
## adding elements
L += [10, 25, 30, 45, 90, "ab", "cd", "ef"]
print(L)


## 2nd Method
L = []
elt_to_add = [10, 25, 30, 45, 90, "ab", "cd", "ef"]

for elt in elt_to_add:
    ## add element 'elt'
    L.append(elt)

print(L)

