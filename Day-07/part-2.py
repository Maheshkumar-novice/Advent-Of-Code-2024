import operator  # noqa: INP001, D100
from itertools import product

with open("input.txt") as f:  # noqa: PTH123
    result = 0
    operator_map = {"+": operator.add, "*": operator.mul, "||": operator.concat}
    for line in f:
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

            if total == value:
                result += total
                break
    print(result)  # noqa: T201
