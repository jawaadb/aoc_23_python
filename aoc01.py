# Part 1
EXAMPLE_FILE = "data/aoc01_example.txt"
PROBLEM_FILE_1 = "data/aoc01_problem1.txt"

# Part 2
EXAMPLE_FILE_2 = "data/aoc01_example2.txt"
PROBLEM_FILE_2 = PROBLEM_FILE_1


def load_text(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        return f.readlines()


def decode_num_only(line: str):
    num_chars = [char for char in line if char.isdigit()]
    assert len(num_chars) != 0
    return num_chars[0] + num_chars[-1]


def findall(sub_str: str, string: str) -> list[int]:
    offset = 0
    found_list: list[int] = []

    while True:
        loc: int = string[offset:].find(sub_str)

        if loc != -1:
            found_list.append(offset+loc)
            offset += loc+1
        else:
            break

    return found_list


def decode_full(line: str):
    str_digits = [str(d) for d in range(10)]
    txt_digits = ['one', 'two', 'three', 'four',
                  'five', 'six', 'seven', 'eight', 'nine']

    found_str_digits: list[tuple[int, str]] = []
    for d in str_digits:
        found_str_digits += [(i, d) for i in findall(d, line)]

    found_txt_digits: list[tuple[int, str]] = []
    for td in txt_digits:
        found_txt_digits += [(i, str(txt_digits.index(td)+1))
                             for i in findall(td, line)]

    found_digits = found_str_digits + found_txt_digits
    found_digits.sort(key=lambda x: x[0])

    return found_digits[0][-1] + found_digits[-1][-1]


def compute_answer(lines: str, read_text_digits=False):
    result: int = 0

    for line in lines:
        if read_text_digits:
            str_value = decode_full(line)
        else:
            str_value = decode_num_only(line)

        result += int(str_value)

    return result


def main():
    example_line = "hdk28lqhhttjz6one2"
    assert findall('2', example_line) == [3, 17]

    eg_simple_decode = decode_num_only(example_line)
    eg_full_decode = decode_full(example_line)

    assert eg_full_decode == eg_simple_decode, f"Expected {eg_simple_decode}, got {eg_full_decode}"

    ans1 = compute_answer(load_text(EXAMPLE_FILE))
    ans2 = compute_answer(load_text(PROBLEM_FILE_1))
    ans3 = compute_answer(load_text(EXAMPLE_FILE_2), read_text_digits=True)
    ans4 = compute_answer(load_text(PROBLEM_FILE_1), read_text_digits=True)

    assert ans1 == 142, f"Example 1 failed giving: {ans1}"
    assert ans2 == 55488, f"Problem 1 failed giving: {ans2}"
    assert ans3 == 281, f"Example 2 failed giving: {ans3}"

    print(ans4)


if __name__ == '__main__':
    main()
