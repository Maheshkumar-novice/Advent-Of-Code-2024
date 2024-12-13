from time import monotonic  # noqa: D100, INP001

import numpy as np

st = monotonic()
with open("input.txt") as f:  # noqa: PTH123
    all_details = [line.replace("Button", "").replace("Prize:", "").replace("A:", "").replace("B:", "").split() for line in f.read().split("\n\n")]

    for detail in all_details:
        for idx, eq in enumerate(detail):
            detail[idx] = eq.replace("X", "").replace("Y", "").replace("+", "").replace("=", "").replace(",", "")

    r = 0
    for detail in all_details:
        eq1 = list(map(int, [detail[0], detail[2]]))
        eq2 = list(map(int, [detail[1], detail[3]]))
        const = list(map(int, (str(10000000000000 + int(e)) for e in detail[4:])))

        x = np.array([eq1, eq2])
        y = np.array(const)
        s = np.linalg.solve(x, y)

        a, b = s
        a, b = round(a, 3), round(b, 3)

        if (np.mod(a, 1) == 0) and (np.mod(b, 1) == 0):
            r += (a * 3) + (b * 1)
        else:
            continue

    print(r)  # noqa: T201

print(monotonic() - st)  # noqa: T201

"""
time: 0.004672000010032207
"""
