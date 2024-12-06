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
    for row in range(len(grid_data)):
        for col in range(len(grid_data)):
            text = grid_data[row][col]
            temp_row, temp_col = row, col
            for _ in range(3):
                new_row, new_col = temp_row + dx, temp_col + dy
                if 0 <= new_row < len(grid_data) and 0 <= new_col < len(grid_data):
                    text += grid_data[new_row][new_col]
                temp_row, temp_col = new_row, new_col
            if text == "XMAS":
                count += 1
print(count)
