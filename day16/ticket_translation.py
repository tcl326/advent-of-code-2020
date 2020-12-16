from collections import defaultdict
import heapq


def parse_valid_values(line):
    field, value = line.split(": ")
    field = field.replace(" ", "_")
    ranges = value.split(" or ")
    ranges = [list(map(int, r.split("-"))) for r in ranges]
    return field, ranges

def parse_ticket(line):
    return list(map(int, line.split(",")))


def parse_tickets(lines):
    valid_values = {}
    your_ticket = []
    nearby_tickets = []

    active = 'valid_values'
    for line in lines:
        if not line:
            continue
        if line == "your ticket:":
            active = "your_ticket"
            continue
        if line == "nearby tickets:":
            active = "nearby_tickets"
            continue
        if active == "valid_values":
            field, ranges = parse_valid_values(line)
            valid_values[field] = ranges
        if active == "your_ticket":
            your_ticket = parse_ticket(line)
        if active == "nearby_tickets":
            nearby_tickets.append(parse_ticket(line))
    return valid_values, your_ticket, nearby_tickets



def find_invalid(valid_values, nearby_tickets):
    valid_set = set()
    for _, ranges in valid_values.items():
        for r in ranges:
            for i in range(r[0], r[1] + 1):
                valid_set.add(i)
    res = 0
    valid_tickets = []
    for ticket in nearby_tickets:
        for val in ticket:
            if val not in valid_set:
                res += val
                break
        else:
            valid_tickets.append(ticket)
    return res, valid_tickets


def find_satisfy(valid_values, valid_tickets):
    valid_values_set = defaultdict(set)
    for key, ranges in valid_values.items():
        for r in ranges:
            for i in range(r[0], r[1] + 1):
                valid_values_set[key].add(i)

    satisfied_fields = [set(valid_values.keys()) for _ in range(len(valid_tickets[0]))]
    for ticket in valid_tickets:
        for i, val in enumerate(ticket):
            for key, ranges in valid_values_set.items():
                if val not in ranges:
                    satisfied_fields[i].remove(key)
    return satisfied_fields


def departure_values(valid_values, valid_tickets, your_ticket):
    satisfied_fields = find_satisfy(valid_values, valid_tickets)
    heap = [(len(fields), fields, col) for col, fields in enumerate(satisfied_fields)]
    heapq.heapify(heap)

    assignment = [-1 for _ in range(len(your_ticket))]
    seen = set()
    while heap:
        _, fields, col = heapq.heappop(heap)
        if len(fields) == 1:
            field = fields.pop()
            seen.add(field)
            assignment[col] = field
        else:
            for field in seen:
                fields.remove(field)
            heapq.heappush(heap, (len(fields), fields, col))

    res = 1
    for field, val in zip(assignment, your_ticket):
        if "departure" in field:
            res *= val
    return res


if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        valid_values, your_ticket, nearby_tickets = parse_tickets(f.read().splitlines())

    part_1_res, valid_tickets = find_invalid(valid_values, nearby_tickets)
    print("Part 1: ", part_1_res)
    print("Part 2: ", departure_values(valid_values, valid_tickets, your_ticket))