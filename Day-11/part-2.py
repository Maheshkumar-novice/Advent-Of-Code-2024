with open("input.txt") as f:  # noqa: D100, INP001, PTH123
    stones = f.read().split()

    from functools import cache

    @cache
    def _apply_rule(stone: str, blink: int):  # noqa: ANN202
        if blink <= 0:
            return 1

        if stone == "0":
            result = _apply_rule("1", blink - 1)
        elif len(stone) % 2 == 0:
            result = _apply_rule(str(int(stone[: len(stone) // 2])), blink - 1) + _apply_rule(str(int(stone[len(stone) // 2 :])), blink - 1)
        else:
            result = _apply_rule(str(int(stone) * 2024), blink - 1)
        return result

    print(sum(_apply_rule(stone, 75) for stone in stones))  # noqa: T201
