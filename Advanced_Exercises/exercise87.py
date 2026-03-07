# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 87 - File processing

"""
Write a function processFile(filePath) that takes a text file as a parameter and
creates another text file (using a path of your choice) that will contain the same
content as the file passed as a parameter but without line breaks.

>> processFile("test.txt")
*****A file without line breaks*****
"""

def processFile(filePath):
    # Read the entire file
    with open(filePath, "r") as file:
        content = file.read()

    # Remove line breaks
    new_content = content.replace("\n", "")

    # Choose output file path
    output_path = "processed_no_breaks.txt"

    # Write the modified content
    with open(output_path, "w") as outfile:
        outfile.write(new_content)

    print("*****A file without line breaks*****")
    return output_path


# -------------------- TEACHING NOTES --------------------
# Topic: Removing Line Breaks from a File
#
# 1. file.read():
#       Loads the entire file into a single string.
#
# 2. Removing line breaks:
#       content.replace("\n", "")
#       This strips ALL newline characters.
#
# 3. Writing the new file:
#       We create a new file instead of overwriting the original.
#
# 4. Why this works:
#       Text files store line breaks as '\n'.
#       Removing them merges all lines into one continuous string.

# -------------------- EXAMPLES --------------------
#
# If test.txt contains:
#   Hello
#   World
#
# processFile("test.txt") creates:
#   processed_no_breaks.txt containing "HelloWorld"

# -------------------- COMMON PITFALLS --------------------
#
# 1. Forgetting to open the output file in write mode.
# 2. Using .strip() — which removes whitespace, not just newlines.
# 3. Overwriting the original file unintentionally.
#
# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------
#
# Beginner:
#     Read line by line and concatenate manually.
#
# Intermediate (My implementation):
#     Use read() + replace() for a clean one‑liner transformation.
#
# Advanced:
#     Use pathlib and more flexible whitespace normalization.
#
# ---------------------------------------------------------------
