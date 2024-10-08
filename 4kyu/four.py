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
