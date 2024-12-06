with open("input.txt") as f:
    grid_data = [list(line.strip()) for line in f]

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),  # Top row
    (0, -1),
    (0, 1),  # Same row (left and right)
    (1, -1),
    (1, 0),
    (1, 1),  # Bottom row
]
count = 0
for dx, dy in directions:
    for i in range(len(grid_data)):
        for j in range(len(grid_data)):
            s = grid_data[i][j]
            r, c = i, j
            for k in range(3):
                new_row, new_col = r + dx, c + dy
                if 0 <= new_row < len(grid_data) and 0 <= new_col < len(grid_data):
                    s += grid_data[new_row][new_col]
                r, c = new_row, new_col
            if s == "XMAS":
                count += 1
print(count)