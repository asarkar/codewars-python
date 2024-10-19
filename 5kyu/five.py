# Moving Zeros To The End
# #arrays #sorting #algorithms
#
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
import re


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


def _transmission_rate(bits: str) -> int:
    rate = 0
    for m in re.finditer("1+|0+", bits):
        if 0 < rate < len(m.group(0)):
            break
        else:
            rate = len(m.group(0))
    return rate


# Decode the Morse code, advanced
# #algorithms
#
# In this kata you have to write a Morse code decoder for wired electrical telegraph.
# Electric telegraph is operated on a 2-wire line with a key that, when pressed,
# connects the wires together, which can be detected on a remote station.
# The Morse code encodes every character being transmitted as a sequence of "dots"
# (short presses on the key) and "dashes" (long presses on the key).
#
# When transmitting the Morse code, the international standard specifies that:
#
# "Dot" – is 1 time unit long.
# "Dash" – is 3 time units long.
# Pause between dots and dashes in a character – is 1 time unit long.
# Pause between characters inside a word – is 3 time units long.
# Pause between words – is 7 time units long.
# However, the standard does not specify how long that "time unit" is. And in fact different operators
# would transmit at different speed. An amateur person may need a few seconds to transmit a single character,
# a skilled professional can transmit 60 words per minute, and robotic transmitters may go way faster.
#
# For this kata we assume the message receiving is performed automatically by the hardware that checks
# the line periodically, and if the line is connected (the key at the remote station is down), 1 is recorded,
# and if the line is not connected (remote key is up), 0 is recorded. After the message is fully received,
# it gets to you for decoding as a string containing only symbols 0 and 1.
#
# For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be received as follows:
#
# 1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011
#
# As you may see, this transmission is perfectly accurate according to the standard, and the hardware
# sampled the line exactly two times per "dot".
#
# That said, your task is to implement two functions:
#
# Function decodeBits(bits), that should find out the transmission rate of the message, correctly decode
# the message to dots ., dashes - and spaces (one between characters, three between words) and return
# those as a string. Note that some extra 0's may naturally occur at the beginning and the end of a message,
# make sure to ignore them. Also if you have trouble discerning if the particular sequence of 1's is a dot
# or a dash, assume it's a dot.
# 2. Function decodeMorse(morseCode), that would take the output of the previous function and return a
# human-readable string.
#
# NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.
#
# The Morse code table is preloaded for you (see the solution setup, to get its identifier in your language).
#
# All the test strings would be valid to the point that they could be reliably decoded as described above,
# so you may skip checking for errors and exceptions, just do your best in figuring out what the message is!
def decode_bits(bits: str) -> str:
    cleaned = bits.strip("0")
    rate = _transmission_rate(cleaned)
    mapping = {
        "1" * rate: ".",
        "1" * rate * 3: "-",
        "0" * rate * 3: " ",
        "0" * rate * 7: " " * 3,
    }

    msg = (
        mapping[x]
        for m in re.finditer("1+|0+", cleaned)
        if (x := m.group(0)) in mapping
    )
    return "".join(msg).strip()
