with open("input.txt") as f:
    garden = [list(line.strip()) for line in f]
    directions = {"d": (1, 0), "u": (-1, 0), "r": (0, 1), "l": (0, -1)}
    x_configs = {"tr": (-1, 1), "tl": (-1, -1), "br": (1, 1), "bl": (1, -1)}

    class Plot:  # noqa: D101
        def __init__(self, x: int, y: int) -> None:  # noqa: D107
            self.x = x
            self.y = y
            self.weight = 0
            self.fences = None
            self.locked = None
            self.straight_neighbours = None

        def __str__(self) -> str:  # noqa: D105
            return f"Plot<{garden[self.x][self.y]}, {self.x=}, {self.y=}, {self.weight=}, {sorted(self.fences)!s}>"

    def _in_bound(x: int, y: int) -> bool:
        return 0 <= x < len(garden) and 0 <= y < len(garden)

    def _get_neighbour_plot(x: int, y: int):  # noqa: ANN202
        for dx, dy in directions.values():
            new_x, new_y = x + dx, y + dy
            if _in_bound(new_x, new_y):
                yield new_x, new_y

    def _get_diagonal_neighbour_plot(x: int, y: int):  # noqa: ANN202
        for dir, (dx, dy) in x_configs.items():  # noqa: A001
            new_x, new_y = x + dx, y + dy
            if _in_bound(new_x, new_y):
                yield dir, new_x, new_y

    plots, plot_map = [], {}
    for i in range(len(garden)):
        for j in range(len(garden)):
            plot = Plot(i, j)
            plot_dirs = set()
            ps = set()

            for direction, (dx, dy) in directions.items():
                new_x, new_y = i + dx, j + dy
                if _in_bound(new_x, new_y):
                    if garden[new_x][new_y] == garden[i][j]:
                        continue
                    else:
                        plot_dirs.add(direction)
                else:
                    plot_dirs.add(direction)

            if len(plot_dirs) == 3:  # noqa: PLR2004
                plot.weight = 2
            elif len(plot_dirs) == 4:  # noqa: PLR2004
                plot.weight = 4
            elif len(plot_dirs) == 2:  # noqa: PLR2004
                if ("u" in plot_dirs and "d" not in plot_dirs) or ("d" in plot_dirs and "u" not in plot_dirs):
                    plot.weight = 1

                if "u" in plot_dirs and "l" in plot_dirs:
                    ps = {"l", "u"}
                elif "u" in plot_dirs and "r" in plot_dirs:
                    ps = {"r", "u"}
                elif "d" in plot_dirs and "l" in plot_dirs:
                    ps = {"l", "d"}
                elif "d" in plot_dirs and "r" in plot_dirs:
                    ps = {"r", "d"}
                elif "u" in plot_dirs and "d" in plot_dirs:
                    ps = {"l", "r"}
                elif "l" in plot_dirs and "r" in plot_dirs:
                    ps = {"u", "d"}

            if len(plot_dirs) == 1:
                if "u" in plot_dirs or "d" in plot_dirs:
                    ps = {"l", "r"}
                elif "l" in plot_dirs or "r" in plot_dirs:
                    ps = {"u", "d"}

            if len(plot_dirs) == 3:  # noqa: PLR2004
                if "u" in plot_dirs and "d" in plot_dirs and "l" in plot_dirs:
                    ps = {"l"}
                elif "u" in plot_dirs and "d" in plot_dirs and "r" in plot_dirs:
                    ps = {"r"}
                elif "l" in plot_dirs and "r" in plot_dirs and "u" in plot_dirs:
                    ps = {"u"}
                elif "l" in plot_dirs and "r" in plot_dirs and "d" in plot_dirs:
                    ps = {"d"}

            plot.ps = ps
            plot.fences = plot_dirs
            plots.append(plot)
            plot_map[(i, j)] = plot

    r = 0
    global_visited = set()
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if (i, j) in global_visited:
                continue

            visited = set()
            q = set()
            q.add((i, j))
            while q:
                x, y = q.pop()
                visited.add((x, y))

                for new_x, new_y in _get_neighbour_plot(x, y):
                    if garden[new_x][new_y] == garden[x][y] and (new_x, new_y) not in visited:
                        q.add((new_x, new_y))

            a = 0
            bs = set()
            for x, y in sorted(visited):
                global_visited.add((x, y))
                plot = plot_map[(x, y)]
                if len(plot.fences) < 4:  # noqa: PLR2004
                    for dir, dx, dy in _get_diagonal_neighbour_plot(plot.x, plot.y):  # noqa: A001
                        if garden[dx][dy] == garden[plot.x][plot.y] and (dx, dy) in visited:
                            t = plot_map[(dx, dy)]

                            if len(plot.fences) != 3:  # noqa: PLR2004
                                if (plot.x, plot.y, dx, dy) in bs:
                                    continue
                                elif "d" in plot.fences and dir in ["bl", "br"]:
                                    if plot.ps.intersection(t.fences) and dir == "bl" and "r" in plot.ps.intersection(t.fences):
                                        plot.weight += 1
                                    if plot.ps.intersection(t.fences) and dir == "br" and "l" in plot.ps.intersection(t.fences):
                                        plot.weight += 1
                                elif "u" in plot.fences and dir in ["tl", "tr"]:
                                    if plot.ps.intersection(t.fences) and dir == "tl" and "r" in plot.ps.intersection(t.fences):
                                        plot.weight += 1
                                    if plot.ps.intersection(t.fences) and dir == "tr" and "l" in plot.ps.intersection(t.fences):
                                        plot.weight += 1
                                elif "l" in plot.fences and dir in ["tl", "bl"]:
                                    if plot.ps.intersection(t.fences) and dir == "tl" and "d" in plot.ps.intersection(t.fences):
                                        plot.weight += 1
                                    if plot.ps.intersection(t.fences) and dir == "bl" and "u" in plot.ps.intersection(t.fences):
                                        plot.weight += 1
                                elif "r" in plot.fences and dir in ["tr", "br"]:
                                    if plot.ps.intersection(t.fences) and dir == "tr" and "d" in plot.ps.intersection(t.fences):
                                        plot.weight += 1
                                    if plot.ps.intersection(t.fences) and dir == "br" and "u" in plot.ps.intersection(t.fences):
                                        plot.weight += 1

                                bs.add((dx, dy, plot.x, plot.y))
                            else:
                                if (plot.x, plot.y, dx, dy) in bs:
                                    continue
                                elif (
                                    ("u" in plot.fences and "d" in plot.fences and "l" in plot.fences and dir in ["tr", "br"] and plot.ps.intersection(t.fences))
                                    or ("u" in plot.fences and "d" in plot.fences and "r" in plot.fences and dir in ["tl", "bl"] and plot.ps.intersection(t.fences))
                                    or ("l" in plot.fences and "r" in plot.fences and "u" in plot.fences and dir in ["br", "bl"] and plot.ps.intersection(t.fences))
                                    or ("l" in plot.fences and "r" in plot.fences and "d" in plot.fences and dir in ["tr", "tl"] and plot.ps.intersection(t.fences))
                                ):
                                    plot.weight += 1
                                bs.add((dx, dy, plot.x, plot.y))

                a += plot.weight
            r += a * len(visited)
print(r)
