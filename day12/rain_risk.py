from typing import List, Tuple
from collections import Counter, defaultdict, deque
import copy

HEADINGS = ["E", "S", "W", "N"]

def _move(inst, curr_x, curr_y):
    if inst[0] == "N":
        curr_y += int(inst[1:])
    elif inst[0] == "S":
        curr_y -= int(inst[1:])
    elif inst[0] == "E":
        curr_x += int(inst[1:])
    elif inst[0] == "W":
        curr_x -= int(inst[1:])
    return curr_x, curr_y


def travel(directions):
    curr_x, curr_y = 0, 0
    curr_dir = "E"
    for inst in directions:
        if inst[0] == "L":
            curr_dir = HEADINGS[(HEADINGS.index(curr_dir) - int(inst[1:]) // 90) % len(HEADINGS)]
        elif inst[0] == "R":
            curr_dir = HEADINGS[(HEADINGS.index(curr_dir) + int(inst[1:]) // 90) % len(HEADINGS)]
        elif inst[0] == "F":
            curr_x, curr_y = _move(curr_dir + inst[1:], curr_x, curr_y)
        else:
            curr_x, curr_y = _move(inst, curr_x, curr_y)

    return abs(curr_x) + abs(curr_y)


def _to_waypoint(move, waypoint_dir, multiple):
    for d, v in waypoint_dir.items():
        move[d] += v * multiple
    return move, waypoint_dir


def way_point_travel(directions):
    move = {"E": 0, "S": 0, "W": 0, "N": 0}
    waypoint_dir = {"E": 10, "S": 0, "W": 0, "N": 1}

    for inst in directions:
        if inst[0] == "L":
            waypoint_dir = {HEADINGS[(HEADINGS.index(direction) - int(inst[1:]) // 90) % len(HEADINGS)]: val for direction, val in waypoint_dir.items()}
        elif inst[0] == "R":
            waypoint_dir = {HEADINGS[(HEADINGS.index(direction) + int(inst[1:]) // 90) % len(HEADINGS)]: val for direction, val in waypoint_dir.items()}
        elif inst[0] == "F":
            move, waypoint_dir = _to_waypoint(move, waypoint_dir, int(inst[1:]))
        else:
            waypoint_dir[inst[0]] += int(inst[1:])

    return abs(move["N"] - move["S"]) + abs(move["W"] - move["E"])


if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        directions = f.read().splitlines()

    print("Part 1: ", travel(directions))
    print("Part 2: ", way_point_travel(directions))