with open("input.txt") as f:
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

    free_spaces = []
    free = 0
    for idx, char in enumerate(expanded_disk_map):
        if char == ".":
            free += 1
            continue

        if free:
            free_spaces.append((idx - free, idx - 1, free))
        free = 0

    last_char = expanded_disk_map[-1]
    count = 1
    char_idx = len(expanded_disk_map) - 1
    for char in expanded_disk_map[-2::-1]:
        char_idx -= 1
        if char == last_char:
            last_char = char
            count += 1
            continue
        else:
            if last_char != ".":
                space_found = False
                for idx, (start, end, space) in enumerate(free_spaces):
                    if space >= count and space and start <= end and start < char_idx:
                        temp_idx = start
                        temp_count = count
                        while temp_count:
                            expanded_disk_map[temp_idx] = last_char
                            temp_count -= 1
                            temp_idx += 1

                        for i in range(1, count + 1):
                            expanded_disk_map[char_idx + i] = "."

                        remaining_space = space - count
                        new_start = start + count
                        new_end = end
                        free_spaces[idx] = (new_start, new_end, remaining_space)
                        space_found = True

                    if space_found:
                        break

            last_char = char
            count = 1

    print(sum(int(char) * idx if char != "." else 0 for idx, char in enumerate(expanded_disk_map)))  # noqa: T201
