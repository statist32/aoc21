def get_puzzle_input(filename):
    with open(filename, "r") as f:
        return [int(line) for line in f.readlines()]


def task1(puzzle_input):
    return sum(
        [
            next_value > current_value
            for current_value, next_value in zip(
                puzzle_input[:-1], puzzle_input[1:]
            )
        ]
    )


def task2(puzzle_input):
    sums = [
        sum(value)
        for value in zip(
            puzzle_input[:-2], puzzle_input[1:-1], puzzle_input[2:]
        )
    ]
    return sum([next > current for current, next in zip(sums[:-1], sums[1:])])


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("puzzle_input1.txt")
    result1 = task1(puzzle_input)
    print(result1)
    result2 = task2(puzzle_input)
    print(result2)
