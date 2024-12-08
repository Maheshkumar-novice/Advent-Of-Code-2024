import operator  # noqa: INP001, D100
from concurrent.futures import ProcessPoolExecutor
from itertools import product

operator_map = {"+": operator.add, "*": operator.mul, "||": lambda a, b: int(f"{a}{b}")}


def process(line: str) -> int:  # noqa: D103
    value, operands = line.split(":")
    value = int(value)
    operands = list(map(int, operands.strip().split()))
    operators_possibilities = product(operator_map.keys(), repeat=len(operands) - 1)

    for possibility in operators_possibilities:
        total = 0
        for idx, (operand, operation) in enumerate(zip(operands[1:], possibility, strict=False)):
            operator_ = operator_map[operation]
            if not total:
                total = operator_(operands[idx], operand) if operation != "||" else int(operator_(str(operands[idx]), str(operand)))
            else:
                total = operator_(total, operand) if operation != "||" else int(operator_(str(total), str(operand)))

            if total > value:
                break

        if total == value:
            return total
    return 0


def recurse(total: int, value: int, operands: list[int]) -> int:  # noqa: D103
    if total == value and not operands:
        return total

    if total > value or not operands:
        return 0

    for op in operator_map.values():
        if recurse(op(total, operands[0]), value, operands[1:]):
            return value
    return 0


if __name__ == "__main__":
    import time

    s = time.monotonic()
    with open("input.txt") as f:  # noqa: PTH123
        with ProcessPoolExecutor(max_workers=6) as e:
            futures = [e.submit(process, line) for line in f]
            r = [k.result() for k in futures]

        print(sum(r))  # noqa: T201
    e = time.monotonic()
    print(" ->", e - s)  # noqa: T201

    s = time.monotonic()
    with open("input.txt") as f:  # noqa: PTH123
        r = 0
        for line in f:
            value, operands = line.split(":")
            value = int(value)
            operands = list(map(int, operands.strip().split()))
            r += recurse(operands[0], value, operands[1:])
        print(r)  # noqa: T201
    e = time.monotonic()
    print(" ->", e - s)  # noqa: T201

"""
401477450831495
 -> 8.011180688001332
401477450831495
 -> 3.3024124520015903

401477450831495
python part-2.py  21.36s user 0.29s system 605% cpu 3.579 total
"""
