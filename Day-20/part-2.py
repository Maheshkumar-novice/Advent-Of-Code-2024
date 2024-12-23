from collections import deque
from copy import deepcopy

with open("sample.txt") as f:
    grid = [list(line.strip()) for line in f]
    hgrid = deepcopy(grid)
    grid_length = len(grid)
    directions = {"n": (-1, 0), "s": (1, 0), "e": (0, 1), "w": (0, -1)}
    sx, sy = next((i, j) for i in range(grid_length) for j in range(grid_length) if grid[i][j] == "S")
    ex, ey = next((i, j) for i in range(grid_length) for j in range(grid_length) if grid[i][j] == "E")
    hashes = []

    def _next_directions(x: int, y: int):  # noqa: ANN202
        next_directions = []
        for dx, dy in directions.values():
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_length and 0 <= ny < grid_length:
                if grid[nx][ny] != "#":
                    next_directions.append((nx, ny))
                else:
                    h = [(x, y)]
                    h.append((nx, ny))

                    nnx, nny = nx, ny
                    for _ in range(4):
                        nnx, nny = nnx + dx, nny + dy
                        if 0 <= nnx < grid_length and 0 <= nny < grid_length:
                            h.append((nnx, nny))
                    #     h.append((nnx, nny))
                    # nnnx, nnny = nnx + dx, nny + dy
                    # if 0 <= nnnx < grid_length and 0 <= nnny < grid_length:
                    #     h.append((nnnx, nnny))
                    hashes.append(h)
        return next_directions

    queue = deque([(sx, sy, 0)])
    min_score = float("inf")
    visited = list()
    while queue:
        x, y, score = queue.popleft()
        if (x, y) in visited:
            continue
        # grid[x][y]= "O"
        visited.append((x, y))

        for nx, ny in _next_directions(x, y):
            if (nx, ny) == (ex, ey):
                min_score = min(score + 1, min_score)
            else:
                queue.append((nx, ny, score + 1))
        # import os
        # from time import sleep
        # print("\n".join(["".join(l) for l in grid]))
        # sleep(0.1)
        # os.system("clear")

    # print(min_score)
    # print("\n".join(["".join(l) for l in grid]))
    visited.append((ex, ey))
    # print(visited)
    print(hashes)
    for a in hashes:
        for x, y in a:
            hgrid[x][y] = "&"
    # print("\n".join(["".join(l) for l in hgrid]))

    cd = 0
    vs = set(visited)
    for hash in sorted(hashes):
        print(hash)
        l1, l2 = hash[-1]
        if (l1, l2) not in vs:
            continue
        f1, f2 = hash[0]
        if (f1, f2) not in vs:
            continue
        k = visited.index((hash[-1][0], hash[-1][1]))
        l = visited.index((hash[0][0], hash[0][1]))
        if 84 - (l + (84 - k) + 2) >= 50:
            # print(84 - (l + (84 - k) + 2))
            cd += 1
        # for p, q in (hash):
        #     if grid[p][q] == ".":
        #         try:
        #             k = visited.index((hash[-1][0], hash[-1][1]))
        #             l = visited.index((hash[0][0], hash[0][1]))
        #             print(p, q, k, l, hash[0][0], hash[0][1])
        #             if 84 - (l + (84 - k) + 2) >= 50:
        #                 # print(84 - (l + (84 - k) + 2))
        #                 cd += 1
        #         except Exception as e:
        #             import traceback
        #             traceback.print_exc()
        #             break

    print(cd)