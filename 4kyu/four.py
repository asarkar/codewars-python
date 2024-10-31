import functools
import heapq
import itertools
import math
from collections import deque, defaultdict
from typing import Any

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


# Recover a secret string from random triplets
# #algorithms
#
# There is a secret string which is unknown to you. Given a collection of random triplets from the string,
# recover the original string.
#
# A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before
# the next in the given string. "whi" is a triplet for the string "whatisup".
#
# As a simplification, you may assume that no letter occurs more than once in the secret string.
#
# You can assume nothing about the triplets given to you other than that they are valid triplets and that
# they contain sufficient information to deduce the original string. In particular, this means that the
# secret string will never contain letters that do not occur in one of the triplets given to you.
#
# ANSWER: We create a graph from the triplets, then run DFS with backtracking.
def recover_secret(triplets: list[list[str]]) -> str:
    graph: dict[str, set[str]] = defaultdict(set)
    indegrees: dict[str, int] = defaultdict(int)

    for x, y, z in triplets:
        graph[x].add(y)
        graph[y].add(z)
        indegrees[x] += 0
        indegrees[y] += 1
        indegrees[z] += 1

    def dfs(ch: str, word: list[str], visited: set[str]) -> str:
        if ch not in graph:
            return "".join(word) if len(word) == len(indegrees) else ""
        for x in graph[ch]:
            word.append(x)
            visited.add(x)
            if w := dfs(x, word, visited):
                return w
            word.pop()
            visited.remove(x)
        return ""

    start = next(k for k, v in indegrees.items() if v == 0)
    # https://stackoverflow.com/a/22440130/839733
    return dfs(start, [start], {start})


# Pyramid Slide Down
# #algorithms #dynamic-programming
#
# Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer,
# you can mess with pyramids even if you are not in Egypt at the time. For example,
# let's consider the following problem. Imagine that you have a pyramid built of numbers, like this one here:
#
#    /3/
#   \7\ 4
#  2 \4\ 6
# 8 5 \9\ 3
# Here comes the task...
# Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid.
# As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23
#
# Your task is to write a function that takes a pyramid representation as an argument and returns its
# largest 'slide down'. For example:
#
# * With the input `[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]`
# * Your function should return `23`.
# By the way...
# My tests include some extraordinarily high pyramids so as you can guess, brute-force method is a bad idea
# unless you have a few centuries to waste. You must come up with something more clever than that.
#
# ANSWER: Bottom-up DP. Max value at a cell is the sum of itself with the max value at one of the two children.
#
# Time Complexity: We visit every element; total number of elements is given by 1 + 2 + 3 + ... + n = O(n^2).
def longest_slide_down(pyramid: list[list[int]]) -> int:
    for row in range(len(pyramid) - 2, -1, -1):
        for col in range(len(pyramid[row])):
            pyramid[row][col] += max(pyramid[row + 1][col], pyramid[row + 1][col + 1])

    return pyramid[0][0]


# parseInt() reloaded
# #parsing #strings #algorithms
#
# In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.
#
# Examples:
#
# "one" => 1
# "twenty" => 20
# "two hundred forty-six" => 246
# "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
# Additional Notes:
#
# The minimum number is "zero" (inclusively)
# The maximum number, which must be supported is 1 million (inclusively)
# The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
# All tested numbers are valid, you don't need to validate them
def parse_int(string: str) -> int:
    # fmt: off
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    # fmt: on

    words = string.replace("-", " ").split()

    numbers: list[int] = []
    for w in words:
        if w in units:
            numbers.append(units.index(w))
        elif w in tens:
            numbers.append((tens.index(w) + 2) * 10)
        elif w == "hundred":
            numbers[-1] *= 100
        elif w == "thousand":
            numbers = [x * 1000 for x in numbers]
        elif w == "million":
            numbers = [x * 1000000 for x in numbers]
    return sum(numbers)


