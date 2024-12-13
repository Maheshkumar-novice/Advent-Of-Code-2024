# ONLY WORKS FOR SAMPLE INPUT LOL!!
# I SHOULD HAVE DESIGNED THIS WELL!

from collections.abc import Generator
from typing import Any

with open("input.txt") as f:
    garden = [list(line.strip()) for line in f]
    directions = {
        "d": (1, 0),
        "u": (-1, 0),
        "r": (0, 1),
        "l": (0, -1),
    }

    def _in_bound(x: int, y: int) -> bool:
        return 0 <= x < len(garden) and 0 <= y < len(garden)

    from collections import defaultdict

    plot_directions = defaultdict(set)
    plot_points = defaultdict(set)

    def _get_neighbour_area(x: int, y: int) -> Generator[tuple[int, int], Any, None]:
        for direction, (dx, dy) in directions.items():
            new_x, new_y = x + dx, y + dy
            if _in_bound(new_x, new_y):
                if garden[new_x][new_y] == garden[x][y]:
                    yield 0
                else:
                    plot_directions[(x, y)].add(direction)
                    plot_points[(x, y)].add((new_x, new_y))
                    yield 1
            else:
                plot_directions[(x, y)].add(direction)
                plot_points[(x, y)].add((new_x, new_y))
                yield 1

    def _get_neighbour_plot(x: int, y: int) -> Generator[tuple[int, int], Any, None]:
        for dx, dy in directions.values():
            new_x, new_y = x + dx, y + dy
            if _in_bound(new_x, new_y):
                yield new_x, new_y

    x_configs = [
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    def _get_diagonal_neighbour_plot(x: int, y: int) -> Generator[tuple[int, int], Any, None]:
        for dx, dy in x_configs:
            new_x, new_y = x + dx, y + dy
            if _in_bound(new_x, new_y):
                yield new_x, new_y

    def _is_a_corner(dirs):
        if len(dirs) < 2:
            return False

        if len(dirs) == 3 or len(dirs) == 4:
            return True

        if "u" in dirs and "d" not in dirs:
            return True

        if "d" in dirs and "u" not in dirs:
            return True

        return False

    def _corner_incr(size):
        if size == 3:
            return 2

        if size == 4:
            return 4

        return 1

    def _valid_intersection(p1, p2):
        a, b = p1
        x, y = p2

        if b > y:
            a, b = a, b - 1
            x, y = x, y + 1
        else:
            x, y = x, y - 1
            a, b = a, b + 1

        return garden[a][b] != garden[x][y]

    def _find_area(visited):
        old_visited = visited
        visited = list(sorted(visited))
        # print(visited)
        result = 0
        from collections import defaultdict

        corners = defaultdict(set)
        cm = 0
        tc = []
        for a, b in visited:
            # print()
            dirs = plot_directions[(a, b)]
            points = plot_points[(a, b)]
            # print("=====", a, b, garden[a][b], dirs, points)
            # print("Corner: ", _is_a_corner(dirs))
            if _is_a_corner(dirs):
                # print("Corner Value: ", _corner_incr(len(dirs)))
                tc.append((a, b, _corner_incr(len(dirs))))
                result += _corner_incr(len(dirs))

            for x, y in _get_diagonal_neighbour_plot(a, b):
                if garden[x][y] == garden[a][b] and (x, y) in old_visited:
                    new_dirs = plot_directions[(x, y)]
                    new_plots = plot_points[(x, y)]
                    k = points.intersection(new_plots)
                    if k:
                        # print(_valid_intersection((a, b), (x, y)))
                        # print(k.pop())
                        k = True
                    if k and (x, y) not in corners and _valid_intersection((a, b), (x, y)):
                        corners[(x, y)].add((a, b))
                        corners[(a, b)].add((x, y))
                        tc.append((x, y, 1))
                        cm += 1
                    elif k and (x, y) in corners and (a, b) not in corners[(x, y)] and _valid_intersection((a, b), (x, y)):
                        corners[(x, y)].add((a, b))
                        corners[(a, b)].add((x, y))
                        tc.append((x, y, 1))
                        cm += 1

                    # print(x, y, garden[x][y], new_dirs, new_plots, cm, corners)
        # print("TC: ", sorted(tc), len(tc))
        return result + cm

    garden_plot_area = [[0 for _ in range(len(garden))] for _ in range(len(garden[0]))]
    for i in range(len(garden)):
        for j in range(len(garden)):
            plot = garden[i][j]

            plot_area = 0
            for area in _get_neighbour_area(i, j):
                plot_area += area
            garden_plot_area[i][j] = plot_area

    global_visited = set()
    r = 0
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if (i, j) in global_visited:
                continue

            visited = set()
            q = set()
            q.add((i, j))
            while q:
                x, y = q.pop()
                visited.add((x, y))

                for new_x, new_y in _get_neighbour_plot(x, y):
                    if garden[new_x][new_y] == garden[x][y] and (new_x, new_y) not in visited:
                        q.add((new_x, new_y))

            a = _find_area(visited)
            # print("xxxxxxxx------------xxxxxxxx")
            print("Plot: ", garden[i][j], "Side: ", a, "   Area: ", len(visited), " ", a * len(visited))
            # print("xxxxxxxx------------xxxxxxxx")
            r += len(visited) * a
            for x, y in visited:
                global_visited.add((x, y))

    print(r)

# 824489
