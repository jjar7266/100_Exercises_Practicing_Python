# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Intermediate-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 36 -Calculation of the sum of digits

# ===========================================================
"""
Write a program that calculates the sum of the digits of a number. The
program should display the result on the console.

Some examples:
  - For the number 149, the program displays 14.
  - For the number 3018, the program displays 12.
"""

# Write your code here :-)

#===================================================================

# Summing the digits of a number

# Strategy:

#   1. Convert the number to a string so we can loop through digits.
#   2. Convert each character back to an integer.
#   3. Add them together.

# Example: "149" -> ['1', '4', '9'] -> [1, 4, 9] -> sum = 14

num = 149
total = 0

for digit in str(num):
    total += int(digit)

print(total)

# ==================================================================

# Pythonic Version (One-liner)

num = 149
print(sum(int(d) for d in str(num)))

# ---------------------------------------------------------------
# TEACHING NOTES — Breaking down the one‑liner
#
# One‑liner:
#     sum(int(d) for d in str(num))
#
# Breakdown:
#   1. str(num)
#        Convert the number into a string so we can loop through
#        each digit as a character. Example: 149 → "149"
#
#   2. for d in str(num)
#        Loop through each character in the string:
#        "1", "4", "9"
#
#   3. int(d)
#        Convert each character back into an integer:
#        "1" → 1, "4" → 4, "9" → 9
#
#   4. sum( ... )
#        The sum() function adds up all the integers produced
#        by the loop. Example: 1 + 4 + 9 = 14
#
# So the one‑liner is just a compact way of:
#   - looping through digits
#   - converting them to integers
#   - adding them together
# ---------------------------------------------------------------



