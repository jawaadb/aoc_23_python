EXAMPLE_FILE = "data/aoc01_example.txt"
PROBLEM_FILE_1 = "data/aoc01_problem1.txt"

def load_text(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        return f.readlines()


def compute_answer(fpath: str):
    result: int = 0

    for line in load_text(fpath):
        num_chars = [char for char in line if char.isdigit()]
        assert len(num_chars) != 0

        result += int(num_chars[0] + num_chars[-1])

    return result


def main():
    print(compute_answer(EXAMPLE_FILE))
    print(compute_answer(PROBLEM_FILE_1))


if __name__ == '__main__':
    main()
