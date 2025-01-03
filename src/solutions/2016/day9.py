import re

import aoc_helper

DAY = 9
YEAR = 2016


def p1(input_text):
    decompressed_text = ""
    while len(input_text) > 0:
        if input_text[0] != '(':
            decompressed_text += input_text[0]
            input_text = input_text[1:]
        else:
            match = re.search(r"\((\d+)x(\d+)\)", input_text)
            span = match.span()
            length, repeats = map(int, match.groups())

            input_text = input_text[span[1]:]
            sequence = input_text[:length]
            decompressed_text += sequence * repeats
            input_text = input_text[length:]
    return len(decompressed_text)


def decompressed_len(data, total_repeats):
    total_length = 0
    while data:
        if data[0] != '(':
            total_length += 1
            data = data[1:]
            continue

        match = re.search(r"\((\d+)x(\d+)\)", data)
        seq_start = match.span()[1]
        seq_length, seq_repeats = map(int, match.groups())

        sequence = data[seq_start:seq_start + seq_length]
        total_length += decompressed_len(sequence, seq_repeats)
        data = data[seq_start + seq_length:]
    return total_length * total_repeats


def p2(input_text):
    return decompressed_len(input_text, 1)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
