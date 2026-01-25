# 100 Exercises for Practicing PYTHON

# Author: Laurentine K.Masson

# A set of exercises with different levels of complexity

# Beginner-level exercises

# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 28

# ===========================================================
"""
Write a program that calculates the execution time of a script. Let's take
the script from exercise 24 as an example and calculate its execution time.
The program should display the multiplication table from exercise 24
and the execution time at the end.
"""

# Write your code here:

import time

start = time.perf_counter()
#start = time.time()

# Exercise 24 script

for num in range(0, 11):
    x = num * 8
    print(f"8 x {num} = {x} ")
    
#end = time.time()
end = time.perf_counter()

execution_time = end - start

print(execution_time)

# ============================
# Teaching Notes (Exercise 28)
# ============================

# 1. Measuring execution time means capturing two timestamps:
#       - one before the code runs
#       - one after the code runs
#    The difference between them is the execution duration.

# 2. Beginner method: time.time()
#    -----------------------------
#    time.time() returns the current time in seconds.
#    It has limited precision (milliseconds), so very fast scripts
#    may appear to take 0.0 seconds.
#
#    Example:
#       start = time.time()
#       ... code ...
#       end = time.time()
#       execution_time = end - start

# 3. Professional method: time.perf_counter()
#    ----------------------------------------
#    time.perf_counter() provides a high-resolution timer designed
#    specifically for measuring execution time. It can detect very
#    small durations that time.time() rounds down to zero.
#
#    Example:
#       start = time.perf_counter()
#       ... code ...
#       end = time.perf_counter()
#       execution_time = end - start

# 4. Why the original result was 0.0
#    The multiplication table loop runs extremely fast.
#    The difference between start and end was smaller than the
#    precision of time.time(), so it rounded down to 0.0 seconds.

# 5. Forcing a visible execution time (optional)
#    Adding a small delay inside the loop makes the timing easier to see:
#
#       time.sleep(0.1)
#
#    This slows the loop down so the execution time becomes measurable.

# Summary:
#    - Use time.time() for simple beginner exercises.
#    - Use time.perf_counter() for accurate timing and benchmarking.
#    - Fast code may show 0.0 seconds unless a high-resolution timer is used.

# ============================================
# Examples: Timing Methods Compared
# ============================================

# Example 1: Using time.time() (lower precision)
start_time = time.time()
for i in range(1000000):
    pass
end_time = time.time()
print("Execution time using time.time():", end_time - start_time)

# Example 2: Using time.perf_counter() (high precision)
start_perf = time.perf_counter()
for i in range(1000000):
    pass
end_perf = time.perf_counter()
print("Execution time using time.perf_counter():", end_perf - start_perf)

# Example 3: Forcing a visible delay
start_delay = time.perf_counter()
time.sleep(0.5)  # half-second delay
end_delay = time.perf_counter()
print("Execution time with sleep():", end_delay - start_delay)

