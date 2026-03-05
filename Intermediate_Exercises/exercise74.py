# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 74

"""
Write a recursive function fibonacciSequence(N) that takes a positive natural
number N positif as a parameter and returns the element at index N of the
Fibonacci sequence.

Reminder: we are interested in the sequence of integers defined by F1 = 1,
F2 = 1 and for any natural number N, F(N+2) = F(N+1) + F(N)

Verification tests:
>> fibonacciSequence(25)
75025

>> fibonacciSequence(45)
1134903170
"""

def fibonacciSequence(N):
    # Base cases
    if N == 1 or N == 2:
        return 1

    # Recursive case
    return fibonacciSequence(N - 1) + fibonacciSequence(N - 2)

# -------------------- TEACHING NOTES --------------------
# Fibonacci is defined recursively, so the code mirrors the math.
#
# Base cases:
#   F1 = 1
#   F2 = 1
#
# Recursive case:
#   F(N) = F(N-1) + F(N-2)
#
# This creates a recursion tree where each call branches into two smaller calls.
# The tree grows quickly, which is why Fibonacci recursion is elegant but slow.
#
# Example:
# fibonacciSequence(5)
# = fibonacciSequence(4) + fibonacciSequence(3)
# = (fibonacciSequence(3) + fibonacciSequence(2)) + (fibonacciSequence(2) + fibonacciSequence(1))
#
# The base cases stop the recursion and allow the tree to unwind.

# -------------------- EXAMPLES --------------------
# >>> fibonacciSequence(5)
# 5
#
# >>> fibonacciSequence(10)
# 55
#
# >>> fibonacciSequence(25)
# 75025


# -------------------- COMMON PITFALLS --------------------
# - Forgetting the base cases → infinite recursion.
# - Using N == 0 as a base case when the exercise defines F1 and F2.
# - Not realizing that Fibonacci recursion is slow for large N.
# - Thinking recursion is the fastest way (it’s not; dynamic programming is faster).


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     Use a loop to build the sequence iteratively.
#
# Intermediate (My implementation):
#     Use direct recursion that mirrors the mathematical definition.
#
# Advanced:
#     Add memoization to avoid repeated calculations:
#
#     def fibonacciSequence(N, memo={}):
#         if N in memo:
#             return memo[N]
#         if N <= 2:
#             return 1
#         memo[N] = fibonacciSequence(N-1, memo) + fibonacciSequence(N-2, memo)
#         return memo[N]


# -------------------- PATTERNS TO RECOGNIZE --------------------
# - Multiple recursive calls per function call.
# - Exponential growth of the recursion tree.
# - Base cases that prevent infinite recursion.
# - Mathematical definitions expressed directly in code.


# -------------------- MINI-QUIZ --------------------
# Q1: Why does Fibonacci recursion branch into two calls?
# Q2: What are the base cases for this exercise?
# Q3: Why does fibonacciSequence(45) take noticeably longer than fibonacciSequence(25)?
# Q4: How does memoization improve performance?
#
# ---------------------------------------------------------------


