import pandas as pd


def get_answer(problem: int, part: int):
    assert (1 <= problem) and (problem <= 25)
    df = pd.read_csv("data/answers.txt", sep='\t', dtype=str)
    answers = df.loc[(df['Problem'] == str(problem)) &
                     (df['Part'] == str(part)), 'Answer']
    assert len(answers) == 1
    return answers.iloc[0]


def load_text(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        return f.readlines()


def str_findall(sub_str: str, string: str) -> list[int]:
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
