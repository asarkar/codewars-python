import pytest
from _pytest.fixtures import FixtureRequest
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


@pytest.mark.parametrize(
    "triplets, expected",
    [
        (
            [
                ["t", "u", "p"],
                ["w", "h", "i"],
                ["t", "s", "u"],
                ["a", "t", "s"],
                ["h", "a", "p"],
                ["t", "i", "s"],
                ["w", "h", "s"],
            ],
            "whatisup",
        ),
        (
            [
                ["t", "u", "p"],
                ["w", "h", "i"],
                ["t", "s", "u"],
                ["a", "t", "s"],
                ["h", "a", "p"],
                ["t", "i", "s"],
            ],
            "whatisup",
        ),
    ],
)
def test_recover_secret(triplets: list[list[str]], expected: str) -> None:
    assert four.recover_secret(triplets) == expected


@pytest.mark.parametrize(
    "pyramid, expected",
    [
        ([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]], 23),
        (
            [
                [75],
                [95, 64],
                [17, 47, 82],
                [18, 35, 87, 10],
                [20, 4, 82, 47, 65],
                [19, 1, 23, 75, 3, 34],
                [88, 2, 77, 73, 7, 63, 67],
                [99, 65, 4, 28, 6, 16, 70, 92],
                [41, 41, 26, 56, 83, 40, 80, 70, 33],
                [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
                [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
                [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
                [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
                [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
            ],
            1074,
        ),
    ],
)
def test_longest_slide_down(pyramid: list[list[int]], expected: int) -> None:
    assert four.longest_slide_down(pyramid) == expected


def test_longest_slide_down_2(request: FixtureRequest) -> None:
    with open(request.path.parent / "data" / "pyramid.txt") as f:
        pyramid = [[int(s) for s in line.split()] for line in f.readlines()]

    assert four.longest_slide_down(pyramid) == 7273


@pytest.mark.parametrize(
    "num, expected",
    [
        ("one", 1),
        ("twenty", 20),
        ("two hundred forty-six", 246),
        ("seven hundred eighty-three thousand nine hundred and nineteen", 783919),
        ("seven hundred thousand", 700000),
    ],
)
def test_parse_int(num: str, expected: int) -> None:
    assert four.parse_int(num) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (907, 790),
        (531, 513),
        (135, -1),
        (2071, 2017),
        (414, 144),
        (123456798, 123456789),
        (123456789, -1),
        (1234567908, 1234567890),
        (9, -1),
        (135, -1),
        (1027, -1),
        (1207, 1072),
        (29009, 20990),
        (158262180741011122456788, 158262180740887654221111),
        (12875531304666, 12875531066643),
        (400104, 400041),
        (703037, 700733),
    ],
)
def test_next_smaller(n: int, expected: int) -> None:
    assert four.next_smaller(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, [3, 4]),
        (8, None),
    ],
)
def test_decompose(n: int, expected: list[int]) -> None:
    assert four.decompose(n) == expected


@pytest.mark.parametrize(
    "maze, expected",
    [
        ([".W.", ".W.", "..."], 4),
        ([".W.", ".W.", "W.."], False),
        (["......", "......", "......", "......", "......", "......"], 10),
        (["......", "......", "......", "......", ".....W", "....W."], False),
        (
            [
                ".......WW.",
                ".W.W..W..W",
                "W........W",
                ".....W.W..",
                "....W...W.",
                ".....W....",
                ".W..W..W..",
                "..W.....WW",
                ".......WW.",
                "WW........",
            ],
            18,
        ),
        (
            [
                "...........",
                "......WW..W",
                ".......WW..",
                ".WW...W....",
                ".........W.",
                "...W..W.W..",
                ".....W....W",
                "W..........",
                "....WWW....",
                "...WW...W.W",
                ".....W.W...",
            ],
            20,
        ),
        (
            [
                "..W.....W.W",
                "...W.W.....",
                "W...W.W....",
                "W..........",
                "..W......WW",
                "........WWW",
                ".WW....W.W.",
                "..W..WW..WW",
                ".WW.W......",
                "....W..W...",
                ".WW....W...",
            ],
            24,
        ),
    ],
)
def test_path_finder(maze: list[str], expected: int) -> None:
    assert four.path_finder("\n".join(maze)) == expected
    assert four.path_finder2("\n".join(maze)) == expected


