from collections import defaultdict, deque
from functools import cache
from itertools import pairwise

with open("sample.txt") as f:
    keypad = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["", "0", "A"],
    ]
    keypad_index = {}
    for i in range(4):
        for j in range(3):
            keypad_index[keypad[i][j]] = (i, j)

    directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

    @cache
    def _next_directions(x: int, y: int):  # noqa: ANN202
        next_directions = []
        for direction, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 3 and keypad[nx][ny] != "":
                next_directions.append((direction, nx, ny))
        return next_directions

    @cache
    def get_shortest_path_to(sx, sy, ex, ey):
        queue = deque([(sx, sy, 0, [], "")])
        vertice_scores = {}
        min_score = float("inf")
        score_path_map = defaultdict(list)
        while queue:
            x, y, score, path, direction = queue.popleft()
            path.append((x, y, direction))
            if (x, y) in vertice_scores and score > vertice_scores[(x, y)]:
                continue
            vertice_scores[(x, y)] = score

            for new_direction, nx, ny in _next_directions(x, y):
                if keypad[nx][ny] == keypad[ex][ey]:
                    # if score + 1 == min_score:
                    #     continue
                    min_score = min(score + 1, min_score)
                    score_path_map[score + 1].append(path + [(ex, ey, new_direction)])
                    # for fx, fy, direction in path:
                    # score_path_map[score + 1].append((ex, ey, new_direction))
                else:
                    queue.append((nx, ny, score + 1, path.copy(), new_direction))
        return score_path_map[min_score]

    value = "A319A"
    paths = []
    for x, y in pairwise(value):
        new = []
        for path in get_shortest_path_to(*keypad_index[x], *keypad_index[y]):
            op = ""
            for a, b, direction in path:
                op += direction
            new.append( op + "A")
        paths.append(new)
    from itertools import product

    np =[]
    for i in product(*paths):
        np.append("".join(i))

    arrow_keypad = [
        ["", "^", "A"],
        ["<", "v", ">"],
    ]
    arrow_keypad_index = {}
    for i in range(2):
        for j in range(3):
            arrow_keypad_index[arrow_keypad[i][j]] = (i, j)

    directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

    @cache
    def _next_directions(x: int, y: int):  # noqa: ANN202
        next_directions = []
        for direction, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < 2 and 0 <= ny < 3 and arrow_keypad[nx][ny] != "":
                next_directions.append((direction, nx, ny))
        return next_directions

    @cache
    def get_shortest_path_to(sx, sy, ex, ey):
        if arrow_keypad[sx][sy] == arrow_keypad[ex][ey]:
            return [[("", "", "")]]
        queue = deque([(sx, sy, 0, [], "")])
        vertice_scores = {}
        min_score = float("inf")
        score_path_map = defaultdict(list)
        while queue:
            x, y, score, path, direction = queue.popleft()
            path.append((x, y, direction))
            if (x, y) in vertice_scores and score > vertice_scores[(x, y)]:
                continue
            vertice_scores[(x, y)] = score

            for new_direction, nx, ny in _next_directions(x, y):
                if arrow_keypad[nx][ny] == arrow_keypad[ex][ey]:
                    # if score + 1 == min_score:
                    #     continue
                    min_score = min(score + 1, min_score)
                    score_path_map[score + 1].append(path + [(ex, ey, new_direction)])
                    # for fx, fy, direction in path:
                    # score_path_map[score + 1].append((ex, ey, new_direction))
                else:
                    queue.append((nx, ny, score + 1, path.copy(), new_direction))
        return score_path_map[min_score]


    newp = []
    for value in np:
        value = "A" + value
        paths = []
        for x, y in pairwise(value):
            new = []
            for path in get_shortest_path_to(*arrow_keypad_index[x], *arrow_keypad_index[y]):
                op = ""
                for a, b, direction in path:
                    op += direction
                new.append( op + "A")
            paths.append(new)
        from itertools import product
        for i in product(*paths):
            newp.append("".join(i))
            # print(len("".join(i)), value)
    # print(newp)

    newpp = []
    from collections import defaultdict
    newpp = defaultdict(list)
    for value in newp:
        value = "A" + value
        paths = []
        for x, y in pairwise(value):
            new = []
            for path in get_shortest_path_to(*arrow_keypad_index[x], *arrow_keypad_index[y]):
                op = ""
                for a, b, direction in path:
                    op += direction
                new.append( op + "A")
            paths.append(new)
        from itertools import product
        for i in product(*paths):
            v = "".join(i)
            newpp[len(v)].append(v)
            # print(len("".join(i)))
    print(min(newpp.keys()))
    print(len(newpp[68]))

    # value = "A" + operation
    # operation = ""
    # for x, y in pairwise(value):
    #     op = ""
    #     for a, b, direction in get_shortest_path_to(*arrow_keypad_index[x], *arrow_keypad_index[y]):
    #         op += direction
    #     operation += op + "A"
    #     print(x, y, op)

    # print(arrow_keypad_index, operation, len(operation))

    # value = "A" + operation
    # operation = ""
    # for x, y in pairwise(value):
    #     op = ""
    #     for a, b, direction in get_shortest_path_to(*arrow_keypad_index[x], *arrow_keypad_index[y]):
    #         op += direction
    #     operation += op + "A"
    #     # print(x, y, op)

    # print(arrow_keypad_index, operation, len(operation))
