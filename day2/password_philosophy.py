from typing import List, Tuple
from collections import Counter


def num_valid(lines: List[Tuple[int, int, str, str]]):
    res = 0
    for low, high, letter, password in lines:
        count = password.count(letter)
        if count >= low and count <= high:
            res += 1
    return res


def num_valid_real_policy(lines: List[Tuple[int, int, str, str]]):
    res = 0
    for low, high, letter, password in lines:
        res += (password[low - 1] == letter) ^ (password[high - 1] == letter)
    return res



def parse_line(line: str):
    min_max, letter, password = line.split(" ")
    low, high = map(int, min_max.split("-"))
    letter = letter[:-1]
    return low, high, letter, password


if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        lines = list(map(parse_line, f.readlines()))

    print("Part 1: ", num_valid(lines))
    print("Part 2: ", num_valid_real_policy(lines))