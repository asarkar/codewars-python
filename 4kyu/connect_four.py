import itertools

import numpy as np
from numpy.typing import NDArray


# Connect Four
# #fundamentals
#
# Take a look at wiki description of Connect Four game:
#
# Wiki Connect Four
#
# The grid is 6 row by 7 columns, those being named from A to G.
#
# You will receive a list of strings showing the order of the pieces which dropped in columns:
#   pieces_position_list = ["A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"]
#
# The list may contain up to 42 moves and shows the order the players are playing.
#
# The first player who connects four items of the same color is the winner.
#
# You should return "Yellow", "Red" or "Draw" accordingly.
#
# ANSWER: The input may contain moves even after the game is won by a player,
# so, we need to check after placing each piece.
def who_is_winner(pieces: list[str]) -> str:
    m, n = 6, 7
    indices = [0] * n
    # https://numpy.org/doc/stable/user/basics.strings.html#fixed-width-data-types
    # One-byte encoding, the byteorder is ‘|’ (not applicable)
    board = np.full((m, n), ".", "|S1")

    # Set each piece on the board and look for a winner.
    for p in pieces:
        col = ord(p[0]) - ord("A")
        board[indices[col], col] = p[2]
        indices[col] += 1

        if (w := find_winner(board)) is not None:
            return w

    return "Draw"


def winner(arr: NDArray[np.bytes_]) -> bytes:
    i = len(arr)
    xs = next(
        (xs for j in range(i - 3) if (xs := set(arr[j : j + 4])) < {b"R", b"Y"}),
        {b""},
    )
    return xs.pop()


def axis(board: NDArray[np.bytes_], x: int) -> bytes | None:
    # https://numpy.org/doc/2.0/reference/generated/numpy.apply_along_axis.html#numpy-apply-along-axis
    # Axis 0 is column-wise, 1 is row-wise.
    return next(
        (w for w in np.apply_along_axis(winner, x, board) if w),
        None,
    )


def diag(board: NDArray[np.bytes_], d: int) -> bytes | None:
    # https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy-diagonal
    # Diagonal number is w.r.t. the main diagonal.
    b = board if bool(d) else np.fliplr(board)
    return next((w for d in range(-3, 4) if (w := winner(b.diagonal(d)))), None)


def find_winner(board: NDArray[np.bytes_]) -> str | None:
    match next(
        (w for f, i in itertools.product((axis, diag), (0, 1)) if (w := f(board, i)) is not None),
        None,
    ):
        case b"Y":
            return "Yellow"
        case b"R":
            return "Red"
        case _:
            return None
