import pytest
import five


@pytest.mark.parametrize(
    "lst",
    [
        ([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
        ([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        ([0, 0]),
        ([0]),
        ([]),
    ],
)
def test_move_zeros(lst: list[int]) -> None:
    # If the value is zero, the key evaluates to true=1,
    # and if the value is non-zero it evaluates to false=0.
    # Keys evaluating to 0 are smaller than 1, and get
    # put at the left. Clever!
    expected = sorted(lst, key=lambda x: int(x == 0))
    assert five.move_zeros(lst) == expected


@pytest.mark.parametrize(
    "seconds, time",
    [
        (0, "00:00:00"),
        (59, "00:00:59"),
        (60, "00:01:00"),
        (3599, "00:59:59"),
        (3600, "01:00:00"),
        (86399, "23:59:59"),
        (86400, "24:00:00"),
        (359999, "99:59:59"),
    ],
)
def test_make_readable(seconds: int, time: str) -> None:
    assert five.make_readable(seconds) == time


@pytest.mark.parametrize(
    "r, g, b, expected",
    [
        (0, 0, 0, "000000"),
        (1, 2, 3, "010203"),
        (255, 255, 255, "FFFFFF"),
        (254, 253, 252, "FEFDFC"),
        (-20, 275, 125, "00FF7D"),
    ],
)
def test_rgb(r: int, g: int, b: int, expected: str) -> None:
    assert five.rgb(r, g, b) == expected


@pytest.mark.parametrize(
    "bits, expected",
    [
        ("1110111", "--"),
        ("11111100111111", "--"),
        ("01110", "."),
        (
            "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011",
            ".... . -.--   .--- ..- -.. .",
        ),
    ],
)
def test_decode_bits(bits: str, expected: str) -> None:
    assert five.decode_bits(bits) == expected
