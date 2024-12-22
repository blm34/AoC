import re

import aoc_helper

DAY = 23
YEAR = 2015


def parse_input(input_text):
    pattern = r"^(\w{3}) (\w|[+-]\d+)(, ([+-]\d+))?$"
    return re.findall(pattern, input_text, re.MULTILINE)


def execute(pointer, reg, instruction):
    if instruction[0] == 'hlf':
        r = instruction[1]
        reg[r] //= 2
    elif instruction[0] == 'tpl':
        r = instruction[1]
        reg[r] *= 3
    if instruction[0] == 'inc':
        r = instruction[1]
        reg[r] += 1
    if instruction[0] == 'jmp':
        offset = instruction[1]
        pointer += int(offset) - 1
    if instruction[0] == 'jie':
        r = instruction[1]
        if reg[r] % 2 == 0:
            offset = instruction[3]
            pointer += int(offset) - 1
    if instruction[0] == 'jio':
        r = instruction[1]
        if reg[r] == 1:
            offset = instruction[3]
            pointer += int(offset) - 1
    pointer += 1
    return pointer, reg


def run_program(program, reg, pointer=0):
    while 0 <= pointer < len(program):
        pointer, reg = execute(pointer, reg, program[pointer])
    return reg


def p1(input_text):
    instructions = parse_input(input_text)
    reg = {'a':0, 'b':0}
    reg = run_program(instructions, reg)
    return reg['b']


def p2(input_text):
    instructions = parse_input(input_text)
    reg = {'a':1, 'b':0}
    reg = run_program(instructions, reg)
    return reg['b']


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
