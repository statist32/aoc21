from collections import defaultdict


def get_puzzle_input(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


def task1(puzzle_input):
    counter = defaultdict(int)
    input_amount = len(puzzle_input)
    bit_amount = len(puzzle_input[0])
    gamma = 0
    for number in puzzle_input:
        for index, bit in enumerate(number):
            counter[index] += int(bit)
    for index, amount in counter.items():
        if amount > input_amount / 2:
            gamma += 2 ** (bit_amount - 1 - index)
    epsilon = 2 ** bit_amount - 1 - gamma
    return epsilon * gamma


def task2(puzzle_input):
    bit_amount = len(puzzle_input[0])
    oxygen = co2 = ""
    data = puzzle_input
    for bit in range(bit_amount):
        counter = 0
        data = [pi for pi in data if pi.startswith(oxygen)]
        for number in data:
            counter += int(number[bit])
        oxygen += "1" if counter >= len(data) - counter else "0"
        if len(data) == 1:
            oxygen = data[0]
            break

    data = puzzle_input
    for bit in range(bit_amount):
        counter = 0
        data = [pi for pi in data if pi.startswith(co2)]
        for number in data:
            counter += int(number[bit])
        co2 += "1" if counter < len(data) - counter else "0"
        if len(data) == 1:
            co2 = data[0]
            break
    return int(oxygen, 2) * int(co2, 2)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("puzzle_input3.txt")
    result1 = task1(puzzle_input)
    print(result1)
    result2 = task2(puzzle_input)
    print(result2)
