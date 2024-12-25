import aoc_helper

DAY = 25
YEAR = 2024


def parse_input(input_text):
    items = input_text.split("\n\n")

    keys = []
    locks = []

    for item in items:
        lines = item.splitlines()
        if item[0][0] == "#":
            # Lock
            lock = []
            for c in range(len(lines[0])):
                height = 0
                for r in range(1, len(lines)):
                    if lines[r][c] == "#":
                        height += 1
                    else:
                        break
                lock.append(height)
            locks.append(lock)

        else:
            # Key
            key = []
            for c in range(len(lines[0])):
                height = 0
                for r in range(len(lines) - 2, 0, -1):
                    if lines[r][c] == "#":
                        height += 1
                    else:
                        break
                key.append(height)
            keys.append(key)

    return locks, keys


def fit(lock, key):
    for c in range(len(lock)):
        if lock[c] + key[c] > 5:
            return False
    return True


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    locks, keys = parse_input(input_text)

    valid = sum(fit(lock, key)
                for key in keys
                for lock in locks)

    return valid, None


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
