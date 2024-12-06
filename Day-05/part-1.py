with open("input.txt", "r") as f:
    rules, updates = f.read().split("\n\n")
    rules = rules.split("\n")

    rules_dict = {}

    for rule in rules:
        before, after = list(map(int, rule.split("|")))
        if before not in rules_dict:
            rules_dict[before] = {"before": [], "after": []}
        if after not in rules_dict:
            rules_dict[after] = {"before": [], "after": []}
        rules_dict[before]["after"].append(after)
        rules_dict[after]["before"].append(before)

    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]

    sum = 0
    for update in updates:
        flag = True
        for idx, page in enumerate(update[1:]):
            if update[idx] not in rules_dict[page]["before"]:
                flag = False
                break
        if flag:
            sum += update[len(update) // 2]

    print(sum)