@pytest.mark.parametrize(
    "money, coins, expected",
    [
        (0, [], 1),
        (4, [1, 2], 3),
        (10, [5, 2, 3], 4),
        (11, [5, 7], 0),
        (0, [1, 2], 1),
        (4040, [419, 194, 385, 12], 42),
        (2739, [144, 50, 220, 312, 2, 185], 12767),
    ],
)
def test_count_change(money: int, coins: list[int], expected: int) -> None:
    assert four.count_change(money, coins) == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        ("a1", "c1", 2),
        ("a1", "f1", 3),
        ("a1", "f3", 3),
        ("a1", "f4", 4),
        ("a1", "f7", 5),
        ("d4", "f4", 2),
        ("f3", "g7", 3),
        ("g4", "c6", 2),
        ("g3", "a7", 4),
        ("e7", "b1", 3),
    ],
)
def test_knight(start: str, end: str, expected: int) -> None:
    assert four.knight(start, end) == expected


# fmt: off
@pytest.mark.parametrize(
    "lst, expected",
    [
        ([9], 9),
        ([6, 9, 21], 9),
        ([1, 21, 55], 3),
        ([4, 8, 8], 12),
        ([3, 1, 2, 3, 1], 5),
        ([60, 12, 24, 48, 60, 24, 72, 36, 72, 72, 48], 132),
        (
            [
                2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1,
                1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1,
                1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1
             ],
            78
        ),
        ([30, 12], 12),
        ([3, 13, 23, 7, 83], 5),
        (
            [
                109561, 66564, 84681, 136161, 210681, 133956, 59536, 82944, 35344,
                102400, 119025, 224676, 154449, 4624, 40401, 124609, 32400
            ],
            17
        ),
        ([4, 16, 24], 12),
    ],
)
def test_smallest_sum(lst: list[int], expected: int) -> None:
    assert four.smallest_sum(lst) == expected
# fmt: on


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, {""}),
        (1, {"()"}),
        (2, {"(())", "()()"}),
        (3, {"((()))", "(()())", "(())()", "()(())", "()()()"}),
    ],
)
def test_balanced_parens(n: int, expected: set[str]) -> None:
    assert set(four.balanced_parens(n)) == expected


def test_find_word() -> None:
    board = [
        ["E", "A", "R", "A"],
        ["N", "L", "E", "C"],
        ["I", "A", "I", "S"],
        ["B", "Y", "O", "R"],
    ]
    assert four.find_word(board, "C")
    assert four.find_word(board, "EAR")
    assert not four.find_word(board, "EARS")
    assert four.find_word(board, "BAILER")
    assert four.find_word(board, "RSCAREIOYBAILNEA")
    assert not four.find_word(board, "CEREAL")
    assert not four.find_word(board, "ROBES")


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abc", "bac"),
        ("abcd", "bdca"),
        ("abcdx", "cbxda"),
        ("abcdxg", "cxgdba"),
        ("abcdxgz", "dczxgba"),
        ("rexoqvzwmdlfghjbtuiyanskpc", "mzyxwvutsrqponlkjihgfedcba"),
        ("rexoqvzwmdlfghjbtuiyanskpc", "mzyxwvutsrqponlkjihgfedcba"),
        ("oibhtyvfskpjwzqxgmdceanrl", "mlzyxwvtsrqponkjihgfedcba"),
    ],
)
def test_middle_permutation(s: str, expected: str) -> None:
    assert four.middle_permutation(s) == expected


@pytest.mark.parametrize(
    "this, that, expected",
    [
        ([1, 1, 1], [2, 2, 2], True),
        ([1, [1, 1]], [2, [2, 2]], True),
        ([1, [1, 1]], [[2, 2], 2], False),
        ([1, [1, 1]], [[2], 2], False),
        ([[[], []]], [[[], []]], True),
        ([[[], []]], [[1, 1]], False),
        ([1, "[", "]"], ["[", "]", 1], True),
    ],
)
def test_same_structure_as(
    this: four.RecursiveList, that: four.RecursiveList, expected: bool
) -> None:
    assert four.same_structure_as(this, that) == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (5, 7, 7),
        (12, 29, 51),
        (4, 7, 8),
    ],
)
def test_count_ones(left: int, right: int, expected: int) -> None:
    assert four.count_ones(left, right) == expected
