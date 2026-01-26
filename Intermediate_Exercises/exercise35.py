# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 35 - Presence of an element in a list

# ===========================================================
"""
Write a function named CheckPresence(a,L) that takes a list L and an
element a as parameters. The function returns True if the element a
exits in the list L, and False if the element a does not exist in the list L.

Verification tests:

>> CheckPresense(2,[1,2,3,4,5,6])
True

>> CheckPresense(-1,[3,6,9,7,"abcr"])
False
"""
# ==============================================================

# The manual loop

"""
def CheckPresence(a, L):
    for element in L:
        if element == a:
            return True
    return False
"""
    
# The Pythonic Version

def CheckPresence(a, L):
    return a in L

print(CheckPresence(2, [1, 2, 3, 4, 5, 6]))
print(CheckPresence(-1, [3, 6, 9, 7, "abcr"]))

# Example saving the return value to a variable named result

result = CheckPresence(5, [1, 2, 3,  4, 5])
print(result)

# ---------------------------------------------------------------
# TEACHING NOTES — Understanding return vs print
#
# This function uses `return`, not `print`. That means:
#   - `return` sends a value *back* to the caller
#   - but it does NOT display anything on the screen
#
# If we want to SEE the result, we must print the function call:
#       print(CheckPresence(2, [1,2,3,4,5]))
#
# Why? Because:
#   - `return` = gives back a value for later use
#   - `print`  = shows the value to the user
#
# This makes the function reusable in other code, not just for display.
# ---------------------------------------------------------------

# -------------------- SUMMARY --------------------
# The function checks if a value exists in a list.
# It returns True or False, and we print the call
# if we want to see the result on screen.
# -------------------------------------------------

