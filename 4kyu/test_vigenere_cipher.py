import pytest
from vigenere_cipher import VigenereCipher


@pytest.mark.parametrize(
    "text",
    ["codewars", "waffles", "CODEWARS"],
)
def test_vigenere_cipher(text: str) -> None:
    abc = "abcdefghijklmnopqrstuvwxyz"
    key = "password"
    c = VigenereCipher(key, abc)
    assert c.decode(c.encode(text)) == text
