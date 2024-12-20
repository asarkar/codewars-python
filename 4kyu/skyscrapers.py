# 4 By 4 Skyscrapers
# puzzles #algorithms
#
# In a grid of 4 by 4 squares you want to place a skyscraper in each square with only some clues:
#
# - The height of the skyscrapers is between 1 and 4
# - No two skyscrapers in a row or column may have the same number of floors
# - A clue is the number of skyscrapers that you can see in a row or column from the outside
# - Higher skyscrapers block the view of lower skyscrapers located behind them
#
# Can you write a program that can solve this puzzle?
#
# Example:
#
# To understand how the puzzle works, this is an example of a row with 2 clues.
# Seen from the left side there are 4 buildings visible while seen from the right side only 1:

#   +--+--+--+--+
# 4 |  |  |  |  | 1
#   +--+--+--+--+
#
# There is only one way in which the skyscrapers can be placed. From left-to-right all four
# buildings must be visible and no building may hide behind another building:
#
#   +---+---+---+---+
# 4 | 1 | 2 | 3 | 4 | 1
#   +---+---+---+---+
#
# Example of a 4 by 4 puzzle with the solution:
#
#           1  2
#   +--+--+--+--+
#   |  |  |  |  |
#   +--+--+--+--+
#   |  |  |  |  | 2
#   +--+--+--+--+
# 1 |  |  |  |  |
#   +--+--+--+--+
#   |  |  |  |  |
#   +--+--+--+--+
#          3
#
#             1   2
#   +---+---+---+---+
#   | 2 | 1 | 4 | 3 |
#   +---+---+---+---+
#   | 3 | 4 | 1 | 2 | 2
#   +---+---+---+---+
# 1 | 4 | 2 | 3 | 1 |
#   +---+---+---+---+
#   | 1 | 3 | 2 | 4 |
#   +---+---+---+---+
#             3
#
# Pass the clues in an array of 16 items. This array contains the clues around the clock, index:
#      0   1   2   3
#    +---+---+---+---+
# 15 | 2 | 1 | 4 | 3 | 4
#    +---+---+---+---+
# 14 | 3 | 4 | 1 | 2 | 5
#    +---+---+---+---+
# 13 | 4 | 2 | 3 | 1 | 6
#    +---+---+---+---+
# 12 | 1 | 3 | 2 | 4 | 7
#    +---+---+---+---+
#     11  10   9   8
#
# - If no clue is available, add value `0`
# - Each puzzle has only one possible solution
# - `SolvePuzzle()` returns matrix `int[][]`. The first indexer is for the row, the second indexer for the column.
#   (Python: returns 4-tuple of 4-tuples, Ruby: 4-Array of 4-Arrays)
import copy
import itertools
import sys
from collections import defaultdict

n = 4
Digit = int
Digits = tuple[Digit, ...]
CluePair = tuple[Digit, Digit]
Clues = tuple[CluePair, ...]
Square = tuple[Digit, Digit]
Squares = list[Square]
Grid = dict[Square, set[Digit]]
Soln = tuple[Digits, ...]


def count_visible(nums: Digits) -> Digit:
    """
    :param nums: Heights of skyscrapers from left to right
    :return: The number of skyscrapers visible from the left
    """
    running_max = -sys.maxsize
    count = 0
    for i in nums:
        count += int(i > running_max)
        running_max = max(running_max, i)
    return count


def row(r: Digit) -> Squares:
    """Generates row[r] by varying the columns"""
    return [(r, c) for c in range(n)]


def col(c: Digit) -> Squares:
    """Generates col[c] by varying the rows"""
    return [(r, c) for r in range(n)]


def fill(grid: Grid, s: Square, d: Digit) -> Grid | None:
    """Eliminates all the digits except d from grid[s]"""
    if grid[s] == {d} or all(eliminate(grid, s, d2) for d2 in grid[s] - {d}):
        return grid
    return None


def eliminate(grid: Grid, s: Square, d: Digit) -> Grid | None:
    """Eliminates digit d from grid[s]; implements the two constraint propagation strategies"""
    if d not in grid[s]:  ## Already eliminated
        return grid
    if len(grid[s]) == 1:  ## Only digit left
        print(f"Cannot eliminate the only digit {d} from {s}")
        return None

    grid[s].remove(d)
    units = set(row(s[0]) + col(s[1]))
    peers = units - {s}

    # 1. If a square has only one possible digit, then eliminate
    # that digit as a possibility for each of the square's peers.
    if len(grid[s]) == 1:
        (d2,) = grid[s]
        # Failed to remove d2 from some peer. Backtrack.
        if not all(eliminate(grid, p, d2) for p in peers):
            return None

    dplaces = tuple(u for u in units if d in grid[u])
    # 2. If a unit has only one possible square that can hold a digit,
    # then fill the square with the digit.
    if not dplaces or (len(dplaces) == 1 and not fill(grid, dplaces[0], d)):
        # No place for digit d in the row and col shared by s. Backtrack.
        print(f"No place for {d} in {dplaces}")
        return None

    return grid


