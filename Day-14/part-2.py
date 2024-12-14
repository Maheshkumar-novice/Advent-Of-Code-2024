import pprint
import re
from pathlib import Path

with open("input.txt") as f:
    values = [re.findall(r"(-?\d+),(-?\d+)", line) for line in f]
    grid = [["." for _ in range(101)] for _ in range(103)]
    max_x, max_y = 103, 101
    middle_x, middle_y = max_x // 2, max_y // 2
    time_elapsed = 1
    while True:
        answer_found = False
        current_positions = set()
        grid = [["." for _ in range(101)] for _ in range(103)]
        for position, velocity in values:
            vy, vx = int(velocity[0]) * time_elapsed, int(velocity[1]) * time_elapsed
            py, px = int(position[0]), int(position[1])
            px, py = (px + vx) % max_x, (py + vy) % max_y
            grid[px][py] = "#"

            current_positions.add((px, py))
            if (px, py + 1) in current_positions and not answer_found:
                flag = True
                for i in range(2, 7):
                    new_py = py + i
                    if (px, new_py) in current_positions:
                        continue
                    flag = False
                if flag:
                    answer_found = True

        if answer_found:
            Path("tree.txt").write_text(pprint.pformat(["".join(line) for line in grid]))
            break

        time_elapsed += 1

print(time_elapsed)
