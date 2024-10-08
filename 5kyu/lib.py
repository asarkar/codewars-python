# Moving Zeros To The End
# #arrays #sorting #algorithms
#
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
def move_zeros(lst: list[int]) -> list[int]:
    n = len(lst)
    zero_pos = -1
    non_zero_pos = 0

    while zero_pos < non_zero_pos < n:
        zero_pos = next((i for i in range(zero_pos + 1, n) if lst[i] == 0), n)
        non_zero_pos = next((i for i in range(zero_pos + 1, n) if lst[i] != 0), n)

        if zero_pos < non_zero_pos < n:
            lst[zero_pos], lst[non_zero_pos] = lst[non_zero_pos], lst[zero_pos]

    return lst
