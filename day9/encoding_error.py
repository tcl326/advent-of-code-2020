from typing import List, Tuple
from collections import Counter, defaultdict, deque


def find_weakness(encodings, desired_sum):
    queue = deque(encodings[:2])
    curr_sum = sum(queue)
    for n in encodings[2:]:
        queue.append(n)
        curr_sum += n
        while curr_sum > desired_sum and len(queue) > 1:
            v = queue.popleft()
            curr_sum -= v
        if curr_sum == desired_sum:
            res_queu = sorted(list(queue))
            return res_queu[0] + res_queu[-1]
    return -1


def first_error(encodings, preamble_num=25):
    queue = deque(encodings[:preamble_num])
    curr_set = set(queue)
    for n in encodings[preamble_num:]:
        for q in queue:
            if n - q in curr_set:
                break
        else:
            return n
        v = queue.popleft()
        curr_set.remove(v)

        queue.append(n)
        curr_set.add(n)
    return -1


if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        encodings = list(map(int, f.read().splitlines()))

    part_1_res = first_error(encodings, 25)
    print(part_1_res)
    print("Part 1: ", part_1_res)
    print("Part 2: ", find_weakness(encodings, part_1_res))