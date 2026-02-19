# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 46 - Divisors of an integer

"""
Write a function divisor(n) which takes an integer n as a parameter and
returns a list containing all the positive divisors of n in ascending order.

Verification tests:

>> divisor(3)
[1, 3]

>> divisor(9)
[1, 3, 9]
"""

def divisor(n):
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors

print(divisor(8))

# =======================================================================
"""
📘 Teaching Notes — Exercise 46: Divisors of an Integer

1. What this exercise teaches

This problem reinforces three important programming concepts:
• Iterating over a numeric range
• Using the modulo operator (%) to test divisibility
• Building a list dynamically using the accumulator pattern

These patterns appear frequently in number theory, factorization,
and algorithm design, so mastering them is valuable.

2. Key idea: What is a divisor?

A number i is a divisor of n if:

        n % i == 0

This means:
• i divides n evenly
• there is no remainder
• i is a “clean factor” of n

3. The divisor‑finding pattern

This is the universal pattern for collecting divisors:

    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

You will reuse this structure in:
• prime checking
• perfect number detection
• GCD/LCM algorithms
• factorization problems
• number classification exercises

4. Why the loop goes to n + 1

range(1, n + 1) includes n itself.

Every positive integer is a divisor of itself, so:
• 3 → [1, 3]
• 9 → [1, 3, 9]
• 12 → [1, 2, 3, 4, 6, 12]

Stopping at n ensures the full set of divisors is captured.

5. Edge cases

The exercise assumes positive integers.
Handling negatives or zero is not required.

If you wanted to be defensive, you could add:

    if n <= 0:
        return []

But this is optional and not part of the exercise.

6. Optional enhancements (not required)

A more advanced optimization loops only to sqrt(n):

    for i in range(1, int(n**0.5) + 1):

This reduces time complexity from O(n) to O(√n),
but the simple version is perfect for this exercise.


===============================================================
🔄 Alternate Solutions
===============================================================

A. Using list comprehension (compact but advanced):

    def divisor(n):
        return [i for i in range(1, n + 1) if n % i == 0]

B. Using a while loop (good for indexing practice):

    def divisor(n):
        divisors = []
        i = 1
        while i <= n:
            if n % i == 0:
                divisors.append(i)
            i += 1
        return divisors

C. Optimized sqrt method (advanced):

    def divisor(n):
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sorted(divisors)


===============================================================
⚠️ Common Mistakes
===============================================================

1. Forgetting to include n itself
   Looping to range(1, n) instead of range(1, n + 1).

2. Using append incorrectly
   Writing divisors = divisors.append(i) (append returns None).

3. Starting the loop at 0
   Causes ZeroDivisionError when checking n % 0.

4. Returning inside the loop
   This stops the function early and only returns the first divisor.

5. Not sorting when using the sqrt optimization
   The optimized method collects divisors out of order.


===============================================================
🧠 Pattern Summary

This exercise reinforces the classic pattern:

    result = []
    for item in sequence:
        if condition(item):
            result.append(item)
    return result

This pattern appears everywhere in Python:
• filtering lists
• collecting matches
• building new sequences
• searching for values
• number theory problems

Mastering this pattern gives you a strong foundation for more advanced algorithms.
"""