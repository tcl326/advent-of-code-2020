import heapq

def parse(lines):
    ingredients = []
    allergents = []

    for line in lines:
        ing, alr = line.rstrip(")").split(" (contains ")
        ingredients.append(ing.split(" "))
        allergents.append(alr.split(", "))
    return ingredients, allergents


def part1(ingredients, allergents):
    alr_to_ing = {}
    for i, alr in enumerate(allergents):
        for a in alr:
            if a not in alr_to_ing:
                alr_to_ing[a] = set(ingredients[i])
            else:
                alr_to_ing[a] &= set(ingredients[i])

    heap = [(len(val), 0, key, val) for key, val in alr_to_ing.items()]
    heapq.heapify(heap)

    matched_ingr_alr = {}
    while heap:
        _, visit, alr, ingr = heapq.heappop(heap)
        if len(ingr) <= 1:
            matched_ingr_alr[ingr.pop()] = alr
        else:
            new_ingr = set()
            for i in ingr:
                if i not in matched_ingr_alr:
                    new_ingr.add(i)
            heapq.heappush(heap, (len(new_ingr), visit + 1, alr, new_ingr))
    res = 0
    for ingr in ingredients:
        for i in ingr:
            if i not in matched_ingr_alr:
                res += 1
    return res, matched_ingr_alr


def part2(matched_ingr_alr):
    ingr = list(matched_ingr_alr.keys())
    alr = list(matched_ingr_alr.values())

    canonical = [i for  _, i in sorted(zip(alr, ingr))]

    return ",".join(canonical)


if __name__ == "__main__":
    input_file = input("Enter your Input File path: ")
    with open(input_file) as f:
        ingredients, allergents = parse(f.read().splitlines())

    p1_res, matched_ingr_alr = part1(ingredients, allergents)
    print("Part 1: ", p1_res)
    print("Part 2: ", part2(matched_ingr_alr))