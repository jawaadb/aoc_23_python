from helpers import load_text


EXAMPLE_1_FILE = "data/aoc02/example1.txt"


def main():
    lines = map(str.strip, load_text(EXAMPLE_1_FILE))

    for l in lines:
        print(l)


if __name__ == '__main__':
    main()
