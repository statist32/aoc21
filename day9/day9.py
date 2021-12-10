def get_puzzle_input(filename):
    with open(filename, "r") as f:
        return [[{"number": int(number), "visited": False} for number in line.strip()] for line in f.readlines()]


def find_lowest_points(puzzle_input):
    lowest_points = {}
    highest_x = len(puzzle_input[0])
    highest_y = len(puzzle_input)

    for x in range(highest_x):
        for y in range(highest_y):
            element = puzzle_input[y][x]["number"]
            if x - 1 >= 0 and element >= puzzle_input[y][x-1]["number"]:
                continue
            if x + 1 < highest_x and element >= puzzle_input[y][x+1]["number"]:
                continue
            if y - 1 >= 0 and element >= puzzle_input[y-1][x]["number"]:
                continue
            if y + 1 < highest_y and element >= puzzle_input[y+1][x]["number"]:
                continue
            lowest_points[(x, y)] = element
    return lowest_points


def solve1(puzzle_input):
    return sum([point + 1 for point in find_lowest_points(puzzle_input).values()])


def find_higher_neighbors(puzzle_input, position):
    highest_x = len(puzzle_input[0])
    highest_y = len(puzzle_input)
    x, y = position
    element = puzzle_input[y][x]["number"]
    s = 1
    if x - 1 >= 0 and element < puzzle_input[y][x-1]["number"] < 9 and not puzzle_input[y][x-1]["visited"]:
        puzzle_input[y][x-1]["visited"] = True
        s += find_higher_neighbors(puzzle_input, (x-1, y))
    if x + 1 < highest_x and element < puzzle_input[y][x+1]["number"] < 9 and not puzzle_input[y][x+1]["visited"]:
        puzzle_input[y][x+1]["visited"] = True
        s += find_higher_neighbors(puzzle_input, (x+1, y))
    if y - 1 >= 0 and element < puzzle_input[y-1][x]["number"] < 9 and not puzzle_input[y-1][x]["visited"]:
        puzzle_input[y-1][x]["visited"] = True
        s += find_higher_neighbors(puzzle_input, (x, y-1))
    if y + 1 < highest_y and element < puzzle_input[y+1][x]["number"] < 9 and not puzzle_input[y+1][x]["visited"]:
        puzzle_input[y+1][x]["visited"] = True
        s += find_higher_neighbors(puzzle_input, (x, y+1))
    return s


def solve2(puzzle_input):
    lowest_points = find_lowest_points(puzzle_input)
    basins = []
    for x, y in lowest_points.keys():
        basins.append(find_higher_neighbors(puzzle_input, (x, y)))
    a, b, c = sorted(basins)[-3:]
    return a*b*c


if __name__ == "__main__":
    puzzle_input = get_puzzle_input("puzzle_input.txt")
    result1 = solve1(puzzle_input)
    print(result1)
    result2 = solve2(puzzle_input)
    print(result2)
