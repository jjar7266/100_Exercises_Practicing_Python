# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 72

"""
Write a program that stores in a list L all positive integers with three digits in
the form abc, such that for each integer, the sum of it's digits a+b+c is a divisor
of the product of its digits a*b*c.
The program should display the list containing these integers at the end.

For example: the number 514 satisfies the property, as 5+1+4 = 10 is a
divisor of 5*1*4 = 20
"""

def findSpecialIntegers():
    L = []

    # Loop through all 3-digit integers: 100 to 999
    for n in range(100, 1000):
        # Extract digits
        a = n // 100            # hundreds digit
        b = (n // 10) % 10      # tens digit
        c = n % 10              # ones digit

        digit_sum = a + b + c
        digit_product = a * b * c

        # Avoid division by zero (if any digit is zero, product becomes zero)
        if digit_sum == 0:
            continue

        # Check if digit_sum divides digit_product
        if digit_product % digit_sum == 0:
            L.append(n)

    return L

# Display the result
if __name__ == "__main__":
    print(findSpecialIntegers())

# -------------------- TEACHING NOTES --------------------
# Topic: Digit decomposition + divisibility conditions
#
# 1. Extracting digits:
#    For a 3-digit number abc:
#       a = n // 100
#       b = (n // 10) % 10
#       c = n % 10
#
# 2. Why check digit_sum == 0?
#    If any digit is zero, the product becomes zero.
#    Zero is divisible by any non-zero number, but the exercise wants
#    "digit_sum divides digit_product", not the reverse.
#    Also, dividing by zero is invalid.
#
# 3. Divisibility test:
#       digit_product % digit_sum == 0
#
# 4. Range:
#    Only 3-digit numbers → 100 to 999 inclusive.
#
# 5. Pattern recognition:
#    Numbers with zeros often fail because product becomes zero.
#    Numbers with large digit sums rarely divide the product cleanly.

# -------------------- EXAMPLES --------------------
# Example: 514
# a=5, b=1, c=4
# sum = 10
# product = 20
# 20 % 10 == 0 → valid
#
# Example: 123
# sum = 6
# product = 6
# 6 % 6 == 0 → valid
#
# Example: 111
# sum = 3
# product = 1
# 1 % 3 != 0 → invalid


# -------------------- COMMON PITFALLS --------------------
# - Forgetting to avoid division by zero.
# - Incorrect digit extraction (especially the tens digit).
# - Using range(99, 1000) instead of range(100, 1000).
# - Misinterpreting the condition as "product divides sum" instead of the reverse.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     Write everything inline inside the loop, no helper function, no digit variables.
#
# Intermediate (My implementation):
#     Break into steps, name digits, compute sum/product, check divisibility.
#
# Advanced:
#     Use list comprehensions, filtering, or even itertools.product for digit generation:
#
#     L = [
#         100*a + 10*b + c
#         for a in range(1, 10)
#         for b in range(0, 10)
#         for c in range(0, 10)
#         if (a+b+c) != 0 and (a*b*c) % (a+b+c) == 0
#     ]

# -------------------- PATTERNS TO RECOGNIZE --------------------
# - Breaking numbers into digits using integer arithmetic.
# - Checking divisibility using modulo.
# - Filtering a range based on a mathematical property.
# - Avoiding invalid operations (division by zero).
# - Building a list of results and returning it.

# -------------------- MINI-QUIZ --------------------
# Q1: Why must we avoid digit_sum == 0?
# Q2: What is the tens digit extraction formula?
# Q3: Why does 123 satisfy the property?
# Q4: What happens if one digit is zero?
#
# ---------------------------------------------------------------



















