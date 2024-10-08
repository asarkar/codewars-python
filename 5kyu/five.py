# Moving Zeros To The End
# #arrays #sorting #algorithms
#
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
def move_zeros(lst: list[int]) -> list[int]:
    n = len(lst)
    zero_pos = -1
    non_zero_pos = 0

    while zero_pos < non_zero_pos < n:
        zero_pos = next((i for i in range(zero_pos + 1, n) if lst[i] == 0), n)
        non_zero_pos = next((i for i in range(zero_pos + 1, n) if lst[i] != 0), n)

        if zero_pos < non_zero_pos < n:
            lst[zero_pos], lst[non_zero_pos] = lst[non_zero_pos], lst[zero_pos]

    return lst


# Human Readable Time
# #date-time #mathematics #algorithms
#
# Write a function, which takes a non-negative integer (seconds) as input
# and returns the time in a human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
def make_readable(seconds: int) -> str:
    h, minutes = divmod(seconds, 3600)
    m, s = divmod(minutes, 60)
    return f"{h:0>2}:{m:0>2}:{s:0>2}"


# RGB To Hex Conversion
# #algorithms
#
# The rgb function is incomplete. Complete it so that passing in RGB decimal values
# will result in a hexadecimal representation being returned.
# Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
# must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"
def rgb(r: int, g: int, b: int) -> str:
    def to_hex(i: int) -> str:
        if i <= 0:
            return "00"
        return f"{hex(min(i, 255))[2:]:0>2}".upper()

    return f"{to_hex(r)}{to_hex(g)}{to_hex(b)}"
