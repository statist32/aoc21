import sys


class BingoSheet:
    def __init__(self, sheet):
        self.sheet = sheet
        self.is_ongoing = True

    def __repr__(self):
        padding = 4
        ret = ""
        for row in self.sheet:
            for entry in row:
                key = list(entry.keys())[0]
                if entry[key]:
                    ret += f"*{key}".rjust(padding)
                else:
                    ret += f"{key}".rjust(padding)
            ret += "\n"
        return ret[1:]

    def mark_number(self, drawn_number):
        for row in self.sheet:
            for entry in row:
                if drawn_number in entry:
                    entry[drawn_number] = True
                    return True
        return False

    def check_bingo(self):
        for row in self.sheet:
            if len(row) == sum([list(entry.values())[0] for entry in row]):
                self.is_ongoing = False
                return True
        row_amount = len(self.sheet)
        for i in range(row_amount):
            if len(row) == sum(
                [list(entry[i].values())[0] for entry in self.sheet]
            ):
                self.is_ongoing = False
                return True
        return False

    def sum_of_all_unmarked_numbers(self):
        return sum(
            [
                sum(
                    [
                        list(entry.keys())[0]
                        for entry in row
                        if not list(entry.values())[0]
                    ]
                )
                for row in self.sheet
            ]
        )


def get_puzzle_input(filename):
    with open(filename, "r") as f:
        puzzle_input = [line.strip() for line in f.readlines()]
    drawn_numbers = [int(number) for number in puzzle_input[0].split(",")]
    sheets = []
    sheet = []
    for line in puzzle_input[2:]:
        if line:
            sheet.append(
                [{int(number): False} for number in line.split(" ") if number]
            )
        else:
            sheets.append(BingoSheet(sheet))
            sheet = []
    sheets.append(BingoSheet(sheet))

    return drawn_numbers, sheets


def solve1(drawn_numbers, sheets):
    for drawn_number in drawn_numbers:
        for sheet in sheets:
            if sheet.mark_number(drawn_number) and sheet.check_bingo():
                return drawn_number * sheet.sum_of_all_unmarked_numbers()


def solve2(drawn_numbers, sheets):
    for drawn_number in drawn_numbers:
        for sheet in sheets:
            if sheet.mark_number(drawn_number) and sheet.check_bingo():
                if sum([sheet.is_ongoing for sheet in sheets]) == 0:
                    return drawn_number * sheet.sum_of_all_unmarked_numbers()


if __name__ == "__main__":
    drawn_numbers, sheets = get_puzzle_input("puzzle_input4.txt")
    result1 = solve1(drawn_numbers, sheets)
    print(result1)
    result2 = solve2(drawn_numbers, sheets)
    print(result2)
