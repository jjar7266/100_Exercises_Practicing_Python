# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 22 - Using the format() Method
# ===========================================================
"""
Write a program that truncates a decimal number to 2 digits after the
decimal point.
For example, if we take the decimal number 187.632587, the program
should display 187.63.
"""

# --- Main Solution ----------------------------------------------------------

# We want to truncate a decimal number to 2 digits after the decimal.
# The exercise specifically wants us to use the format() method.
#
# Number formatting uses a pattern inside the format specifier:
#
#   : . 2 f
#     | | |
#     | | └── 'f' = fixed‑point decimal format
#     | └──── '2' = keep exactly 2 digits after the decimal
#     └────── '.' = start of the precision specifier
#
# Optional:
#   ',' adds a thousands separator (not required here, but allowed)
#
# Structure inside format():
#   format(value, ".2f")
#
# Structure inside an f-string (same rules):
#   f"{value:.2f}"
#
# Now write the actual formatting line below using the pattern above.

num = 187.632587

print(f"{num:.2f}")

# ========================================================================

# --- Additional Learning Examples ---

# 1. Formatting with 3 decimal places

# Shows how changing the precision affects the output.

example_three_decimals = format(187.632587, ".3f")
print(example_three_decimals)

# 2. Formatting with NO decimal places

# Useful when you want to drop the fractional part entirely.

example_no_decimals = format(187.632587, ".0f")
print(example_no_decimals)

# 3. Formatting with a thousands separator + 2 decimals

# Demonstrates how ',' can be combined with precision.

example_with_commas = format(12345.6789, ",.2f")
print(example_with_commas)

# 4. Using an f-string with the same formatting rules

# Same pattern, just inside an f-string.

num = 187.632587
example_fstring = f"{num:.2f}"
print(example_fstring)

# ---------------------------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------------------------
# Number formatting lets you control how many digits appear after the decimal.
# The pattern ".2f" means: fixed‑point number with exactly 2 decimal places.
# You can also add a comma for thousands separators: ",.2f".
#
# format() and f-strings use the same rules, so once you learn the pattern,
# you can format any number consistently.
# ---------------------------------------------------------------------------