# Next smaller number with the same digits
# #strings #mathematics #algorithms
#
# Write a function that takes a positive integer and returns the
# next smaller positive integer containing the same digits.
#
# For example:
#
# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017
# Return -1 (for Haskell: return Nothing, for Rust: return None),
# when there is no smaller number that contains the same digits.
# Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.
#
# next_smaller(9) == -1
# next_smaller(135) == -1
# next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
# some tests will include very large numbers.
# test data only employs positive integers.
#
# ANSWER: Similar to next_bigger.
def next_smaller(n: int) -> int:
    digits: deque[int] = deque()
    while n > 0:
        n, digit = divmod(n, 10)
        digits.appendleft(digit)

    lo = next(
        (x for x in range(len(digits) - 1, 0, -1) if digits[x] < digits[x - 1]), 0
    )

    if lo > 0:
        i = next(
            x for x in range(len(digits) - 1, lo - 1, -1) if digits[x] < digits[lo - 1]
        )
        digits[lo - 1], digits[i] = digits[i], digits[lo - 1]
    else:
        return -1

    hi = len(digits) - 1
    while lo < hi:
        digits[lo], digits[hi] = digits[hi], digits[lo]
        lo += 1
        hi -= 1

    if digits[0] == 0:
        return -1

    return functools.reduce(lambda acc, x: acc * 10 + x, digits, 0)


# Square into Squares. Protect trees!
# mathematics #algorithms
#
# Given a positive integral number n, return a strictly increasing sequence
# (list/array/string depending on the language) of numbers, so that the sum of the squares is equal to n^2.
#
# If there are multiple solutions (and there will be), return as far as possible the result with the largest
# possible values:
#
# Examples
# decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11^2,
#   11^2 = 121 = 1 + 4 + 16 + 100 = 1^2 + 2^2 + 4^2 + 10^2 but don't return [2,6,9], since 9 is smaller than 10.
#
# For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a
# strictly increasing sequence.
#
# Note
# Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists, return nil, null, Nothing,
# None (depending on the language) or "[]" (C) ,{} (C++), [] (Swift, Go).
#
# The function "decompose" will take a positive integer n and return the decomposition of N = n^ as:
#
# [x1 ... xk] or
# "x1 ... xk" or
# Just [x1 ... xk] or
# Some [x1 ... xk] or
# {x1 ... xk} or
# "[x1,x2, ... ,xk]"
# depending on the language (see "Sample tests")
#
# Hint
# Very often xk will be n-1.
def decompose(n: int, remaining: int = -1) -> list[int] | None:
    if remaining < 0:
        remaining = n * n
    if remaining == 0:
        return []
    for i in range(min(n - 1, int(math.sqrt(remaining))), 0, -1):
        sub = decompose(i, remaining - i * i)
        if sub is not None:
            return sub + [i]
    return None


# Path Finder #2: shortest path
# #algorithms
#
# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions
# (i.e. North, East, South, West). Return the minimal number of steps to exit position [N-1, N-1]
# if it is possible to reach the exit from the starting position. Otherwise, return false.
#
# Empty positions are marked .. Walls are marked W. Start and exit positions are guaranteed to be empty
# in all test cases.
#
# ANSWER: BFS.
def path_finder(maze: str) -> int:
    grid = maze.splitlines()
    n = len(grid)
    dist: dict[tuple[int, int], int] = {(0, 0): 0}
    to_visit = deque([(0, 0)])
    moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
    end = (n - 1, n - 1)

    while to_visit:
        rc = to_visit.popleft()
        d = dist[rc]
        if rc == end:
            break
        for (dx, dy), (r, c) in itertools.product(moves, (rc,)):
            row, col = r + dx, c + dy
            if (
                0 <= row < n
                and 0 <= col < n
                and grid[row][col] == "."
                and ((row, col) not in dist or dist[(row, col)] > d + 1)
            ):
                dist[(row, col)] = d + 1
                to_visit.append((row, col))

    return dist[end] if end in dist else 0


