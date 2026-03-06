# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 75 — Mutual Recursive Functions

"""
A number n is even if n-1 is odd, and a number n is odd if n-1 is even.
Write two mutually recursive functions isEven(n) and isOdd(n) to determine
whether a number n is even or odd.

Verification tests:
>> isEven(5)
False

>> isOdd(7)
True
"""

# -----------------------------
# Your Code Solution
# -----------------------------

def isEven(n):
    """Return True if n is even using mutual recursion."""
    # Normalize negative numbers to avoid infinite recursion
    if n < 0:
        n = -n
    if n == 0:
        return True
    return isOdd(n - 1)

def isOdd(n):
    """Return True if n is odd using mutual recursion."""
    # Normalize negative numbers to avoid infinite recursion
    if n < 0:
        n = -n
    if n == 0:
        return False
    return isEven(n - 1)


# -----------------------------
# Verification Tests
# -----------------------------

print("isEven(5)  ->", isEven(5))   # Expected: False
print("isOdd(7)   ->", isOdd(7))    # Expected: True
print("isEven(0)  ->", isEven(0))   # Expected: True
print("isOdd(0)   ->", isOdd(0))    # Expected: False
print("isEven(-4) ->", isEven(-4))  # Expected: True
print("isOdd(-9)  ->", isOdd(-9))   # Expected: True


# -----------------------------
# Teaching Notes
# -----------------------------
"""
Mutual recursion occurs when two functions call each other.
Here, isEven() calls isOdd(), and isOdd() calls isEven().

Base cases:
    - 0 is even → isEven(0) = True
    - 0 is not odd → isOdd(0) = False

Recursive cases:
    - n is even if n-1 is odd
    - n is odd if n-1 is even

Why normalize negatives?
    Without converting negative numbers to positive, n would move
    toward negative infinity and never reach the base case.
"""

# -----------------------------
# Alternative Approach (Non‑recursive)
# -----------------------------
"""
def isEven(n):
    return n % 2 == 0

def isOdd(n):
    return n % 2 != 0
"""

