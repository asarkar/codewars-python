from collections.abc import Callable
from typing import Any

import pytest
import six
from _pytest.fixtures import FixtureRequest


@pytest.fixture
def data_loader(request: FixtureRequest) -> Callable[[str], list[Any]]:
    def loader(filename: str) -> list[Any]:
        with open(request.path.parent / "data" / filename) as f:
            return list(map(eval, f.readlines()))

    return loader


@pytest.mark.parametrize(
    "code, expected",
    [
        (".-", "A"),
        ("--...", "7"),
        ("...-..-", "$"),
        (".", "E"),
        ("..", "I"),
        (". .", "EE"),
        (".   .", "E E"),
        ("...-..- ...-..- ...-..-", "$$$"),
        ("----- .---- ..--- ---.. ----.", "01289"),
        (".-... ---...   -..-. --...", "&: /7"),
        ("...---...", "SOS"),
        ("... --- ...", "SOS"),
        ("...   ---   ...", "S O S"),
        (" . ", "E"),
        ("   .   . ", "E E"),
        (
            "      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   "
            + ".--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  ",
            "SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.",
        ),
    ],
)
def test_decode_morse(data_loader: Callable[[str], list[Any]], code: str, expected: str) -> None:
    table, *x = data_loader("morse.txt")
    assert six.decode_morse(code, table) == expected
