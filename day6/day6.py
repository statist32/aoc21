def get_puzzle_input(filename):
    fishes = {time: 0 for time in range(0, 9)}
    with open(filename, "r") as f:
        for number in f.readlines()[0].strip().split(","):
            fishes[int(number)] += 1
    return fishes


def solve1(fishes, days):
    for _ in range(days):
        for time in range(0, 9):
            fishes[time - 1] = fishes[time]
        babies = fishes.pop(-1)
        fishes[6] += babies
        fishes[8] = babies
    return sum(fishes.values())


if __name__ == "__main__":
    fishes = get_puzzle_input("puzzle_input6.txt")
    result1 = solve1(fishes, 256)
    print(result1)
    fishes = get_puzzle_input("puzzle_input6.txt")
    result2 = solve1(fishes, 256)
    print(result2)
