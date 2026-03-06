# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 82 - Circular prime numbers

"""
Write a function isCircularPrime(nbr) that takes a positive integer nbr as a
parameter and tests whether a number is a circular prime. The function returns
True if the number passed as a parameter is a circular prime and False otherwise.

Reminder: A number is considered a circular prime if its digit rotations are
prime numbers. For example the number 197 is a circular prime because 197,
971, and 719 are prime numbers (the first digit of 197 is moved to the end to get
971, then the 9 is moved to the end of 971 to get 719).
Other examples of circular prime numbers include 19391, 19937, 71, 37, 31, 9377, etc.

Hint: It is advisable to implement a function isPrime(nbr) that checks if a
number is prime, and then use it in isCircularPrime(nbr)

Verification tests:
>> isCircularPrime(9377)
True

>> isCircularPrime(36)
False
"""

def isPrime(nbr):
    # Basic prime check
    if nbr < 2:
        return False
    if nbr == 2:
        return True
    if nbr % 2 == 0:
        return False

    # Check odd divisors up to sqrt(nbr)
    limit = int(nbr ** 0.5) + 1
    for i in range(3, limit, 2):
        if nbr % i == 0:
            return False
    return True


def rotateNumber(nbr):
    # Rotate digits: 197 -> 971 -> 719
    s = str(nbr)
    return int(s[1:] + s[0])


def isCircularPrime(nbr):
    # If the number itself is not prime, stop early
    if not isPrime(nbr):
        return False

    rotation = nbr
    length = len(str(nbr))

    # Generate all rotations
    for _ in range(length - 1):
        rotation = rotateNumber(rotation)
        if not isPrime(rotation):
            return False

    return True


# -------------------- TEACHING NOTES --------------------
# Topic: Circular Prime Numbers
#
# 1. What is a circular prime?
#    A number whose every digit rotation is prime.
#
# 2. Rotations:
#    197 → 971 → 719
#    Rotate by moving the first digit to the end.
#
# 3. Why check the original number first?
#    If nbr isn't prime, it cannot be circular prime.
#
# 4. Why use a helper function?
#    isPrime() and rotateNumber() keep isCircularPrime() clean and readable.

# -------------------- EXAMPLES --------------------
#
# >>> isCircularPrime(9377)
# True
#
# >>> isCircularPrime(36)
# False
#
# >>> isCircularPrime(197)
# True
#
# >>> isCircularPrime(101)
# False   # rotation 011 = 11 (prime), but 101 itself is prime → True
#         # but 110 is NOT prime → overall False

# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to check all rotations:
#    Only checking the first rotation gives wrong results.
#
# 2. Leading zeros after rotation:
#    101 → "011" → int("011") = 11 (valid)
#
# 3. Not checking primality first:
#    Saves time by eliminating non-primes early.
#
# 4. Confusing circular primes with palindromes:
#    They are unrelated concepts.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     - Write isPrime()
#     - Write rotateNumber()
#     - Loop through rotations manually
#
# Intermediate (My implementation):
#     def isCircularPrime(nbr):
#         if not isPrime(nbr):
#             return False
#         rotation = nbr
#         for _ in range(len(str(nbr)) - 1):
#             rotation = rotateNumber(rotation)
#             if not isPrime(rotation):
#                 return False
#         return True
#
# Advanced:
#     - Pre-check digits (no even digits allowed except 2)
#     - Use sieve of Eratosthenes for fast prime lookup

# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Breaking a problem into helper functions.
# 2. Reusing logic (prime checking).
# 3. Rotating digits using string slicing.
# 4. Early returns for efficiency.

# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What makes a number circular prime?
# A1: All its digit rotations must be prime.
#
# Q2: Why check nbr itself first?
# A2: If nbr isn't prime, no rotation can save it.
#
# Q3: How do you rotate digits?
# A3: s[1:] + s[0]
#
# ---------------------------------------------------------------
