from typing import List, Tuple


def tree_encounters(local_geology: List[str], right = 3, down = 1):
    dx = right
    dy = down
    curr_x = 0
    curr_y = 0

    m = len(local_geology)
    n = len(local_geology[0])

    res = 0

    while curr_y < m:
        curr_x = (curr_x + dx) % n
        curr_y = curr_y + dy
        if curr_y >= m:
            break
        res += local_geology[curr_y][curr_x] == '#'

    return res

def multiple_tree_encounters(local_geology, slopes):
    res = 1
    for right, down in slopes:
        res *= tree_encounters(local_geology, right, down)
    return res


if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        local_geology = list(map(list, f.read().splitlines()))

    print("Part 1: ", tree_encounters(local_geology))
    print("Part 2: ", multiple_tree_encounters(local_geology, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))