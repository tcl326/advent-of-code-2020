from collections import defaultdict


def get_active_coords(conway_map):
    active_coords = set()
    for i in range(len(conway_map)):
        for j in range(len(conway_map[0])):
            if conway_map[i][j] == "#":
                active_coords.add((i, j, 0))
    return active_coords


def simulate(conway_map, steps=6):
    active_coords = get_active_coords(conway_map)

    for _ in range(steps):
        coord_votes = defaultdict(int)
        next_active_coords = set()
        for coord in active_coords:
            x, y, z = coord
            active_neighbours = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        if i == 0 and j == 0 and k == 0:
                            continue
                        coord_votes[(x + i, y + j, z + k)] += 1
                        if (x + i, y + j, z + k) in active_coords:
                            active_neighbours += 1
            if active_neighbours == 2 or active_neighbours == 3:
                next_active_coords.add(coord)
        for coord, votes in coord_votes.items():
            if coord in active_coords:
                continue
            if votes == 3:
                next_active_coords.add(coord)
        active_coords = next_active_coords

    return len(active_coords)


def get_active_coords_4d(conway_map):
    active_coords = set()
    for i in range(len(conway_map)):
        for j in range(len(conway_map[0])):
            if conway_map[i][j] == "#":
                active_coords.add((i, j, 0, 0))
    return active_coords


def simulate_4d(conway_map, steps=6):
    active_coords = get_active_coords_4d(conway_map)

    for _ in range(steps):
        coord_votes = defaultdict(int)
        next_active_coords = set()
        for coord in active_coords:
            x, y, z, w = coord
            active_neighbours = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if i == 0 and j == 0 and k == 0 and l == 0:
                                continue
                            coord_votes[(x + i, y + j, z + k, w + l)] += 1
                            if (x + i, y + j, z + k, w + l) in active_coords:
                                active_neighbours += 1
            if active_neighbours == 2 or active_neighbours == 3:
                next_active_coords.add(coord)
        for coord, votes in coord_votes.items():
            if coord in active_coords:
                continue
            if votes == 3:
                next_active_coords.add(coord)
        active_coords = next_active_coords

    return len(active_coords)




if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        conway_map = list(map(list, f.read().splitlines()))

    print("Part 1: ", simulate(conway_map, 6))
    print("Part 2: ", simulate_4d(conway_map, 6))