import operator  # noqa: INP001, D100
from itertools import product

with open("input.txt") as f:  # noqa: PTH123
    result = 0
    operator_map = {"+": operator.add, "*": operator.mul}
    for line in f:
        value, operands = line.split(":")
        value = int(value)
        operands = list(map(int, operands.strip().split()))
        operators_possibilities = product(operator_map.keys(), repeat=len(operands) - 1)

        for possibility in operators_possibilities:
            total = 0
            for idx, (operand, operation) in enumerate(zip(operands[1:], possibility, strict=False)):
                operator_ = operator_map[operation]
                total = operator_(operands[idx], operand) if not total else operator_(total, operand)

            if total == value:
                result += total
                break
    print(result)  # noqa: T201

"""
2314935962622
         2183052 function calls in 0.709 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.709    0.709 {built-in method builtins.exec}
        1    0.579    0.579    0.709    0.709 part-1.py:1(<module>)
  1125766    0.066    0.000    0.066    0.000 {built-in method _operator.add}
  1053016    0.063    0.000    0.063    0.000 {built-in method _operator.mul}
     1700    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _io.open}
      850    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
      850    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
      850    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        6    0.000    0.000    0.000    0.000 <frozen codecs>:319(decode)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
        6    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 <frozen codecs>:309(__init__)
        1    0.000    0.000    0.000    0.000 <frozen codecs>:260(__init__)
"""
