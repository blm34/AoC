import re

import aoc_helper

DAY = 4
YEAR = 2017


def valid_phrase(phrase):
    return not re.search(r"\b([a-z]+)\b.+\b\1\b", phrase)


def p1(input_text):
    lines = input_text.split('\n')
    return sum(valid_phrase(line) for line in lines)


def p2(input_text):
    lines = input_text.split('\n')
    phrases = [line.split() for line in lines]

    for i in range(len(phrases)):
        for j in range(len(phrases[i])):
            phrases[i][j] = ''.join(sorted(phrases[i][j]))
        phrases[i] = ' '.join(phrases[i])
    return sum(valid_phrase(phrase) for phrase in phrases)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
