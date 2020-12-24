def parse(lines):
    instructions = []
    for line in lines:
        i = 0
        instruction = []
        while i in range(len(line)):
            if line[i] == 's' or line[i] == 'n':
                instruction.append(line[i: i + 2])
                i += 2
            else:
                instruction.append(line[i])
                i += 1
        instructions.append(instruction)
    return instructions


direction_map = {
    "e": (0, 1),
    "w": (0, -1),
    "ne": (-1, 1),
    "nw": (-1, 0),
    "se": (1, 0),
    "sw": (1, -1),
}


def flip_board(instructions):
    black_tiles = set()
    for instruction in instructions:
        i, j = 0, 0
        for inst in instruction:
            di, dj = direction_map[inst]
            i += di
            j += dj
        if (i, j) in black_tiles:
            black_tiles.remove((i, j))
        else:
            black_tiles.add((i, j))
    return black_tiles


def simulate(black_tiles, days=100):
    for _ in range(days):
        new_black_tiles = set()
        white_tiles_of_interest = set()
        for b_i, b_j in black_tiles:
            b_count = 0
            for di, dj in direction_map.values():
                n_i, n_j = b_i + di, b_j + dj
                if (n_i, n_j) in black_tiles:
                    b_count += 1
                else:
                    white_tiles_of_interest.add((n_i, n_j))
            if b_count > 0 and b_count <= 2:
                new_black_tiles.add((b_i, b_j))

        for w_i, w_j in white_tiles_of_interest:
            b_count = 0
            for di, dj in direction_map.values():
                n_i, n_j = w_i + di, w_j + dj
                if (n_i, n_j) in black_tiles:
                    b_count += 1
            if b_count == 2:
                new_black_tiles.add((w_i, w_j))
        black_tiles = new_black_tiles

    return black_tiles




if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        instructions = parse(f.read().splitlines())

    black_tiles = flip_board(instructions)
    print("Part 1: ", len(black_tiles))
    print("Part 2: ", len(simulate(black_tiles, 100)))