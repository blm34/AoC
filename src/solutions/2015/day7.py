from collections import deque

import aoc_helper

DAY = 7
YEAR = 2015


def parse_input(input_text):
    L = input_text.split("\n")
    return L


def get_instructions(lines):
    """Take the lines from the input and convert them into a deque of operations to perform"""
    Q = deque()
    for line in lines:
        instruction, destination = line.split(' -> ')
        instruction = instruction.split()
        if len(instruction) == 1:
            Q.append(['EQUAL', [instruction[0], ], None, destination])
        elif instruction[1] == 'AND':
            Q.append(['AND', [instruction[0], instruction[2]], None, destination])
        elif instruction[1] == 'OR':
            Q.append(['OR', [instruction[0], instruction[2]], None, destination])
        elif instruction[1] == 'LSHIFT':
            Q.append(['LSHIFT', [instruction[0], ], instruction[2], destination])
        elif instruction[1] == 'RSHIFT':
            Q.append(['RSHIFT', [instruction[0], ], instruction[2], destination])
        elif instruction[0] == 'NOT':
            Q.append(['NOT', [instruction[1], ], None, destination])
        else:
            assert False
    return Q


def run_instructions(Q):
    """Take a deque of instructions to perform, perform them, return the resulting value of a"""
    calculated = dict()
    while Q:
        # Take next instruction in queue
        operation, inps, amount, destination = Q.popleft()
        # Verify all inputs are calculated, else return to queue
        ready = True
        for i in inps:
            if (not i.isdigit()) and (i not in calculated):
                Q.append([operation, inps, amount, destination])
                ready = False
                break
        if not ready:
            continue
        # Find the values for all the inputs
        for i in range(len(inps)):
            if inps[i] in calculated:
                inps[i] = calculated[inps[i]]
            elif inps[i].isdigit():
                inps[i] = int(inps[i])
            else:
                assert False
        # Perform the calculation
        if operation == 'EQUAL':
            calculated[destination] = inps[0]
        elif operation == 'AND':
            calculated[destination] = inps[0] & inps[1]
        elif operation == 'OR':
            calculated[destination] = inps[0] | inps[1]
        elif operation == 'LSHIFT':
            calculated[destination] = inps[0] << int(amount)
        elif operation == 'RSHIFT':
            calculated[destination] = inps[0] >> int(amount)
        elif operation == 'NOT':
            calculated[destination] = ~inps[0] + 2 ** 16
        else:
            assert False
    return calculated['a']


def p1(input_text):
    L = parse_input(input_text)
    Q = get_instructions(L)
    return run_instructions(Q)


def p2(input_text):
    L = parse_input(input_text)
    Q = get_instructions(L)
    for i in range(len(Q)):
        if Q[i][3] == 'b':
            p1_ans = p1().answer
            Q[i][1] = [str(p1_ans)]
            break
    return run_instructions(Q)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
