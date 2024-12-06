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

    incorrect_updates = []
    for update in updates:
        for idx, page in enumerate(update[1:]):
            if update[idx] not in rules_dict[page]["before"]:
                incorrect_updates.append(update)
                break

    updating = True
    while updating:
        updating = False
        for update in incorrect_updates:
            for idx, page in enumerate(update[1:]):
                if update[idx] not in rules_dict[page]["before"]:
                    updating = True
                    update[idx], update[idx + 1] = update[idx + 1], update[idx]

    print(sum(update[len(update) // 2] for update in incorrect_updates))
