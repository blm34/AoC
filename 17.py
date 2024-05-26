import time
import Modules

START_TIME = time.time()

text = Modules.read_input('17.txt')
L = text.split('\n')

containers = [int(x) for x in L]
containers.sort()
quantity = 150


def dp1(remaining, target):
    if target <= 0:
        return int(target == 0)
    total = 0
    for i in range(len(remaining)):
        total += dp1(remaining[i + 1:], target - remaining[i])
    return total


def dp2(used, remaining, target):
    if target == 0:
        return (len(used), 1)
    if target < 0:
        return None
    ans = None
    for i, bucket in enumerate(remaining):
        next_ans = dp2(used + [bucket], remaining[i + 1:], target - bucket)
        if next_ans is None:
            continue
        elif ans is None:
            ans = next_ans
        elif next_ans[0] == ans[0]:
            ans = (ans[0], next_ans[1] + ans[1])
        elif next_ans[0] < ans[0]:
            ans = next_ans
    return ans


p1 = dp1(containers, quantity)
p2 = dp2([], containers, quantity)[0]

END_TIME = time.time()
RUN_TIME = END_TIME - START_TIME
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f'Run time: {1000*RUN_TIME:.3f} ms')
