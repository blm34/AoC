import re

import aoc_helper

DAY = 4
YEAR = 2017


def valid_phrase(phrase):
    return not re.search(r"\b([a-z]+)\b.+\b\1\b", phrase)


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    lines = input_text.split('\n')
    return sum(valid_phrase(line) for line in lines)


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    lines = input_text.split('\n')
    phrases = [line.split() for line in lines]

    for i in range(len(phrases)):
        for j in range(len(phrases[i])):
            phrases[i][j] = ''.join(sorted(phrases[i][j]))
        phrases[i] = ' '.join(phrases[i])
    return sum(valid_phrase(phrase) for phrase in phrases)


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
