with open("input.txt") as f:
    grid_data = [list(line.strip()) for line in f]

directions = [
    (-1, -1),
    (-1, 1),  # Top row
    (1, -1),
    (1, 1),  # Bottom row
]
count = 0

for i in range(len(grid_data)):
    for j in range(len(grid_data)):
        s = grid_data[i][j]
        if s != "A":
            continue
        r, c = i, j
        v = []
        for dx, dy in directions:
            new_row, new_col = r + dx, c + dy
            if 0 <= new_row < len(grid_data) and 0 <= new_col < len(grid_data):
                v.append(grid_data[new_row][new_col])
        if v.count("M") == 2 and v.count("S") == 2 and v[0] != v[3] and v[1] != v[2]:
            count += 1
print(count)
