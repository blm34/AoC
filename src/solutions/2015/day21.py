import re
import math

import aoc_helper

DAY = 21
YEAR = 2015

SHOP = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""


def parse_input(input_text):
    kvs = re.findall(r'(.+): (\d+)', input_text)
    return {k: int(v) for k, v in kvs}


def parse_shop(shop_text):
    weapons_text, armor_text, rings_text = shop_text.split("\n\n")

    def parse(text):
        matches = re.findall(r'(^[\w\s+]+?)\s{2,}(\d+)\s{2,}(\d+)\s{2,}(\d+)', text, re.MULTILINE)
        return {weapon: {'cost': int(cost),
                         'damage': int(damage),
                         'armor': int(armor)}
                for weapon, cost, damage, armor in matches}

    shop = {'weapons': parse(weapons_text),
            'armor': parse(armor_text),
            'rings': parse(rings_text)}
    shop['armor']['none'] = {key: 0 for key in ('cost', 'damage', 'armor')}
    shop['rings']['none 1'] = {key: 0 for key in ('cost', 'damage', 'armor')}
    shop['rings']['none 2'] = {key: 0 for key in ('cost', 'damage', 'armor')}
    return shop


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    boss = parse_input(input_text)
    shop = parse_shop(SHOP)
    min_cost = 999999

    for weapon in shop['weapons'].values():
        for armor in shop['armor'].values():
            for ring1 in shop['rings'].values():
                for ring2 in shop['rings'].values():
                    if ring1 == ring2:
                        continue
                    my_hitpoints = 100
                    boss_hitpoints = boss['Hit Points']
                    my_damage = -boss['Armor']
                    boss_damage = boss['Damage']
                    cost = 0

                    for item in (weapon, armor, ring1, ring2):
                        cost += item['cost']
                        my_damage += item['damage']
                        boss_damage -= item['armor']
                    my_damage = max(my_damage, 1)
                    boss_damage = max(boss_damage, 1)

                    my_turns = math.ceil(boss_hitpoints / my_damage)
                    boss_turns = math.ceil(my_hitpoints / boss_damage)

                    if my_turns <= boss_turns and cost < min_cost:
                        min_cost = cost
    return min_cost


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    boss = parse_input(input_text)
    shop = parse_shop(SHOP)
    max_cost = 0

    for weapon in shop['weapons'].values():
        for armor in shop['armor'].values():
            for ring1 in shop['rings'].values():
                for ring2 in shop['rings'].values():
                    if ring1 == ring2:
                        continue
                    my_hitpoints = 100
                    boss_hitpoints = boss['Hit Points']
                    my_damage = -boss['Armor']
                    boss_damage = boss['Damage']
                    cost = 0

                    for item in (weapon, armor, ring1, ring2):
                        cost += item['cost']
                        my_damage += item['damage']
                        boss_damage -= item['armor']
                    my_damage = max(my_damage, 1)
                    boss_damage = max(boss_damage, 1)

                    my_turns = math.ceil(boss_hitpoints / my_damage)
                    boss_turns = math.ceil(my_hitpoints / boss_damage)

                    if my_turns > boss_turns and cost > max_cost:
                        max_cost = cost
    return max_cost


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