def are_clues_satisfied(digits: Digits, clues: CluePair) -> bool:
    """Checks if the given clues are satisfied for the given line"""
    return (clues[0] == 0 or count_visible(digits) == clues[0]) and (
        clues[1] == 0 or count_visible(digits[::-1]) == clues[1]
    )


# Inspired by https://github.com/norvig/pytudes/blob/main/ipynb/Sudoku.ipynb.
def search(grid: Grid, row_clues: Clues, col_clues: Clues) -> Soln | None:
    rows = [tuple(next(iter(grid[c])) for c in row(r) if len(grid[c]) == 1) for r in range(n)]
    # Check all completed rows satisfy the given clues.
    if not all(are_clues_satisfied(r, row_clues[i]) for i, r in enumerate(rows) if len(r) == n):
        return None

    cols = [tuple(next(iter(grid[r])) for r in col(c) if len(grid[r]) == 1) for c in range(n)]
    # Check all completed columns satisfy the given clues.
    if not all(are_clues_satisfied(c, col_clues[i]) for i, c in enumerate(cols) if len(c) == n):
        return None
    # Find the square with the minimum number of possibilities.
    s = min(
        (s for s, xs in grid.items() if len(xs) > 1),
        default=None,
        key=lambda x: len(grid[x]),
    )
    # No squares with multiple possibilities; the search has succeeded.
    if s is None:
        return tuple(tuple(grid[(r, c)].pop() for c in range(n)) for r in range(n))

    for d in grid[s]:
        # Try filling square s with digit d and see if it leads to a solution.
        if (g := fill(copy.deepcopy(grid), s, d)) is not None and (soln := search(g, row_clues, col_clues)) is not None:
            return soln
    return None


# The solution is somewhat more involved than the Sudoku solution referred to in the accepted answer,
# because of two reasons:
#
# 1. The Sudoku board comes prefilled with some digits, and the empty squares can be thought of having
#    the possibilities 1..9 to begin with, but in this problem, we have to generate the board based on the clues.
#
# 2. Once a Sudoku board is filled by appropriately choosing from the possibilities for each square,
#    it is guaranteed to be valid. In this problem, however, completed row and columns have to be further
#    validated with the given clues.
#
# Having generated a board, with a set of possibilities for each square, we run DFS with backtracking.
def solve_puzzle(clues: Digits) -> Soln | None:
    # Create dictionaries keyed by clues to possible arrangement of skyscrapers
    # that satisfy those clues. A clue is the number of skyscrapers visible
    # when viewed from left, right, top or bottom.
    #
    # We will use these dictionaries to constrain the heights of the skyscrapers
    # that may be placed at a grid.
    clue_to_candidates: dict[Digit, set[Digits]] = defaultdict(set)
    rev_clue_to_candidates: dict[Digit, set[Digits]] = defaultdict(set)
    all_candidates = set(itertools.permutations(range(1, n + 1)))
    for c in all_candidates:
        clue_to_candidates[count_visible(c)].add(c)
        x = c[::-1]
        rev_clue_to_candidates[count_visible(x)].add(c)
    clue_to_candidates[0] = all_candidates
    rev_clue_to_candidates[0] = all_candidates

    def candidates(clues: Clues) -> list[list[set[Digit]]]:
        """
        :param clues: Clues at both ends of the row or column
        :return: Heights of the skyscrapers that may be placed at each square
        """
        result: list[list[set[Digit]]] = []
        for clue, rev_clue in clues:
            cs = clue_to_candidates[clue] & rev_clue_to_candidates[rev_clue]
            result.append([set(c) for c in zip(*cs, strict=False)])
        return result

    m = n * n
    # Clues are given in a clockwise manner around the n x n grid, pair them.
    batched_clues = [clues[i : i + n] if i < 2 * n else clues[i + n - 1 : i - 1 : -1] for i in range(0, m - n + 1, n)]
    row_clues = tuple(zip(batched_clues[3], batched_clues[1], strict=False))
    col_clues = tuple(zip(batched_clues[0], batched_clues[2], strict=False))

    # Find the candidates (heights of the skyscrapers that may be placed at each square)
    # row by row.
    row_candidates = {(r, c): cs for r, cols in enumerate(candidates(row_clues)) for c, cs in enumerate(cols)}

    # Create the grid by intersecting the column-wise candidates with the row-wise candidates.
    grid = {
        (r, c): cs & row_candidates[(r, c)] for c, rows in enumerate(candidates(col_clues)) for r, cs in enumerate(rows)
    }

    return search(grid, row_clues, col_clues)
