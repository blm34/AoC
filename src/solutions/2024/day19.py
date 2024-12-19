from functools import cache

import aoc_helper

DAY = 19
YEAR = 2024


class TrieNode:
    def __init__(self):
        self.end = False
        self.children = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, value):
        node = self.root
        for char in value:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def valid_prefixes(self, string):
        node = self.root
        prefix = ""
        for char in string:
            if char not in node.children:
                return
            prefix += char
            node = node.children[char]
            if node.end:
                yield prefix


def parse_input(input_text):
    towels, patterns = input_text.split("\n\n")
    towels = tuple(towels.split(", "))
    patterns = patterns.split("\n")
    towels_trie = Trie()
    for towel in towels:
        towels_trie.add(towel)
    return towels_trie, patterns


@cache
def possible_pattern(pattern, towels):
    if pattern == "":
        return True
    for towel in towels.valid_prefixes(pattern):
        if pattern.startswith(towel) and possible_pattern(pattern.removeprefix(towel), towels):
            return True
    return False


@cache
def count_pattern(pattern, towels):
    if pattern == "":
        return 1
    count = 0
    for towel in towels.valid_prefixes(pattern):
        if pattern.startswith(towel):
            count += count_pattern(pattern.removeprefix(towel), towels)
    return count


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    towels, patterns = parse_input(input_text)
    return sum(possible_pattern(pattern, towels) for pattern in patterns)


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    towels, patterns = parse_input(input_text)
    return sum(count_pattern(pattern, towels) for pattern in patterns)


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
