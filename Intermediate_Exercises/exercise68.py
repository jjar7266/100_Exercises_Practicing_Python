# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 68 - Ask the user for a list

"""
Write a program that prompts the user to enter a list of integers from the
console. The program should store this list in a variable user_list and display
it at the end of the program.

Note: The function we have at our disposal to interact with the user is input(),
      which returns a string as output. The goal of the exercise is to use this
      function to obtain a list of elements by the end of the program.
"""

def askUserList():
    user_input = input("Enter a list of integers separated by spaces: ")

    # Split the string into pieces, convert each to int

    user_list = [int(x) for x in user_input.split()]

    print("You entered:", user_list)
    return user_list

# -------------------- TEACHING NOTES --------------------
# Topic: Converting User Input into a List of Integers
#
# 1. input() returns a string:
#    Example: "1 2 3 4"
#
# 2. Splitting the string:
#    user_input.split() → ["1", "2", "3", "4"]
#
# 3. Converting each element:
#    int(x) converts each string to an integer.
#
# 4. List comprehension:
#    [int(x) for x in user_input.split()] builds the final list.
#
# 5. Displaying the result:
#    The program prints the list at the end as required.


# -------------------- EXAMPLES --------------------
#
# Example 1:
# User enters:
#   10 20 30 40
#
# >>> askUserList()
# Enter a list of integers separated by spaces: 10 20 30 40
# You entered: [10, 20, 30, 40]
#
# Example 2:
# User enters:
#   5 5 5 1 2
#
# >>> askUserList()
# Enter a list of integers separated by spaces: 5 5 5 1 2
# You entered: [5, 5, 5, 1, 2]


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to convert to int:
#    Without int(), the list becomes ["1", "2", "3"] instead of [1, 2, 3].
#
# 2. Commas:
#    If the user types "1, 2, 3", split() won't work as expected.
#
# 3. Non-numeric input:
#    Entering letters will cause int() to raise an error.
#
# 4. Extra spaces:
#    split() handles multiple spaces automatically.


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     user_input = input("Enter numbers: ")
#     parts = user_input.split()
#     user_list = []
#     for p in parts:
#         user_list.append(int(p))
#     print(user_list)
#
# Intermediate (My implementation):
#     def askUserList():
#         user_input = input("Enter a list of integers separated by spaces: ")
#         user_list = [int(x) for x in user_input.split()]
#         print("You entered:", user_list)
#         return user_list
#
# Advanced (input validation):
#     def askUserList():
#         while True:
#             try:
#                 user_input = input("Enter integers separated by spaces: ")
#                 return [int(x) for x in user_input.split()]
#             except ValueError:
#                 print("Invalid input. Please enter only integers.")


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Using split() to break user input into pieces.
# 2. Using list comprehension for clean conversion.
# 3. Converting strings to integers with int().
# 4. Returning the final list for later use.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does split() do?
# A1: Breaks the input string into separate pieces based on spaces.
#
# Q2: Why do we use int(x)?
# A2: To convert each string element into an integer.
#
# Q3: What happens if the user types letters?
# A3: int() raises a ValueError.
#
# ---------------------------------------------------------------
