import pprint  # noqa: D100, INP001
from collections import defaultdict
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
    visited = set()
    for members in antennae.values():
        for member1, member2 in combinations(members, r=2):
            distance = dist(member1, member2)
            distance2 = 2 * distance
            for i in range(len(grid)):
                for j in range(len(grid)):
                    dist1 = dist(member1, (i, j))
                    dist2 = dist(member2, (i, j))
                    if distance in [dist1, dist2] and distance2 in [dist1, dist2]:
                        grid[i][j] = "#"
                        if (i, j) not in visited:
                            result += 1
                        visited.add((i, j))
    pprint.pprint(["".join(line) for line in grid])  # noqa: T203
    print(result)  # noqa: T201
