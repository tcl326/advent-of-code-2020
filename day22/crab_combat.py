from collections import deque


def parse(lines):
    p1cards = []
    p2cards = []
    player = 1

    for line in lines:
        if not line:
            player = 2
            continue
        if player == 1 and line.isdigit():
            p1cards.append(int(line))
        if player == 2 and line.isdigit():
            p2cards.append(int(line))
    return p1cards, p2cards


def get_score(cards):
    res = 0
    for i, c in enumerate(reversed(cards)):
        res += (i + 1) * c
    return res


def part1(p1cards, p2cards):
    p1cards = deque(p1cards)
    p2cards = deque(p2cards)

    while p1cards and p2cards:
        p1, p2 = p1cards.popleft(), p2cards.popleft()
        if p2 > p1:
            p2cards.append(p2)
            p2cards.append(p1)
        else:
            p1cards.append(p1)
            p1cards.append(p2)

    print(p1cards, p2cards)

    score = get_score(p1cards or p2cards)
    return score


def part2(p1cards, p2cards):
    og_c1 = p1cards
    og_c2 = p2cards
    p1cards = deque(p1cards)
    p2cards = deque(p2cards)

    def subgame(cards1, cards2):
        seen = set()
        while cards1 and cards2:
            hand = (tuple(cards1), tuple(cards2))
            if hand in seen:
                return 1, cards1
            else:
                seen.add(hand)
            c1, c2 = cards1.popleft(), cards2.popleft()
            p1wins = False
            if c1 <= len(cards1) and c2 <= len(cards2):
                p1wins, _ = subgame(deque(list(cards1)[:c1]), deque(list(cards2)[:c2]))
            else:
                p1wins = c1 > c2
            if p1wins:
                cards1.append(c1)
                cards1.append(c2)
            else:
                cards2.append(c2)
                cards2.append(c1)
        print(cards1, cards2)
        return p1wins, cards1 or cards2

    p1wins, winner_card = subgame(p1cards, p2cards)
    print(winner_card)
    return get_score(winner_card)



if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        p1cards, p2cards = parse(f.read().splitlines())

    print("Part 1: ", part1(p1cards, p2cards))
    print("Part 2: ", part2(p1cards, p2cards))