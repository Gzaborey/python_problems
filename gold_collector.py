import random
import itertools

max_depth = 7

rock = []

rock = [[7], [5, 8], [9, 8, 2], [1, 3, 5, 6],
        [6, 2, 4, 4, 5], [9, 5, 3, 5, 5, 7],
        [7, 4, 6, 4, 7, 6, 8]]

"""for y in range(max_depth):
    rock.append([random.randint(1, 9) for x in range(y + 1)])"""

print(rock)

x = [0, 1]
paths = [p for p in itertools.product(x, repeat=max_depth - 1)]

total_gold = []
for path in paths:
    x = 0
    y = 0
    gold = []
    gold = gold + [rock[y][x]]
    for direction in path:
        if direction == 0:
            y += 1
            gold = gold + [rock[y][x]]
        elif direction == 1:
            x += 1
            y += 1
            gold = gold + [rock[y][x]]

    total_gold.append(gold)

print(sum(max(total_gold)))
