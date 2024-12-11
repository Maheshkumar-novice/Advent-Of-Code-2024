with open("input.txt") as f:  # noqa: D100, INP001, PTH123
    stones = f.read().split()

    def _apply_rule(stone: str):  # noqa: ANN202
        if stone == "0":
            yield "1"
        elif len(stone) % 2 == 0:
            yield str(int(stone[: len(stone) // 2]))
            yield str(int(stone[len(stone) // 2 :]))
        else:
            yield str(int(stone) * 2024)

    for i in range(25):
        new_stones = []
        for stone in stones:
            for _ in _apply_rule(stone):
                new_stones.append(i)  # noqa: PERF401
        stones = new_stones
    print(len(stones))  # noqa: T201
