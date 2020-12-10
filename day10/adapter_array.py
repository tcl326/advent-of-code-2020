from typing import List, Tuple
from collections import Counter, defaultdict, deque


def find_all_combinations(adapters):
    adapters.sort()
    start = 0
    end = max(adapters) + 3

    memo = {}

    def dfs(idx):
        if idx in memo:
            return memo[idx]
        if _can_link(adapters[idx], end):
            return 1
        res = 0
        for i in range(idx + 1, len(adapters)):
            if not _can_link(adapters[idx], adapters[i]):
                break
            res += dfs(i)
        memo[idx] = res
        return res

    res = 0
    for i in range(len(adapters)):
        if not _can_link(0, adapters[i]):
            break
        res += dfs(i)
    return res


def _can_link(input_, rating):
    if rating - input_ > 0 and rating - input_ < 4:
        return True
    return False


def adapter_chain(adapters):
    end = max(adapters) + 3
    def dfs(curr, path, left):
        if not left and _can_link(curr, end):
            return path + [end]
        for l in left:
            if not _can_link(curr, l):
                continue
            p = dfs(l, path + [l], left - {l})
            if p:
                return p
        return None

    start = 0
    path = dfs(start, [0], set(adapters))
    return path


def one_three_differences(path):
    one_count = 0
    three_count = 0
    for i in range(1, len(path)):
        if abs(path[i] - path[i - 1]) == 1:
            one_count += 1
        if abs(path[i] - path[i - 1]) == 3:
            three_count += 1
    return one_count * three_count


if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        adapters = list(map(int, f.read().splitlines()))

    print("Part 1: ", one_three_differences(adapter_chain(adapters)))
    print("Part 2: ", find_all_combinations(adapters))