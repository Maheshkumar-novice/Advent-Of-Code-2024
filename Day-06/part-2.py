import pprint
# PLEASE FIND A GOOD SOLUTION!
with open("input.txt", "r") as f:
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

    def is_out_of_bound(i, j):
        return not (0 <= i < lines_length and 0 <= j < lines_length)

    def get_next_position(i, j, symbol):
        dx, dy = marker_movements[symbol]
        return i + dx, j + dy

    count = 0
    for x in range(lines_length):
        for y in range(lines_length):
            if (x, y) == position:
                continue
            if lines[x][y] == "#":
                continue
            # print(x,y)
            lines[x][y] = "#"
            ops = position
            pm = position_marker
            obs_count = {}
            # pprint.pprint((list("".join(line) for line in lines)))

            c = 0
            while True:
                old_position = position
                # lines[i][j] = position_marker
                i, j = get_next_position(position[0], position[1], position_marker)

                if is_out_of_bound(i, j):
                    # print(i,j)
                    break

                if lines[i][j] == "#":
                    # obs_count[(i, j)x] = obs_count.get((i, j), 0) + 1
                    # if obs_count[(i, j)] == 2:
                    #     print(obs_count)
                    #     pprint.pprint((list("".join(line) for line in lines)))

                    #     print(i, j)
                    #     count += 1
                    #     break
                    position_marker = next_marker[position_marker]
                    i, j = old_position
                position = (i, j)

                c += 1
                if c == 7500:
                    count += 1
                    break

            position = ops
            position_marker = pm
            lines[x][y] = "."

    # pprint.pprint((list("".join(line) for line in lines)))
    print(count)