# Alternative implementation using A* search and a heuristic of Manhattan distance + current distance.
def path_finder2(maze: str) -> int:
    grid = [list(row) for row in maze.splitlines()]
    n = len(grid)
    to_visit: list[tuple[int, int, tuple[int, int]]] = [
        (0, 0, (0, 0))
    ]  # (heuristic, dist, (r, c))
    moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
    end = (n - 1, n - 1)
    x = sum(end)

    while to_visit:
        _, d, rc = heapq.heappop(to_visit)
        if rc == end:
            return d
        d += 1
        for (dx, dy), (r, c) in itertools.product(moves, (rc,)):
            row, col = r + dx, c + dy
            if 0 <= row < n and 0 <= col < n and grid[row][col] == ".":
                grid[row][col] = "X"
                heapq.heappush(to_visit, (d + x - row - col, d, (row, col)))

    return 0


# Counting Change Combinations
# #puzzles #recursion
#
# LeetCode 518: Coin Change II
#
# Write a function that counts how many different ways you can make change for an amount of money,
# given an array of coin denominations. For example, there are 3 ways to give change for 4
# if you have coins with denomination 1 and 2:
#
# 1+1+1+1, 1+1+2, 2+2.
# The order of coins does not matter:
#
# 1+1+2 == 2+1+1
# Also, assume that you have an infinite amount of coins.
#
# ANSWER: Top-down recursive implementation runs into stackoverflow for some inputs.
def count_change(money: int, coins: list[int]) -> int:
    # @functools.cache
    # def loop(remaining: int, i: int) -> int:
    #     if remaining < 0:
    #         return 0
    #     if remaining == 0:
    #         return 1
    #     candidates = itertools.takewhile(
    #         lambda x: coins[x] <= remaining, range(i, len(coins))
    #     )
    #     return sum(loop(remaining - coins[c], c) for c in candidates)
    #
    if money == 0:
        return 1
    # coins.sort()
    # return loop(money, 0)

    # dp[i][j] is the number of ways amount i can be made using the coins up to and including index j
    dp: list[list[int]] = [[0] * len(coins) for _ in range(money + 1)]
    for i in range(len(coins)):
        # There's only one way to change for amount zero, with no coins
        dp[0][i] = 1

    for i in range(1, money + 1):
        for j in range(len(coins)):
            # Include coin[j]
            if coins[j] <= i:
                dp[i][j] += dp[i - coins[j]][j]
            # Exclude coin[j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]

    return dp[-1][-1]


# Shortest Knight Path
# #algorithms
#
# Given two different positions on a chess board, find the least number of moves it would take a knight
# to get from one to the other. The positions will be passed as two arguments in algebraic notation.
# For example, knight("a3", "b5") should return 1.
#
# The knight is not allowed to move off the board. The board is 8x8.
#
# ANSWER: While we can solve this by BFS, we will use A* algorithm. Note that A* is just Dijkstra's algorithm
# with the distance function modified. In this case, we will use the Manhattan distance of a cell from the target
# _divided by three_ as the heuristic. We divide by three because x and y change by a total of 3 in each move.
def knight(p1: str, p2: str) -> int:
    def coord(square: str) -> tuple[int, int]:
        return ord(square[0]) - ord("a"), int(square[1]) - 1

    start, end = coord(p1), coord(p2)
    n = 8
    to_visit = [(0, start)]
    steps = {start: 0}

    while to_visit:
        _, square = heapq.heappop(to_visit)
        curr_step = steps[square]
        if square == end:
            return curr_step
        for d in (-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2):
            nxt_row = square[0] + d[0]
            nxt_col = square[1] + d[1]
            next_step = curr_step + 1
            if (
                0 <= nxt_row < n
                and 0 <= nxt_col < n
                and (
                    (nxt_row, nxt_col) not in steps
                    or next_step < steps[(nxt_row, nxt_col)]
                )
            ):
                steps[(nxt_row, nxt_col)] = next_step
                heuristic = (abs(end[0] - nxt_row) + abs(end[1] - nxt_col)) // 3
                dist = next_step + heuristic
                heapq.heappush(to_visit, (dist, (nxt_row, nxt_col)))

    return -1


