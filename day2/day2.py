from collections import defaultdict


def get_puzzle_input(filename):
    with open(filename, "r") as f:
        return [line for line in f.readlines()]


def task1(puzzle_input):
    sums = defaultdict(int)
    for command in puzzle_input:
        direction, amount = command.split(" ")
        sums[direction] += int(amount)
    depth = sums["down"] - sums["up"]
    return sums["forward"] * depth


def task2(puzzle_input):
    aim = depth = horizontal_position = 0
    for command in puzzle_input:
        direction, amount = command.split(" ")
        amount = int(amount)
        if direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount
        else:
            horizontal_position += amount
            depth += aim * amount
    return horizontal_position * depth


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("puzzle_input2.txt")
    result1 = task1(puzzle_input)
    print(result1)
    result2 = task2(puzzle_input)
    print(result2)
