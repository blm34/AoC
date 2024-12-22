from functools import cache

import aoc_helper

DAY = 21
YEAR = 2024

moves_dict = {(-1, 0): '^',
              (0, 1): '>',
              (1, 0): 'v',
              (0, -1): '<'}

move_positions = {'^': (0, 1),
                  'A': (0, 2),
                  '<': (1, 0),
                  'v': (1, 1),
                  '>': (1, 2)}

num_positions = {'7': (0, 0),
                 '8': (0, 1),
                 '9': (0, 2),
                 '4': (1, 0),
                 '5': (1, 1),
                 '6': (1, 2),
                 '1': (2, 0),
                 '2': (2, 1),
                 '3': (2, 2),
                 '0': (3, 1),
                 'A': (3, 2)}


def complexity(code, depth):
    moves = get_code_moves(code)
    length = sum(get_sequence_length(move+'A', depth)
                 for move in moves.split('A')[:-1])
    numeric = int(code.replace("A", ""))
    return numeric * length


@cache
def get_sequence_length(move, depth):
    if depth == 1:
        return len(move)
    else:
        moves = get_moves_to_press(move)
        return sum(get_sequence_length(move+'A', depth-1)
                   for move in moves.split('A')[:-1])


def get_move_sequence(start, end, positions):
    sr, sc = positions[start]
    er, ec = positions[end]
    dr = er - sr
    dc = ec - sc

    # Preferred order = < ^ v >
    # Only horizontal
    if dr == 0:
        moves = '>' * dc if dc > 0 else '<' * -dc
    # Only vertical
    elif dc == 0:
        moves = 'v' * dr if dr > 0 else '^' * -dr
    # Try going left first
    elif dc < 0:
        if (sr, ec) in positions.values():
            moves = '<' * -dc
            moves += 'v' * dr if dr > 0 else '^' * -dr
        else:
            moves = 'v' * dr if dr > 0 else '^' * -dr
            moves += '<' * -dc
    # Try going up first
    elif dr < 0:
        if (er, sc) in positions.values():
            moves = '^' * -dr
            moves += '>' * dc if dc > 0 else '<' * -dc
        else:
            moves = '>' * dc if dc > 0 else '<' * -dc
            moves += '^' * -dr
    # Try going down first
    elif dr > 0:
        if (er, sc) in positions.values():
            moves = 'v' * dr
            moves += '>' * dc if dc > 0 else '<' * -dc
        else:
            moves = '>' * dc if dc > 0 else '<' * -dc
            moves += 'v' * dr
    # Otherwise go right first
    else:
        moves = '>' * dc
        moves += 'v' * dr if dr > 0 else '^' * -dr
    return moves + 'A'


def get_code_moves(code):
    moves = ""
    for start, end in zip('A' + code[:-1], code):
        moves += get_move_sequence(start, end, num_positions)
    return moves


@cache
def get_moves_to_press(move):
    moves = ""
    for start, end in zip('A' + move[:-1], move):
        moves += get_move_sequence(start, end, move_positions)
    return moves


def p1(input_text):
    codes = input_text.split('\n')
    return sum(complexity(code, depth=3) for code in codes)


def p2(input_text):
    codes = input_text.split('\n')
    return sum(complexity(code, depth=26) for code in codes)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
