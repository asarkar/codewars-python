import itertools
import operator
from collections.abc import Callable
from dataclasses import dataclass, field


# Vigenère Cipher Helper
# #algorithms #ciphers #security #object-oriented-programming #strings
#
# From Wikipedia:
#
# > The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar
# > ciphers based on the letters of a keyword. It is a simple form of polyalphabetic substitution.
#
# . . .
#
# > In a Caesar cipher, each letter of the alphabet is shifted along some number of places; for example,
# > in a Caesar cipher of shift 3, A would become D, B would become E, Y would become B and so on.
# > The Vigenère cipher consists of several Caesar ciphers in sequence with different shift values.
#
# Assume the key is repeated for the length of the text, character by character. Note that some
# implementations repeat the key over characters only if they are part of the alphabet -- this is not the case here.
#
# The shift is derived by applying a Caesar shift to a character with the corresponding
# index of the key in the alphabet.
#
# Write a class that, when given a key and an alphabet, can be used to encode and decode from the cipher.
#
# Example
# var alphabet = 'abcdefghijklmnopqrstuvwxyz';
# var key = 'password';
#
# // creates a cipher helper with each letter substituted
# // by the corresponding character in the key
# var c = new VigenèreCipher(key, alphabet);
#
# c.encode('codewars'); // returns 'rovwsoiv'
# c.decode('laxxhsj');  // returns 'waffles'
# Any character not in the alphabet must be left as is. For example (following from above):
# c.encode('CODEWARS'); // returns 'CODEWARS'
#
# ANSWER: https://www.youtube.com/watch?v=RCkGauRMs2A
@dataclass
class VigenereCipher:
    key: str
    alphabet: str
    n: int = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        self.n = len(self.alphabet)

    def encode(self, text: str) -> str:
        return self._xcode(text, operator.add)

    def decode(self, text: str) -> str:
        return self._xcode(text, operator.sub)

    def _xcode(self, text: str, op: Callable[[int, int], int]) -> str:
        s: list[str] = []
        for a, b in zip(text, itertools.cycle(self.key)):
            if a not in self.alphabet:
                s.append(a)
            else:
                i = self.alphabet.index(a)
                j = self.alphabet.index(b)
                c = self.alphabet[op(i, j) % self.n]
                s.append(c)
        return "".join(s)
