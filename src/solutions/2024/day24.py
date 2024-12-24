import itertools

import aoc_helper

DAY = 24
YEAR = 2024


def parse_input(input_text):
    values_text, rules_text = input_text.split("\n\n")

    values = dict()
    for line in values_text.splitlines():
        k, v = line.split(": ")
        values[k] = int(v)

    rules = dict()
    for line in rules_text.splitlines():
        op1, op, op2, _, res = line.split()
        rules[res] = [op1, op, op2]

    return values, rules


def get_wire(wire, values, rules):
    if wire not in values:
        op1, op, op2 = rules[wire]
        op1 = get_wire(op1, values, rules)
        op2 = get_wire(op2, values, rules)
        values[wire] = calculate(op1, op, op2)
    return values[wire]


def calculate(op1, op, op2):
    match op:
        case "AND":
            return op1 and op2
        case "OR":
            return op1 or op2
        case "XOR":
            return int(op1 != op2)


def get_circuit_output(values, rules):
    binary = ""
    for i in itertools.count():
        wire = f"z{i:02d}"
        if wire in rules:
            binary = str(get_wire(wire, values, rules)) + binary
        else:
            return int(binary, 2)


def get_incorrect_wires(rules):
    incorrect = set()

    for res, (op1, op, op2) in rules.items():
        if op == "XOR":
            if res == "z00" and op1 in ("x00", "y00"):
                continue
            if op1[0] in "xy" and op2[0] in "xy":
                # If `res = x** XOR y**`, res cannot output z**. (other than `z00 = x00 XOR y00`)
                if res[0] == "z":
                    incorrect.add(res)
                else:
                    # If `res = x** XOR y**`, res must be input to another XOR
                    valid = False
                    for sub_op1, sub_op, sub_op2 in rules.values():
                        if sub_op == "XOR" and res in (sub_op1, sub_op2):
                            valid = True
                            break
                    if not valid:
                        incorrect.add(res)
            elif res[0] != "z":
                # If an XOR and not an x**, y** input, it must output to a z**
                incorrect.add(res)

        elif res[0] == "z" and res != "z45":
            # If not XOR, cannot output to a z**
            incorrect.add(res)

        if op == "AND" and op1[0] in "xy" and "x00" not in (op1, op2):
            # if `res = x** AND y**` then res must be input to an OR (other than `res = x00 AND y00`)
            valid = False
            for sub_op1, sub_op, sub_op2 in rules.values():
                if sub_op == "OR" and res in (sub_op1, sub_op2):
                    valid = True
                    break
            if not valid:
                incorrect.add(res)

    return incorrect


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    values, rules = parse_input(input_text)

    p1 = get_circuit_output(values, rules)

    incorrect = get_incorrect_wires(rules)
    p2 = ",".join(sorted(incorrect))

    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
