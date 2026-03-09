# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 99 - The maximum sum of a sub-list

"""
Write a function largestSum(L) that takes a list L as a parameter and
determines the largest sum obtained by summing the elements of all
possible subsequences of the list L.
The function should return the subsequence list that yields the largest
sum as well as the maximum sum found.

Reminder: a subsequence is sequence of numbers in the list L.

Verification tests:
>> largestSum([-8, -4, 6, 8, -6, 10, -4, -4])
(18, [6, 8, -6, 10])

>> largestSum([-6, 1, 8, -7, 1, 9, -1, 2])
(13, [1, 8, -7, 1, 9, -1, 2])
"""

def largestSum(L):
    max_sum = float('-inf')
    current_sum = 0

    start = 0
    best_start = 0
    best_end = 0

    for i, value in enumerate(L):
        if current_sum <= 0:
            current_sum = value
            start = i
        else:
            current_sum += value

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start
            best_end = i

    return max_sum, L[best_start:best_end + 1]


# -------------------- TEACHING NOTES --------------------
# Topic: Maximum Subarray (Kadane’s Algorithm)
#
# 1. current_sum tracks the running sum of the current subsequence.
# 2. If current_sum becomes negative, we restart at the next index.
# 3. max_sum stores the best sum found so far.
# 4. best_start and best_end track the indices of the best subsequence.
# 5. Complexity: O(n), extremely efficient.


# -------------------- EXAMPLES --------------------
#
# >>> largestSum([-8, -4, 6, 8, -6, 10, -4, -4])
# (18, [6, 8, -6, 10])
#
# >>> largestSum([-6, 1, 8, -7, 1, 9, -1, 2])
# (13, [1, 8, -7, 1, 9, -1, 2])


# -------------------- COMMON PITFALLS --------------------
#
# 1. Forgetting to track the subsequence indices.
# 2. Restarting the sum incorrectly.
# 3. Returning only the sum instead of (sum, subsequence).
# 4. Using O(n²) brute force instead of O(n) Kadane’s Algorithm.


# -------------------- BEGINNER VERSION --------------------
def largestSum_Beginner(L):
    max_sum = float('-inf')
    best_sub = []

    for i in range(len(L)):
        current_sum = 0
        for j in range(i, len(L)):
            current_sum += L[j]
            if current_sum > max_sum:
                max_sum = current_sum
                best_sub = L[i:j+1]

    return max_sum, best_sub


# -------------------- INTERMEDIATE VERSION (my implementation) --------------------
def largestSum_Intermediate(L):
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    best_start = 0
    best_end = 0

    for i, value in enumerate(L):
        if current_sum <= 0:
            current_sum = value
            start = i
        else:
            current_sum += value

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start
            best_end = i

    return max_sum, L[best_start:best_end + 1]


# -------------------- ADVANCED VERSION (handles all-negative lists cleanly) --------------------
def largestSum_Advanced(L):
    max_sum = L[0]
    current_sum = L[0]
    best_start = best_end = 0
    start = 0

    for i in range(1, len(L)):
        if current_sum + L[i] < L[i]:
            current_sum = L[i]
            start = i
        else:
            current_sum += L[i]

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start
            best_end = i

    return max_sum, L[best_start:best_end + 1]