# Smallest possible sum
# #algorithms #mathematics #arrays
#
# Given an array X of positive integers, its elements are to be transformed
# by running the following operation on them as many times as required:
#
# if X[i] > X[j] then X[i] = X[i] - X[j]
#
# When no more transformations are possible, return its sum ("smallest possible sum").
def smallest_sum(lst: list[int]) -> int:
    return math.gcd(*lst) * len(lst)


# All Balanced Parentheses
# #algorithms
#
# Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses.
#
# Examples
# balanced_parens(0) => [""]
# balanced_parens(1) => ["()"]
# balanced_parens(2) => ["()()","(())"]
# balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
def balanced_parens(n: int) -> list[str]:
    def loop(left: int, right: int, way: list[str]) -> None:
        if left == right == 0:
            ways.append("".join(way))
            return
        if left > 0:
            way.append("(")
            loop(left - 1, right, way)
            way.pop()
        if right > left:
            way.append(")")
            loop(left, right - 1, way)
            way.pop()

    ways: list[str] = []
    loop(n, n, [])
    return ways


# Boggle Word Checker
# #arrays #recursion #puzzles
#
# Write a function that determines whether a string is a valid guess in a Boggle board,
# as per the rules of Boggle. A Boggle board is a 2D array of individual characters, e.g.:
# [ ["I","L","A","W"],
#   ["B","N","G","E"],
#   ["I","U","A","O"],
#   ["A","S","R","L"] ]
# Valid guesses are strings which can be formed by connecting adjacent cells
# (horizontally, vertically, or diagonally) without re-using any previously used cells.
#
# For example, in the above board "BINGO", "LINGO", and "ILNBIA" would all be valid guesses,
# while "BUNGIE", "BINS", and "SINUS" would not.
#
# Your function should take two arguments (a 2D array and a string) and return true or false
# depending on whether the string is found in the array as per Boggle rules.
def find_word(board: list[list[str]], word: str) -> bool:
    def search(curr: tuple[int, int], i: int) -> bool:
        if i == len(word) - 1:
            return True
        shift = (-1, 0, 1)
        grid[curr[0]][curr[1]] = ""
        for dx, dy in itertools.product(shift, repeat=2):
            row = curr[0] + dx
            col = curr[1] + dy
            if (
                0 <= row < len(grid)
                and 0 <= col < len(grid[row])
                and grid[row][col] == word[i + 1]
                and search((row, col), i + 1)
            ):
                return True

        grid[curr[0]][curr[1]] = word[i]
        return False

    # Make a copy of the board since the same board is used for multiple tests.
    grid = [[*r] for r in board]
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == word[0] and search((r, c), 0):
                return True
    return False


