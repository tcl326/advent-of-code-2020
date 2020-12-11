from typing import List, Tuple
from collections import Counter, defaultdict, deque
import copy

ADJACENCY = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, 1), (0, -1)]


def occupied_adjacent_seats(i, j, seating):
    res = 0
    for di, dj in ADJACENCY:
        ni, nj = di + i, dj + j
        if ni < 0 or ni >= len(seating) or nj < 0 or nj >= len(seating[0]):
            continue
        if seating[ni][nj] == "#":
            res += 1
    return res


def final_occupancy(seating):
    while True:
        next_seating = [["" for _ in seating[0]] for _ in seating]
        for i in range(len(seating)):
            for j in range(len(seating[i])):
                occupied_seats = occupied_adjacent_seats(i, j, seating)
                if seating[i][j] == "L" and occupied_seats == 0:
                    next_seating[i][j] = "#"
                elif seating[i][j] == "#" and occupied_seats >= 4:
                    next_seating[i][j] = "L"
                else:
                    next_seating[i][j] = seating[i][j]
        if seating == next_seating:
            break
        seating = next_seating

    res = 0
    for i in range(len(seating)):
        for j in range(len(seating[i])):
            if seating[i][j] == "#":
                res += 1
    return res


def occupied_visible_seats(i, j, seating):
    res = 0
    for di, dj in ADJACENCY:
        ni, nj = i + di, j + dj
        while ni >= 0 and ni < len(seating) and nj >= 0 and nj < len(seating[0]):
            if seating[ni][nj] == "#":
                res += 1
                break
            if seating[ni][nj] == "L":
                break
            ni += di
            nj += dj
    return res

def final_occupancy_two(seating):
    while True:
        next_seating = [["" for _ in seating[0]] for _ in seating]
        for i in range(len(seating)):
            for j in range(len(seating[i])):
                occupied_seats = occupied_visible_seats(i, j, seating)
                if seating[i][j] == "L" and occupied_seats == 0:
                    next_seating[i][j] = "#"
                elif seating[i][j] == "#" and occupied_seats >= 5:
                    next_seating[i][j] = "L"
                else:
                    next_seating[i][j] = seating[i][j]
        if seating == next_seating:
            break
        seating = next_seating

    res = 0
    for i in range(len(seating)):
        for j in range(len(seating[i])):
            if seating[i][j] == "#":
                res += 1
    return res



if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        seat_map = list(map(list, f.read().splitlines()))

    print("Part 1: ", final_occupancy(seat_map))
    print("Part 2: ", final_occupancy_two(seat_map))