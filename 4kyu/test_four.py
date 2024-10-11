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


@pytest.mark.parametrize(
    "nums, expected",
    [
        (
            [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
            "-6,-3-1,3-5,7-11,14,15,17-20",
        ),
        ([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20], "-3--1,2,10,15,16,18-20"),
    ],
)
def test_solution(nums: list[int], expected: str) -> None:
    assert four.solution(nums) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (12, 21),
        (21, -1),
        (513, 531),
        (2017, 2071),
        (414, 441),
        (144, 414),
        (2097, 2709),
        (154, 415),
        (1234567890, 1234567908),
        (59884848459853, 59884848483559),
    ],
)
def test_next_bigger(n: int, expected: int) -> None:
    assert four.next_bigger(n) == expected


# fmt: off
@pytest.mark.parametrize(
    "observed, expected",
    [
        ("8", ["5","7","8","9","0"]),
        ("11",["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
        ('369', [
            "339","366","399","658","636","258","268","669","668","266","369","398",
            "256","296","259","368","638","396","238","356","659","639","666","359",
            "336","299","338","696","269","358","656","698","699","298","236","239"
        ]),
    ],
)
def test_get_pins(observed: str, expected: list[str]) -> None:
    assert set(four.get_pins(observed)) == set(expected)
# fmt: on


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([(1, 5)], 4),
        ([(1, 5), (6, 10)], 8),
        ([(1, 5), (1, 5)], 4),
        ([(1, 4), (7, 10), (3, 5)], 7),
        ([(-1_000_000_000, 1_000_000_000)], 2_000_000_000),
        ([(0, 20), (-100_000_000, 10), (30, 40)], 100_000_030),
    ],
)
def test_sum_of_intervals(intervals: list[tuple[int, int]], expected: int) -> None:
    assert four.sum_of_intervals(intervals) == expected
