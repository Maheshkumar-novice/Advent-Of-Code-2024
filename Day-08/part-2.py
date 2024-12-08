from collections import defaultdict  # noqa: D100, INP001
from itertools import combinations
from math import dist

with open("input.txt") as f:  # noqa: PTH123
    grid = [list(line.strip()) for line in f]
    antennae = defaultdict(list)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                antennae[grid[i][j]].append((i, j))

    result = 0
    for members in antennae.values():
        for member1, member2 in combinations(members, r=2):
            distance = dist(member1, member2)
            distance2 = 2 * distance
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if grid[i][j] != "#":
                        x1, y1 = member1
                        x2, y2 = member2
                        x3, y3 = (i, j)

                        # some collinear formula
                        if abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
                            grid[i][j] = "#"
                            result += 1
    print(result)  # noqa: T201
