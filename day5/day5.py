from collections import defaultdict
from itertools import product


def get_puzzle_input(filename):
    with open(filename, "r") as f:
        return [
            [
                [int(direction) for direction in point.split(",")]
                for point in line.strip().split(" -> ")
            ]
            for line in f.readlines()
        ]


def solve1(puzzle_input):
    map = defaultdict(int)
    filtered_input = [
        line
        for line in puzzle_input
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]
    ]
    for start_position, end_position in filtered_input:
        a = sorted([start_position[0], end_position[0]])
        b = sorted([start_position[1], end_position[1]])
        for entry in product(
            range(a[0], a[1] + 1),
            range(b[0], b[1] + 1),
        ):
            map[str(entry)] += 1
    return sum([1 for value in map.values() if value >= 2])


def solve2(puzzle_input):
    map = defaultdict(int)
    for start_position, end_position in puzzle_input:
        if start_position[0] == end_position[0]:
            y_direction = 1 if start_position[1] < end_position[1] else -1
            lines = product(
                [start_position[0]],
                range(
                    start_position[1],
                    end_position[1] + y_direction,
                    y_direction,
                ),
            )
        elif start_position[1] == end_position[1]:
            x_direction = 1 if start_position[0] < end_position[0] else -1
            lines = product(
                range(
                    start_position[0],
                    end_position[0] + x_direction,
                    x_direction,
                ),
                [start_position[1]],
            )

        elif abs(start_position[0] - end_position[0]) == abs(
            start_position[1] - end_position[1]
        ):
            x_direction = 1 if start_position[0] < end_position[0] else -1
            y_direction = 1 if start_position[1] < end_position[1] else -1

            x_axis = range(
                start_position[0], end_position[0] + x_direction, x_direction
            )
            y_axis = range(
                start_position[1], end_position[1] + y_direction, y_direction
            )
            lines = zip(x_axis, y_axis)
        for entry in lines:
            map[str(entry)] += 1

       return sum([1 for value in map.values() if value >= 2])


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("puzzle_input5.txt")
    result1 = solve1(puzzle_input)
    print(result1)
    result2 = solve2(puzzle_input)
    print(result2)
