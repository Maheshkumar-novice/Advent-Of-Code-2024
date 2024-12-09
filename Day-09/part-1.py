with open("input.txt") as f:  # noqa: PTH123, INP001, D100
    disk_map = f.read().strip()
    expanded_disk_map = []

    free_space = False
    ident = 0
    for thing in disk_map:
        if free_space:
            for _ in range(int(thing)):
                expanded_disk_map.append(".")  # noqa: PERF401
        else:
            for _ in range(int(thing)):
                expanded_disk_map.append(str(ident))  # noqa: PERF401
            ident += 1
        free_space = not free_space

    for idx, char in enumerate(expanded_disk_map):
        if char == ".":
            for block_idx in range(len(expanded_disk_map) - 1, idx, -1):
                if expanded_disk_map[block_idx] != ".":
                    expanded_disk_map[idx], expanded_disk_map[block_idx] = expanded_disk_map[block_idx], char
                    break

    print(sum(int(char) * idx for idx, char in enumerate(expanded_disk_map) if char != "."))  # noqa: T201
