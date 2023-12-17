EXAMPLE_FILE = "data/aoc01_example.txt"


def load_text(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        return f.readlines()


def main():
    result: int = 0

    for line in load_text(EXAMPLE_FILE):
        num_chars = [char for char in line if char.isdigit()]
        assert len(num_chars) != 0

        result += int(num_chars[0] + num_chars[-1])

    print(result)


if __name__ == '__main__':
    main()
