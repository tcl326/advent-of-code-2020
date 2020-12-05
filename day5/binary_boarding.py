from typing import List, Tuple


def max_seat_id(seats):
    max_id = -float('inf')
    for seat in seats:
        max_id = max(get_seat_id(seat), max_id)
    return max_id


def get_seat_id(seats):
    rows = int("".join(list(map(lambda x: str(int(x == "B")), seats[:7]))), 2)
    cols = int("".join(list(map(lambda x: str(int(x == "R")), seats[7:]))), 2)
    return rows * 8 + cols



def find_missing_seat(seats):
    seat_ids = sorted([get_seat_id(seat) for seat in seats])
    for idx in range(1, len(seat_ids)):
        if seat_ids[idx] - seat_ids[idx - 1] > 1:
            return seat_ids[idx] - 1
    return None



if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        seats = list(f.read().splitlines())

    print("Part 1: ", max_seat_id(seats))
    print("Part 2: ", find_missing_seat(seats))