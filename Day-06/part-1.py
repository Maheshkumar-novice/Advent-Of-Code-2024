with open("input.txt") as f:  # noqa: PTH123, INP001, D100
    lines = [list(line.strip()) for line in f]
    position_markers = ["^", "v", ">", "<"]
    lines_length = len(lines)

    position_found = False
    for i in range(lines_length):
        for j in range(lines_length):
            if lines[i][j] in position_markers:
                position_marker = lines[i][j]
                position = (i, j)
                position_found = True
                break

        if position_found:
            break

    marker_movements = {
        "^": (-1, 0),
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1),
    }

    next_marker = {"^": ">", ">": "v", "v": "<", "<": "^"}

    def is_out_of_bound(i: int, j: int) -> bool:  # noqa: D103
        return not (0 <= i < lines_length and 0 <= j < lines_length)

    def get_next_position(i: int, j: int, symbol: str) -> tuple[int, int]:  # noqa: D103
        dx, dy = marker_movements[symbol]
        return i + dx, j + dy

    visited = set()
    while True:
        visited.add(position)
        old_position = position
        lines[i][j] = position_marker
        i, j = get_next_position(position[0], position[1], position_marker)

        if is_out_of_bound(i, j):
            break

        if lines[i][j] == "#":
            position_marker = next_marker[position_marker]
            i, j = old_position

        position = (i, j)

    import pprint

    pprint.pprint(["".join(line) for line in lines])  # noqa: T203
    print(len(visited))  # noqa: T201
