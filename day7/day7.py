import statistics


def get_puzzle_input(filename):
    with open(filename, "r") as f:
        return [
            int(position) for position in f.readlines()[0].strip().split(",")
        ]


def solve1(puzzle_input):
    median = statistics.median(puzzle_input)
    return sum([abs(position - median) for position in puzzle_input])


def solve2(puzzle_input):
    # it has to be the mean +-1 due to rounding
    mean = round(statistics.mean(puzzle_input)) - 1
    print(mean)
    return sum(
        [sum(range(abs(position - mean) + 1)) for position in puzzle_input]
    )


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("puzzle_input7.txt")
    result1 = solve1(puzzle_input)
    print(result1)
    result2 = solve2(puzzle_input)
    print(result2)
