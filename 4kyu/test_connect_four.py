import connect_four
import pytest


# fmt: off
@pytest.mark.parametrize(
    "pieces, expected",
    [
        (
            [
                "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow",
                "G_Red", "C_Yellow", "C_Red", "D_Yellow", "F_Red", "E_Yellow", "A_Red",
                "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red", "B_Yellow",
                "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
            ],
            "Yellow"
        ),
        (
            [
                "C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow",
                "G_Red", "E_Yellow", "A_Red", "G_Yellow", "C_Red", "A_Yellow", "A_Red",
                "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red", "D_Yellow",
                "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red",
                "A_Yellow", "F_Red", "C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow",
                "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red", "E_Yellow", "E_Red"
            ],
            "Yellow"
        ),
        (
            [
                "F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow",
                "D_Red", "D_Yellow", "F_Red", "B_Yellow", "E_Red", "C_Yellow", "D_Red",
                "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red", "F_Yellow",
                "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red",
                "E_Yellow", "G_Red", "A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow",
                "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red", "B_Yellow", "B_Red"
            ],
            "Red"
        ),
        (
            [
                "A_Yellow", "B_Red", "B_Yellow", "C_Red", "G_Yellow", "C_Red", "C_Yellow", "D_Red",
                "G_Yellow", "D_Red", "G_Yellow", "D_Red", "F_Yellow", "E_Red", "D_Yellow"
            ],
            "Red"
        ),
        (
            ["A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"],
            "Yellow"
        ),
        (
            ["A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"],
            "Draw"
        ),
        (
            [
                'F_Red', 'B_Yellow', 'F_Red', 'A_Yellow', 'E_Red', 'C_Yellow', 'A_Red',
                'F_Yellow', 'E_Red', 'E_Yellow', 'B_Red', 'B_Yellow', 'D_Red', 'F_Yellow',
                'C_Red', 'E_Yellow', 'G_Red', 'E_Yellow', 'F_Red', 'E_Yellow'
            ],
            "Red"
        )
    ],
)
def test_who_is_winner(pieces: list[str], expected: str) -> None:
    assert connect_four.who_is_winner(pieces) == expected
# fmt: on
