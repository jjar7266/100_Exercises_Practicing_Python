# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Intermediate-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 69 - Number of days and hours

"""
Write a function daysHoursCount(startDate, endDate) which takes two input
parameters: the start date startDate and the end date endDate. This function
will allow us to calculate the number of days and the number of hours
between the start and end dates provided as parameters. The function should
return the tuple (DayCount, HourCount)

Verification tests:
>> daysHoursCount("2022/05/15", "2022/06/20")
(36, 864)

>> daysHoursCount("2022/04/01", "2022/04/27")
(26, 624)
"""

from datetime import datetime

def daysHoursCount(startDate, endDate):
    # Convert strings into datetime objects
    fmt = "%Y/%m/%d"
    start = datetime.strptime(startDate, fmt)
    end = datetime.strptime(endDate, fmt)

    # Compute the difference
    delta = end - start

    # Extract days and convert to hours
    day_count = delta.days
    hour_count = day_count * 24

    return (day_count, hour_count)

# --------------------- TEACHING NOTES ------------------------
# Topic: Working with Date Differences
#
# 1. Parsing dates:
#    datetime.strptime() converts a string into a datetime object.
#    Format used: "%Y/%m/%d"
#
# 2. Subtracting dates:
#    end - start returns a timedate object.
#
# 3. Extracting days:
#    delta.days gives the number of full days between dates.
#
# 4. Converting days to hours:
#    hour_count = day_count * 24
#
# 5. Why this works:
#    Since no time-of-day is provided, the difference is clean and predictable.

# ----------------------- EXAMPLES -------------------------
#
# Example 1:
# >>> daysHoursCount("2022/05/15", "2022/06/20")
# (36, 864)
#
# Example 2:
# >>> daysHoursCount("2022/04/01", "2022/04/27")
# (26, 624)

# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Wrong date format:
#    "2022-05-15" will fail unless the format string is changed.
#
# 2. End date before start date:
#    Produces a negative number of days.
#
# 3. Forgetting to multiply by 24:
#    delta.days gives days only, not hours.
#
# 4. Assuming partial days:
#    The exercise expects whole-day differences only.

# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED -------------
#
# Beginner:
#     def daysHoursCount(startDate, endDate):
#         fmt = "%Y/%m/%d"
#         start = datetime.strptime(startDate, fmt)
#         end = datetime.strptime(endDate, fmt)
#         delta = end - start
#         days = delta.days
#         hours = days * 24
#         return (days, hours)
#
# Intermediate (My implementation):
#     def daysHoursCount(startDate, endDate):
#         fmt = "%Y/%m/%d"
#         start = datetime.strptime(startDate, fmt)
#         end = datetime.strptime(endDate, fmt)
#         delta = end - start
#         return (delta.days, delta.days * 24)
#
# Advanced (Validation + Flexible Formats):
#     def daysHoursCount(startDate, endDate):
#         formats = ["%Y/%m/%d", "%Y-%m-%d"]
#         for f in formats:
#             try:
#                 start = datetime.strptime(startDate, f)
#                 end = datetime.strptime(endDate, f)
#                 break
#             except ValueError:
#                 continue
#         else:
#             raise ValueError("Invalid date format.")
#
#         delta = end - start
#         return (delta.days, delta.days * 24)

# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Converting strings to datetime objects.
# 2. Using strptime() with format codes.
# 3. Subtracting datetime objects to get a timedelta.
# 4. Extracting .days from timedelta.
# 5. Returning multiple values in a tuple.

# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does strptime() do?
# A1: Converts a date string into a datetime object using a format pattern.
#
# Q2: What type is returned when subtracting two datetime objects?
# A2: A timedelta object.
#
# Q3: How do you convert days into hours?
# A3: Multiply by 24.
#
# ---------------------------------------------------------------
















