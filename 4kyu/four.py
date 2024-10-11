import functools
import itertools
from collections import deque

import numpy as np


# Snail
# #array #algorithms
#
# Given an n x n array, return the array elements arranged from
# outermost elements to the middle element, traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
#
# NOTE: The idea is not sort the elements from the lowest value to the highest;
# the idea is to traverse the 2-d array in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
def snail(snail_map: list[list[int]]) -> list[int]:
    m = np.array(snail_map, int)
    result: list[int] = []

    while len(m) > 0:  # Python truthy doesn't work for 2D array
        result.extend(m[0])
        # Rotates counter-clockwise
        m = np.rot90(m[1:])

    return result


# Human readable duration format
# #strings #date-time #algorithms
#
# Your task in order to complete this Kata is to write a function which formats a duration,
# given as a number of seconds, in a human-friendly way.
#
# The function must accept a non-negative integer. If it is zero, it just returns "now".
# Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
#
# It is much easier to understand with an example:
#
# * For seconds = 62, your function should return
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.
#
# Note that spaces are important.
#
# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc.
# In general, a positive integer and one of the valid units of time, separated by a space.
# The unit of time is used in plural if the integer is greater than 1.
#
# The components are separated by a comma and a space (", "). Except the last component,
# which is separated by " and ", just like it would be written in English.
#
# A more significant units of time will occur before than a least significant one.
# Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.
#
# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.
#
# A component will not appear at all if its value happens to be zero.
# Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
#
# A unit of time must be used "as much as possible". It means that the function should not return 61 seconds,
# but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater
# than any valid more significant unit of time.
def format_duration(seconds: int) -> str:
    def fmt(i: int, text: str) -> str:
        return "" if i == 0 else f"{i} {text}{'' if i == 1 else 's'}"

    if seconds == 0:
        return "now"

    units = (
        (31536000, "year"),
        (86400, "day"),
        (3600, "hour"),
        (60, "minute"),
        (1, "second"),
    )

    parts: list[str] = []
    for i, t in units:
        x, seconds = divmod(seconds, i)
        if y := fmt(x, t):
            parts.append(y)

    lft = ", ".join(parts[:-1])
    rt = parts[-1]
    return f"{lft}{' and ' if lft and rt else ''}{rt}"


# Range Extraction
# #algorithms
#
# A format for expressing an ordered list of integers is to use a comma separated list of either
#
# - individual integers
# - or a range of integers denoted by the starting integer separated from the end integer
#   in the range by a dash, '-'. The range includes all integers in the interval including
#   both endpoints. It is not considered a range unless it spans at least 3 numbers.
#   For example "12,13,15-17"
#
# Complete the solution so that it takes a list of integers in increasing order and returns
# a correctly formatted string in the range format.
#
# Example:
#
# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
def solution(nums: list[int]) -> str:
    rng: list[str] = []
    count = 0
    n = len(nums)
    for i in range(n + 1):
        if i == 0 or (i < n and nums[i] == nums[i - 1] + 1):
            count += 1
        else:
            start = nums[i - 1] - count + 1
            if count >= 3:
                rng.append(f"{start}-{nums[i - 1]}")
            else:
                rng.extend([str(j) for j in range(start, nums[i - 1] + 1)])
            count = 1
    return ",".join(rng)


# Next bigger number with the same digits
# strings #refactoring
#
# LeetCode 31: Next Permutation
# LeetCode 556: Next Greater Element III
#
# Create a function that takes a positive integer and returns the next bigger number
# that can be formed by rearranging its digits. For example:
#
#   12 ==> 21
#  513 ==> 531
# 2017 ==> 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):
#
#   9 ==> -1
# 111 ==> -1
# 531 ==> -1
#
# ANSWER: Since a descending sequence is already at its largest value, we can't get the next larger sequence from it.
# We therefore find the first ascending pair a[i] > a[i-1] from the end, and swap a[i-1] with the smallest possible
# value on the right that is larger than it. Since a[i-1] has been increased in value, the sequence a[i:] must be
# set to its smallest value to give the smallest next larger sequence, which is given by the ascending order.
# Furthermore, since we swapped a[i-1] with the smallest possible value on the right, say a[j], all elements in
# sequence a[j+1:] are smaller than a[i-1], and all elements in the sequence a[i:j] are larger than a[i-1].
# Thus, the sequence a[i:] is in descending order, and can be made ascending by using two pointers to swap
# elements from both ends.
#
# Time Complexity: O(n).
def next_bigger(n: int) -> int:
    digits: deque[int] = deque()
    while n > 0:
        n, digit = divmod(n, 10)
        digits.appendleft(digit)

    lo = next(
        (x for x in range(len(digits) - 1, 0, -1) if digits[x] > digits[x - 1]), 0
    )

    if lo > 0:
        i = next(
            x for x in range(len(digits) - 1, lo - 1, -1) if digits[x] > digits[lo - 1]
        )
        digits[lo - 1], digits[i] = digits[i], digits[lo - 1]
    else:
        return -1

    hi = len(digits) - 1
    while lo < hi:
        digits[lo], digits[hi] = digits[hi], digits[lo]
        lo += 1
        hi -= 1

    return functools.reduce(lambda acc, x: acc * 10 + x, digits, 0)


# The observed PIN
# #algorithms
#
# Alright, detective, one of our colleagues successfully observed our target person, Robby the robber.
# We followed him to a secret warehouse, where we assume to find all the stolen stuff.
# The door to this warehouse is secured by an electronic combination lock.
# Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.
#
# The keypad has the following layout:
#
# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
# He noted the PIN 1357, but he also said, it is possible that each of the digits he saw
# could actually be another adjacent digit (horizontally or vertically, but not diagonally).
# E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.
#
# He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs,
# they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.
#
# * possible in sense of: the observed PIN itself and all variations considering the adjacent digits
#
# Can you help us to find all those variations? It would be nice to have a function, that returns an array
# (or a list in Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits.
# We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs,
# the observed one and also the results, must be strings, because of potentially leading '0's.
# We already prepared some test cases for you.
#
# Detective, we are counting on you!
#
# Time Complexity: If the average number of options is 3, then 3^n, where n is the length
# of the observed PIN.
def get_pins(observed: str) -> list[str]:
    adj = ("08", "124", "2135", "326", "4157", "52468", "6359", "748", "85790", "968")

    return ["".join(p) for p in itertools.product(*(adj[int(d)] for d in observed))]


# Sum of Intervals
# #algorithms #performance
#
# Write a function called sumIntervals/sum_intervals that accepts an array of intervals,
# and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
#
# Intervals
# Intervals are represented by a pair of integers in the form of an array.
# The first value of the interval will always be less than the second value.
# Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
#
# Overlapping Intervals
# List containing overlapping intervals:
#
# [
#    [1, 4],
#    [7, 10],
#    [3, 5]
# ]
# The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap,
# we can treat the interval as [1, 5], which has a length of 4.
#
# Time Complexity: O(n), where n is the number of intervals.
def sum_of_intervals(intervals: list[tuple[int, int]]) -> int:
    intervals.sort(reverse=True)
    total = 0

    while intervals:
        start, end = intervals.pop()
        if intervals and intervals[-1][0] <= end:
            y = intervals.pop()[1]
            intervals.append((start, max(end, y)))
        else:
            total += end - start

    return total
