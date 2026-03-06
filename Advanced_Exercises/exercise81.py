# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 81 - Palindrome numbers

"""
The largest palindrome number obtained as the product of two-digit
integers is 9009 = 91 x 99.
Write a program that finds the largest palindrome number obtained as the
product of two three-digit integers.

Note: You can use the isPalindrome function from the previous exercise.
"""

def isPalindrome(nbr):
    # Reuse logic from Exercise 80
    s = str(nbr)
    return s == s[::-1] and nbr > 10

def largestPalindromeProduct():
    largest = 0
    a_max = 0
    b_max = 0

    # Loop through all 3-digit numbers (100–999)
    for a in range(100, 1000):
        for b in range(100, 1000):
            product = a * b

            # Check if product is a palindrome and larger than current best
            if product > largest and isPalindrome(product):
                largest = product
                a_max = a
                b_max = b

    return largest, a_max, b_max

# -------------------- TEACHING NOTES --------------------
# Topic: Searching for the largest palindrome product
#
# 1. Brute-force search:
#    We check every product of two 3-digit numbers (100–999).
#    Total combinations: 900 x 900 = 810,000 checks.
#
# 2. Using the previous isPalindrome():
#    Reusing functions is a key programming skill.
#
# 3. Tracking the largest palindrome:
#    We keep a variable 'largest' and update it whenever we find a bigger one.
#
# 4. Returning factors:
#    We also return the pair (a, b) that produced the palindrome.

# -------------------- EXAMPLES --------------------
#
# Example run:
# >>> largestPalindromeProduct()
# (906609, 913, 993)
#
# Meaning:
# 906609 is the largest palindrome made from 913 × 993.

# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to check if product is larger than current largest:
#    Without this, you might return the *first* palindrome, not the largest.
#
# 2. Not reusing isPalindrome():
#    Reinventing the wheel leads to bugs and duplicated logic.
#
# 3. Starting loops at 0 or 1:
#    Only 3-digit numbers (100–999) are allowed.
#
# 4. Returning only the palindrome:
#    Returning the factors is extremely helpful for verification.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     largest = 0
#     for a in range(100, 1000):
#         for b in range(100, 1000):
#             if isPalindrome(a*b):
#                 if a*b > largest:
#                     largest = a*b
#     return largest
#
# Intermediate (My implementation):
#     def largestPalindromeProduct():
#         largest = 0
#         a_max = 0
#         b_max = 0
#         for a in range(100, 1000):
#             for b in range(100, 1000):
#                 product = a * b
#                 if product > largest and isPalindrome(product):
#                     largest = product
#                     a_max = a
#                     b_max = b
#         return largest, a_max, b_max
#
# Advanced (optimized search):
#     - Loop from 999 down to 100
#     - Break early when products become smaller than current largest
#     - Reduces runtime significantly

# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Nested loops for pairwise combinations.
# 2. Tracking maximum values during iteration.
# 3. Reusing helper functions (isPalindrome).
# 4. Brute-force search as a valid strategy for bounded problems.

# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: Why do we check product > largest before updating?
# A1: To ensure we only keep the biggest palindrome found so far.
#
# Q2: Why do we loop from 100 to 999?
# A2: Because the problem specifies three-digit integers.
#
# Q3: What does largestPalindromeProduct() return?
# A3: The largest palindrome AND the two factors that produced it.
#
# ---------------------------------------------------------------
