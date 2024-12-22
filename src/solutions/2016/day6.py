from collections import defaultdict

import aoc_helper

DAY = 6
YEAR = 2016


def parse_input(input_text):
    L = input_text.split('\n')
    return L


def p1(input_text):
    words = parse_input(input_text)
    solution = ""
    for char in range(len(words[0])):
        freq = defaultdict(int)
        for word in words:
            freq[word[char]] += 1
        solution += max(freq, key=freq.get)
    return solution


def p2(input_text):
    words = parse_input(input_text)
    solution = ""
    for char in range(len(words[0])):
        freq = defaultdict(int)
        for word in words:
            freq[word[char]] += 1
        solution += min(freq, key=freq.get)
    return solution


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
