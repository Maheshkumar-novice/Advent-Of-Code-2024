import re

with open("input.txt") as f:
    matches, sum, do = re.findall(r"(l\((\d+),(\d+)\))|(do\()|(don't)", f.read()), 0, True

    for match in matches:
        if match[4] == "don't":
            do = False
            continue

        if match[3] == "do(":
            do = True
            continue

        if do:
            sum += int(match[1]) * int(match[2])
    print(sum)
