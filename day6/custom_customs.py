from typing import List, Tuple
from collections import Counter


def get_group_sum(group_counts):
    res = 0
    for count in group_counts:
        res += len(count)
    return res


def get_all_sum(group_counts, person_counts):
    res = 0
    for count, p_count in zip(group_counts, person_counts):
        for key, val in count.items():
            if val == p_count:
                res += 1
    return res


def get_group_count(lines):
    group_counts = []
    person_counts = []
    p_count = 0
    count = Counter()
    for line in lines:
        if not line:
            if count:
                group_counts.append(count)
                person_counts.append(p_count)
            count = Counter()
            p_count = 0
        else:
            p_count += 1
            for l in line:
                count[l] += 1
    if count:
        person_counts.append(p_count)
        group_counts.append(count)
    return group_counts, person_counts



if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        group_counts, person_counts = get_group_count(list(f.read().splitlines()))

    print("Part 1: ", get_group_sum(group_counts))
    print("Part 2: ", get_all_sum(group_counts, person_counts))