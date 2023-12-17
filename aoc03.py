from helpers import load_text, get_answer
import numpy as np

EXAMPLE_1_FILE = "data/aoc03/example1.txt"
PROBLEM_1_FILE = "data/aoc03/problem1.txt"


def expand_mat(arr: np.ndarray):
    # Expand array
    arr_exp = np.full((arr.shape[0]+2, arr.shape[1]+2),
                      dtype='<U1', fill_value='.')
    arr_exp[1:(1+arr.shape[0]), 1:(arr.shape[1]+1)] = arr
    return arr_exp


def find_nums_on_line(arr_line: np.ndarray, line_num: int) -> list[tuple[int, int, str]]:
    nums = []

    for i in range(1, len(arr_line)-1):
        mask = [str(c).isdigit() for c in arr_line[i-1:i+2]]

        if mask[0:2] == [False, True]:
            idx_start = i

        if mask[1:3] == [True, False]:
            idx_end = i
            nums.append((line_num, idx_start, ''.join(
                arr_line[idx_start:(idx_end+1)])))

    return nums


def find_numbers(arr: np.ndarray):
    nums: list[tuple[int, int, str]] = []
    for i in range(1, arr.shape[0]):
        nums += find_nums_on_line(arr[i, :], i)
    return nums


def is_symbol(c: str):
    if c == '.':
        return False
    elif c.isdigit():
        return False
    else:
        return True


def calc_symbols_mask(arr: np.ndarray):
    mask_symbol = np.zeros(arr.shape, dtype=np.bool_)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            mask_symbol[i, j] = is_symbol(arr[i, j])
    return mask_symbol


def is_near_symbol(num: tuple[int, int, str], arr: np.ndarray, sym_mask: np.ndarray):
    assert arr.shape == sym_mask.shape

    res: bool = False

    i = num[0]
    for j in range(num[1], num[1]+len(num[2])):
        mask_sub = sym_mask[(i-1):(i+2), (j-1):(j+2)]
        res |= np.any(mask_sub)

    return res


def calc_part_nums_sum(lines: list[str]):
    arr = expand_mat(np.array([[c for c in l] for l in lines], '<U1'))
    sym_mask = calc_symbols_mask(arr)

    part_nums = [int(num[2])
                 for num in find_numbers(arr) if is_near_symbol(num, arr, sym_mask)]
    return np.sum(part_nums)


def main():
    lines = list(map(str.strip, load_text(EXAMPLE_1_FILE)))
    assert calc_part_nums_sum(lines) == int(get_answer(3, 1))

    lines = list(map(str.strip, load_text(PROBLEM_1_FILE)))
    assert calc_part_nums_sum(lines) == int(get_answer(3, 2))


if __name__ == '__main__':
    main()
