from collections import defaultdict

import aoc_helper

DAY = 6
YEAR = 2016


def parse_input(input_text):
    L = input_text.split('\n')
    return L


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    words = parse_input(input_text)
    solution = ""
    for char in range(len(words[0])):
        freq = defaultdict(int)
        for word in words:
            freq[word[char]] += 1
        solution += max(freq, key=freq.get)
    return solution


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    words = parse_input(input_text)
    solution = ""
    for char in range(len(words[0])):
        freq = defaultdict(int)
        for word in words:
            freq[word[char]] += 1
        solution += min(freq, key=freq.get)
    return solution


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
