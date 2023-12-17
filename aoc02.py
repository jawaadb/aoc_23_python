from helpers import load_text
import numpy as np


EXAMPLE_1_FILE = "data/aoc02/example1.txt"
PROBLEM_1_FILE = "data/aoc02/problem1.txt"


MAX_CUBES: list[tuple[int, str]] = [(12, 'red'), (13, 'green'), (14, 'blue')]
CUBE_COLOURS = [c[1] for c in MAX_CUBES]
CUBE_COUNTS = [c[0] for c in MAX_CUBES]


def split_game(l: str):
    id, g = map(str.strip, l.split(':'))
    id = id.split(' ')[-1].strip()
    assert id.isnumeric(), "Non-numeric game id"
    id = int(id)
    return (int(id), list(map(str.strip, g.split(';'))))


def split_result(r: str):
    def f(x): return (int(x[0].strip()), str(x[1]).strip())
    return [f(tuple(c.split(' '))) for c in map(str.strip, r.split(','))]


def is_valid_result(r: str) -> bool:
    counts = np.zeros(len(MAX_CUBES))

    reveals = split_result(r)

    for reveal in reveals:
        idx = CUBE_COLOURS.index(reveal[1])
        counts[idx] += reveal[0]

    return np.all(counts <= CUBE_COUNTS)


def is_valid_set(g: list[str]):
    return all([is_valid_result(r) for r in g])


def sum_of_valid_game_ids(lines: list[str]):
    id_sum = 0
    for l in lines:
        id, gset = split_game(l)

        valid_set = is_valid_set(gset)

        if valid_set:
            id_sum += id

    return id_sum



def calc_power(gset: list[str]) -> int:
    max_count = np.zeros(len(CUBE_COLOURS), dtype=np.int64)

    for r in gset:
        for c in split_result(r):
            idx = CUBE_COLOURS.index(c[1])
            count = c[0]
            max_count[idx] = max(max_count[idx], count)

    return np.prod(max_count)


def calc_power_sum(lines: list[str]) -> int:
    sum = 0
    for l in lines:
        sum += calc_power(split_game(l)[1])

    return sum


def main():
    lines = list(map(str.strip, load_text(EXAMPLE_1_FILE)))
    assert sum_of_valid_game_ids(lines) == 8

    lines = list(map(str.strip, load_text(PROBLEM_1_FILE)))
    assert sum_of_valid_game_ids(lines) == 2416

    lines = list(map(str.strip, load_text(EXAMPLE_1_FILE)))
    assert calc_power_sum(lines)==2286

    lines = list(map(str.strip, load_text(PROBLEM_1_FILE)))
    print(f"result={calc_power_sum(lines)}")


if __name__ == '__main__':
    main()
