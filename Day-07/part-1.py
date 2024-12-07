import operator
from itertools import product

with open("input.txt") as f:
    sum = 0
    operators = ["+", "*"]
    operator_map = {"+": operator.add, "*": operator.mul}
    for line in f:
        value, operands = line.split(":")
        operands = list(map(int, operands.strip().split()))
        operators_possibilities = product(operators, repeat=len(operands) - 1)

        for possibility in operators_possibilities:
            total = 0
            rs = None
            for idx, (operand, p) in enumerate(zip(operands[1:], possibility, strict=False)):
                op = operator_map[p]
                if not rs:
                    total = op(operands[idx], operand)
                    rs = total
                else:
                    total = op(rs, operand)
                    rs = total

            if total == int(value):
                sum += total
                break
    print(sum)