# Simple Fun #159: Middle Permutation
# #puzzles
#
# You are given a string s. Every letter in s appears once.
#
# Consider all strings formed by rearranging the letters in s. After ordering these strings in dictionary order,
# return the middle term. (If the sequence has a even length n, define its middle term to be the (n/2)th term.)
#
# Example
# For s = "abc", the result should be "bac".
#
#  The permutations in order are: "abc", "acb", "bac", "bca", "cab", "cba" So, The middle term is "bac".
def middle_permutation(s: str) -> str:
    def loop(t: list[str], start: int, num_comb: int) -> str:
        """
        :param t: Sorted input sequence
        :param start: If all possible permutations of the input were in sorted order,
            the index of the permutation to start this iteration from. Starts from 1
        :param num_comb: Number of permutations with each letter at the beginning of a word.
            Example: t=['a','b','c'] - There are 2 combinations each beginning with 'a', 'b', and 'c'

        :returns: The target sequence
        """
        n = len(t)
        if n == 1:
            return t.pop()
        if start == target:
            return "".join(t)
        # Number of combinations to skip that can't contain the target combination.
        # Example: t=['a','b','c'], start=1, target=3, we can skip the first 2 combinations beginning with 'a'.
        # Mathematically, we are looking for the greatest k such that start + k * num_comb <= target.
        k = (target - start) // num_comb
        return t.pop(k) + loop(t, start + num_comb * k, num_comb // (n - 1))

    n = len(s)
    x = math.factorial(n)
    target = x // 2
    return loop(sorted(s), 1, x // n)


# https://peps.python.org/pep-0695/#generic-type-alias
# Python 3.12 onwards
type RecursiveList = Any | list[RecursiveList]


# Nesting Structure Comparison
# #arrays #algorithms
#
# Complete the function/method (depending on the language) to return true/True when its argument is an array
# that has the same nesting structures and same corresponding length of nested arrays as the first array.
def same_structure_as(this: RecursiveList, that: RecursiveList) -> bool:
    if isinstance(this, list) and isinstance(that, list):
        return len(this) == len(that) and all(
            same_structure_as(x, y) for x, y in zip(this, that)
        )
    return not isinstance(this, list) and not isinstance(that, list)


# Count ones in a segment
# #binary #performance #algorithms
#
# Given two numbers: 'left' and 'right' (1 <= 'left' <= 'right' <= 200000000000000), return sum of
# all '1' occurrences in binary representations of numbers between 'left' and 'right' (including both)
#
# Example:
# countOnes 4 7 should return 8, because:
# 4(dec) = 100(bin), which adds 1 to the result.
# 5(dec) = 101(bin), which adds 2 to the result.
# 6(dec) = 110(bin), which adds 2 to the result.
# 7(dec) = 111(bin), which adds 3 to the result.
# So finally result equals 8.
# WARNING: Segment may contain billions of elements, to pass this kata, your solution cannot iterate
# through all the numbers in the segment!
#
# ANSWER: Let's try to find a pattern:
# The numbers below 2^1 are:
#   0
#   1
# To get the numbers below 2^2, we clone the above numbers, and put 0s before the first half of numbers
# and 1s before the second half of numbers.
#   00
#   01
#   10
#   11
# Let f(n) be the number of 1s _until_ 2^n where n >= 1. Since we clone the numbers from the previous step,
# and then prepend 1s to half of them, f(n) = f(n-1) + 2^(n-1). The 2nd factor comes from the fact that
# there are 2^n numbers from 0 _until_ 2^n, and we append 1 to half of them.
# f(n) = 2 * f(n-1) + 2^(n-1)
# 	   = 2 * 2 * f(n-2) + 2 * 2^(n-2) + 2^(n-1)  # Expanding f(n-1)
# 	   = 2 * 2 * 2 * f(n-3) + 2 * 2 * 2^(n-3) + 2 * 2^(n-2) + 2^(n-1)  # Expanding f(n-2)
# 	   = 2^(n-1) + (n-1) * 2^(n-1)  # When i=n-1, f(1)=1
# 	   = n * 2^(n-1)
#
# Now let's use the above formula to find the number of 1s from 0 to 12, both included.
#         -a-
# 1  →  |0001|
# 2  →  |0010|
# 3  →  |0011|
# 4  →  |0100|
# 5  →  |0101|
# 6  →  |0110|
# 7  →  |0111|
#       -c- -b-
# 8  →  |1|000|
# 9  →  |1|001|
# 10 →  |1|010|
# 11 →  |1|011|
# 12 →  |1|100|
#
# The greatest power of 2 that is not greater than 12 is 3, because 2^3 (=8) <= 12.
# We can find the number of 1s from 0 till 7 using the above formula. -- Call this 'a' --
# Notice that number 8 onwards, the last 3 bits form a series that we have seen before,
# which is 000 (=0), 001 (=1), ..., 100 (=4). Thus, we can calculate the number of 1s
# from 0 till 4 using a recursive call. -- Call this 'b' --
# The first bit from 8 till 12 is 1; -- call this 'c' --
# The answer is a+b+c.
#
# Time Complexity: Since each time n is reduced by the closest power of 2, the algorithm
# converges extremely quickly, and runs in almost O(1) time.
def count_ones(left: int, right: int) -> int:
    def count1s(n: int) -> int:
        if n <= 1:
            return n
        x = int(math.log2(n))
        y = int(2 ** (x - 1))
        a = x * y
        b = count1s(n - 2 * y)
        c = n - 2 * y + 1
        return a + b + c

    return count1s(right) - count1s(left - 1)
