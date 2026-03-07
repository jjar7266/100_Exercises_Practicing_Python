# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 86 - Pythagorean triplet x, y, z

"""
A Pythagorean triplet is a triplet (x, y, z) of integers such that x < y < z and
x ** 2 + y ** 2 = z ** 2. There is a unique Pythagorean triplet such that:
x + y + z = 1000. What is the value of x * y * z?

Note: ** denotes exponentiation, and * denotes multiplication
"""

def find_pythagorean_triplet_product(total_sum=1000):
    """
    Finds the unique Pythagorean triplet (x, y, z) such that:
        - x < y < z
        - x^2 + y^2 = z^2
        - x + y + z = total_sum

    Returns:
        (x, y, z, product)
    """
    for x in range(1, total_sum):
        for y in range(x + 1, total_sum):
            z = total_sum - x - y
            if z <= y:
                continue
            if x * x + y * y == z * z:
                return x, y, z, x * y * z

    return None  # Should not happen for total_sum = 1000


# Compute the specific answer for 1000
triplet = find_pythagorean_triplet_product(1000)
if triplet is not None:
    x, y, z, product = triplet
    # For this exercise, the key answer is x * y * z
    # You can print or just rely on product in an interactive session.
    # print(x, y, z, product)
else:
    x = y = z = product = None

# -------------------- TEACHING NOTES --------------------
# Topic: Pythagorean Triplet with Sum Constraint
#
# 1. Definitions:
#    - Pythagorean triplet: integers (x, y, z) with x < y < z and x^2 + y^2 = z^2.
#    - Additional constraint: x + y + z = 1000.
#
# 2. Strategy:
#    - Loop over possible x and y.
#    - Compute z = total_sum - x - y.
#    - Enforce x < y < z.
#    - Check the Pythagorean condition: x^2 + y^2 == z^2.
#
# 3. Why this works:
#    - The sum constraint reduces the search space.
#    - We don't need a third loop for z; it's derived from x and y.

# -------------------- EXAMPLES / CHECKS --------------------
#
# For total_sum = 1000, the unique triplet is:
#   x = 200, y = 375, z = 425
#   x^2 + y^2 = 200^2 + 375^2 = 40000 + 140625 = 180625 = 425^2
#   x + y + z = 200 + 375 + 425 = 1000
#   x * y * z = 200 * 375 * 425 = 31875000
#
# So the answer to the question "Que vaut x*y*z?" is:
#   31875000

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     - Use three nested loops for x, y, z and check both conditions.
#
# Intermediate (My implementation):
#     - Use two loops (x, y), derive z from the sum constraint.
#
# Advanced:
#     - Use number theory / Euclid's formula for generating Pythagorean triplets
#       and solve algebraically for the sum constraint.
#
# ---------------------------------------------------------------
