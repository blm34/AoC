import re
import heapq

import aoc_helper

DAY = 22
YEAR = 2015


def parse_input(input_text):
    kvs = re.findall(r'(.+): (\d+)', input_text)
    return {k: int(v) for k, v in kvs}


def step(mana_spent, mana_left, my_hp, boss_hp, shield_cooldown, poison_cooldown, recharge_cooldown, boss_damage, spell_to_cast, part2=False):

    if part2:
        my_hp -= 1
        if my_hp <= 0:
            return

    # Use active potions
    if poison_cooldown > 0:
        boss_hp -= 3
    if recharge_cooldown > 0:
        mana_left += 101

    # Reduce cooldowns
    shield_cooldown = max(shield_cooldown - 1, 0)
    poison_cooldown = max(poison_cooldown - 1, 0)
    recharge_cooldown = max(recharge_cooldown - 1, 0)

    # Check if won
    if boss_hp <= 0:
        return mana_spent, mana_left, my_hp, boss_hp, shield_cooldown, poison_cooldown, recharge_cooldown

    # Player cast spell
    spell_cost = {'mm': 53,
                  'd': 73,
                  's': 113,
                  'p': 173,
                  'r': 229}[spell_to_cast]

    if spell_cost > mana_left:
        return

    mana_left -= spell_cost
    mana_spent += spell_cost

    if spell_to_cast == 'mm':
        boss_hp -= 4
    elif spell_to_cast == 'd':
        boss_hp -= 2
        my_hp += 2
    elif spell_to_cast == 's':
        if shield_cooldown > 0:
            return
        shield_cooldown = 6
    elif spell_to_cast == 'p':
        if poison_cooldown < 0:
            return
        poison_cooldown = 6
    elif spell_to_cast == 'r':
        if recharge_cooldown > 0:
            return
        recharge_cooldown = 5

    # Check if won
    if boss_hp <= 0:
        return mana_spent, mana_left, my_hp, boss_hp, shield_cooldown, poison_cooldown, recharge_cooldown

    # Use active potions
    if poison_cooldown > 0:
        boss_hp -= 3
    if recharge_cooldown > 0:
        mana_left += 101

    # Reduce cooldowns
    shield_cooldown = max(shield_cooldown - 1, 0)
    poison_cooldown = max(poison_cooldown - 1, 0)
    recharge_cooldown = max(recharge_cooldown - 1, 0)

    # Check if won
    if boss_hp <= 0:
        return mana_spent, mana_left, my_hp, boss_hp, shield_cooldown, poison_cooldown, recharge_cooldown

    # Boss deals damage
    d = boss_damage if shield_cooldown == 0 else max(boss_damage - 7, 1)
    my_hp -= d

    if my_hp <= 0:
        return

    return mana_spent, mana_left, my_hp, boss_hp, shield_cooldown, poison_cooldown, recharge_cooldown


def search_graph(boss, part2=False):
    states = list()
    heapq.heappush(states, (0, 500, 50, boss['Hit Points'], 0, 0, 0))
    while states:
        state = heapq.heappop(states)
        if state[3] <= 0:
            return state[0]
        for spell in ('mm', 'd', 's', 'p', 'r'):
            next_state = step(*state, boss['Damage'], spell, part2)
            if next_state is None:
                continue
            heapq.heappush(states, next_state)


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    boss = parse_input(input_text)
    return search_graph(boss)


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    boss = parse_input(input_text)
    return search_graph(boss, part2=True)


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
