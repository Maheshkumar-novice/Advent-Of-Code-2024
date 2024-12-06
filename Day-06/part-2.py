# PLEASE FIND A GOOD SOLUTION!
with open("input.txt") as f:  # noqa: PTH123
    lines = [list(line.strip()) for line in f]
    lines_length = len(lines)
    position_markers = ["^", "v", ">", "<"]
    marker_movements = {
        "^": (-1, 0),
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1),
    }
    next_marker = {"^": ">", ">": "v", "v": "<", "<": "^"}

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

    count = 0
    for x in range(lines_length):
        for y in range(lines_length):
            if (x, y) == position:
                continue
            if lines[x][y] == "#":
                continue

            lines[x][y] = "#"
            original_position = position
            old_position_marker = position_marker

            c = 0
            while True:
                dx, dy = marker_movements[position_marker]
                i, j = position[0] + dx, position[1] + dy

                if not (0 <= i < lines_length and 0 <= j < lines_length):
                    break

                if lines[i][j] == "#":
                    position_marker = next_marker[position_marker]
                    i, j = position
                position = (i, j)

                c += 1
                if c == 7500:
                    count += 1
                    break

            position = original_position
            position_marker = old_position_marker
            lines[x][y] = "."

    print(count)  # noqa: T201
