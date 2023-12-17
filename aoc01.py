from helpers import get_answer, load_text, str_findall

# Part 1
EXAMPLE_FILE_1 = "data/aoc01/example1.txt"
PROBLEM_FILE_1 = "data/aoc01/problem1.txt"

# Part 2
EXAMPLE_FILE_2 = "data/aoc01/example2.txt"
PROBLEM_FILE_2 = PROBLEM_FILE_1


def decode_line(line: str, text_as_digit: bool):
    str_digits = [str(d) for d in range(10)]
    txt_digits = ['one', 'two', 'three', 'four',
                  'five', 'six', 'seven', 'eight', 'nine']

    if not text_as_digit:
        txt_digits: list[str] = []

    found_digits: list[tuple[int, str]] = []
    for d in str_digits:
        found_digits += [(i, d) for i in str_findall(d, line)]

    for td in txt_digits:
        found_digits += [(i, str(txt_digits.index(td)+1))
                         for i in str_findall(td, line)]

    found_digits.sort(key=lambda x: x[0])

    assert len(found_digits) != 0
    return int(found_digits[0][-1] + found_digits[-1][-1])


def compute_answer(lines: str, text_as_digit=False):
    result: int = 0

    for line in lines:
        result += decode_line(line, text_as_digit)

    return result


def main():
    # Calculate answers
    calculated_answers: list[int] = []
    calculated_answers.append(compute_answer(load_text(EXAMPLE_FILE_1)))
    calculated_answers.append(compute_answer(load_text(PROBLEM_FILE_1)))
    calculated_answers.append(compute_answer(
        load_text(EXAMPLE_FILE_2), text_as_digit=True))
    calculated_answers.append(compute_answer(
        load_text(PROBLEM_FILE_1), text_as_digit=True))

    # Check answers
    answers = [int(get_answer(1, part)) for part in range(1, 5)]
    for i, (ans, calc_ans) in enumerate(zip(answers, calculated_answers)):
        assert calc_ans == ans
        print(f"Answer {i+1}: {calc_ans}")


if __name__ == '__main__':
    main()
