from typing import List, Tuple
from collections import Counter, defaultdict, deque


def _reverse_rule(bag_rules):
    reverse_rule = defaultdict(set)
    for outer_bag, counter in bag_rules.items():
        for inner_bag, _ in counter.items():
            reverse_rule[inner_bag].add(outer_bag)
    return reverse_rule


def can_contrain(bag_rules, bag_name="shiny_gold"):
    graph = _reverse_rule(bag_rules)
    candidates = set()

    queue = deque([bag_name])

    while queue:
        q = queue.popleft()
        for n in graph[q]:
            if n not in candidates:
                candidates.add(n)
                queue.append(n)
    return len(candidates)


def bag_count(bag_rules, bag_name="shiny_gold"):
    if len(bag_rules[bag_name]) == 0:
        return 0

    res = 0
    for inner_bag, count in bag_rules[bag_name].items():
        res += count
        res += count * bag_count(bag_rules, inner_bag)
    return res


def build_bag_rules(lines):
    bag_rules = defaultdict(dict)
    for line in lines:
        words = line.split(" ")
        outer_bag = "_".join(words[:2])

        for w in range(4, len(words), 4):
            if words[w] == "no":
                continue
            inner_bag = "_".join(words[w+1: w+3])
            count = int(words[w])
            bag_rules[outer_bag][inner_bag] = count

    return bag_rules



if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        bag_rules = build_bag_rules(list(f.read().splitlines()))

    print("Part 1: ", can_contrain(bag_rules, "shiny_gold"))
    print("Part 2: ", bag_count(bag_rules, "shiny_gold"))