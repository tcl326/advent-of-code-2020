from typing import List
from collections import Counter


def report_repair(nums: List[int]):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == 2020:
                return nums[i] * nums[j]
    return -1


def report_repair_3(nums: List[int]):
    num_counter = Counter(nums)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            val_of_interest = 2020 - (nums[i] + nums[j])
            if val_of_interest in num_counter:
                if nums[i] == val_of_interest or nums[j] == val_of_interest:
                    if num_counter[val_of_interest] > 1:
                        return nums[i] * nums[j] * val_of_interest
                    else:
                        continue
                return nums[i] * nums[j] * val_of_interest
    return -1



if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    nums = []
    with open(input_file) as f:
        nums = list(map(int, f.readlines()))

    print("Part 1: ", report_repair(nums))
    print("Part 2: ", report_repair_3(nums))