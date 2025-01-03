import heapq

import aoc_helper

DAY = 24
YEAR = 2015


def parse_input(input_text):
    L = input_text.split('\n')
    list_weights = [int(num) for num in L]
    return list_weights


def get_min_entanglement(weights, target):
    weights = sorted(weights, reverse=True)
    q = list()
    heapq.heappush(q, (0, 0, [], weights))  # length, entanglement, used weights, available weights
    while q:
        length, entanglement, used_weights, available_weights = heapq.heappop(q)
        if sum(used_weights) == target:
            return entanglement
        for i in range(len(available_weights)):
            new_used_weights = used_weights + [available_weights[i]]
            if sum(new_used_weights) > target:
                continue
            heapq.heappush(q, (len(new_used_weights), aoc_helper.prod(new_used_weights), new_used_weights, available_weights[i+1:]))


def p1(input_text):
    weights = parse_input(input_text)
    target_weight = sum(weights) // 3

    return get_min_entanglement(weights, target_weight)


def p2(input_text):
    weights = parse_input(input_text)
    target_weight = sum(weights) // 4

    return get_min_entanglement(weights, target_weight)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
