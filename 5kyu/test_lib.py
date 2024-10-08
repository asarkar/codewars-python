import pytest
import lib


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
    assert lib.move_zeros(lst) == expected
