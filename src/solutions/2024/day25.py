import aoc_helper

DAY = 25
YEAR = 2024

width = 5
height = 7


def parse_input(input_text):
    items = input_text.split("\n\n")

    keys = []
    locks = []

    for item in items:
        # Encode keys/locks in binary where 1 represents a `#` and 0 a `.`
        #  As valid if no overlapping #'s, valid if key bitwise and lock is 0
        value = 0
        for char in item[width:-width]:
            if char == "\n":
                continue
            if char == "#":
                value += 1
            value *= 2

        if item[0] == "#":
            locks.append(value)
        else:
            keys.append(value)

    return locks, keys


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    locks, keys = parse_input(input_text)

    valid = sum(lock & key == 0
                for key in keys
                for lock in locks)

    return valid, None


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
