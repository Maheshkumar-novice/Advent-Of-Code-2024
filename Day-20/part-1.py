from collections import deque
from copy import deepcopy

with open("input.txt") as f:
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
                    nnx, nny = nx + dx, ny + dy
                    if 0 <= nnx < grid_length and 0 <= nny < grid_length:
                        h.append((nnx, nny))
                    nnnx, nnny = nnx + dx, nny + dy
                    if 0 <= nnnx < grid_length and 0 <= nnny < grid_length:
                        h.append((nnnx, nnny))
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

    print(min_score)
    # exit()
    # print("\n".join(["".join(l) for l in grid]))
    visited.append((ex, ey))
    # print(visited)
    # print(hashes)
    for a in hashes:
        for x, y in a:
            hgrid[x][y] = "&"
    # print("\n".join(["".join(l) for l in hgrid]))


    cd = 0
    for hash in sorted(hashes):
        if len(hash) == 2:
            continue

        if len(hash) == 3:
            i, a, b = hash
            if grid[b[0]][b[1]] == ".":
                print(visited.index((b[0], b[1])))

        if len(hash) == 4:
            i, a, b, c = hash
            # print(grid[a[0]][a[1]])
            if grid[b[0]][b[1]] == ".":
                k = visited.index((b[0], b[1]))
                l = visited.index((i[0], i[1]))
                if 9440 - (l + (9440 - k) + 2) >= 100:
                    # print(84 - (l + (84 - k) + 2))
                    cd += 1
                # print(a,b,c, grid[a[0]][a[1]], grid[b[0]][b[1]],grid[c[0]][c[1]], l, k, l + (84 - k) + 2, 84 - (l + (84 - k) + 2))
            elif grid[c[0]][c[1]] == ".":
                k =  visited.index((c[0], c[1]))
                l = visited.index((i[0], i[1]))
                if 9440 - (l + (9440 - k) + 2) >= 100:
                    # print(84 - (l + (84 - k) + 2))
                    cd += 1
                # print(a,b,c, grid[a[0]][a[1]], grid[b[0]][b[1]], grid[c[0]][c[1]], l, k, l + (84 - k) + 2, 84 - (l + (84 - k) + 2))
    print(cd)