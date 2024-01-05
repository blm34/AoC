import time
START_TIME = time.time()

import Modules
import sys

text = Modules.readInput(sys.argv[1]) 
L = text.split('\n')

def gen_input(L):
    reindeer = list()
    for line in L:
        _, _, _, speed, _, _, time, _, _, _, _, _, _, rest, _ = line.split()
        reindeer.append((int(speed), int(time), int(rest)))
    return reindeer

def distance(reindeer, time):
    speed, fly_time, rest_time = reindeer
    dist_per_cycle = fly_time * speed
    complete_cycles = time // (fly_time + rest_time)
    final_cycle_time = time % (fly_time + rest_time)

    d = dist_per_cycle * complete_cycles
    if final_cycle_time >= fly_time:
        d += dist_per_cycle
    else:
        d += final_cycle_time * speed

    return d
    
# Part 1
reindeers = gen_input(L)
p1 = max(distance(reindeer, 2503) for reindeer in reindeers)

# Part 2
points = [0] * len(reindeers)
for t in range(1, 2503+1):
    dists = [distance(reindeer, t) for reindeer in reindeers]
    winner = dists.index(max(dists))
    points[winner] += 1

p2 = max(points)

END_TIME = time.time()
RUN_TIME = round(1000*(END_TIME - START_TIME), 3)
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f'Run time: {RUN_TIME} ms')

assert p1 == 2655
assert p2 == 1059
