import pytest
import four


@pytest.mark.parametrize(
    "snail_map, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3], [8, 9, 4], [7, 6, 5]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([[]], []),
    ],
)
def test_snail(snail_map: list[list[int]], expected: list[int]) -> None:
    assert four.snail(snail_map) == expected


@pytest.mark.parametrize(
    "seconds, expected",
    [
        (0, "now"),
        (1, "1 second"),
        (62, "1 minute and 2 seconds"),
        (120, "2 minutes"),
        (3600, "1 hour"),
        (3662, "1 hour, 1 minute and 2 seconds"),
        (15731080, "182 days, 1 hour, 44 minutes and 40 seconds"),
        (132030240, "4 years, 68 days, 3 hours and 4 minutes"),
        (205851834, "6 years, 192 days, 13 hours, 3 minutes and 54 seconds"),
        (253374061, "8 years, 12 days, 13 hours, 41 minutes and 1 second"),
        (242062374, "7 years, 246 days, 15 hours, 32 minutes and 54 seconds"),
        (101956166, "3 years, 85 days, 1 hour, 9 minutes and 26 seconds"),
        (33243586, "1 year, 19 days, 18 hours, 19 minutes and 46 seconds"),
    ],
)
def test_format_duration(seconds: int, expected: str) -> None:
    assert four.format_duration(seconds) == expected
