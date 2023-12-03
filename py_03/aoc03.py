from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Self

inputfolder = Path(__file__).parent.parent / "inputs"

with open(inputfolder / "input03.txt", "r", encoding="utf-8") as file:
    input_lines = [line.strip() for line in file.readlines() if line]

NUMBER_RE = re.compile(r"(\d+)")


@dataclass
class Number:
    matrix: list[str]
    contents: str
    x_start: int
    x_end: int
    y: int

    def __int__(self) -> int:
        return int(self.contents)

    @property
    def max_x(self):
        return len(self.matrix[0])

    @property
    def max_y(self):
        return len(self.matrix)

    @classmethod
    def from_match(cls, matrix: list[str], match: re.Match, y: int) -> Self:
        """Builds the Number object from the re.Match

        Args:
            matrix (list[str]): the whole input
            match (re.Match): successful match of NUMBER_RE
            y (int): y position in map

        Returns:
            Self: _description_
        """
        return Number(
            contents=match.groups()[0],
            x_start=match.span()[0],
            x_end=match.span()[1],
            y=y,
            matrix=matrix,
        )

    @property
    def adjacent_stars(self) -> list[tuple[int, int]]:
        """List of adjacent star positions

        Returns:
            list[tuple[int, int]]: adjacent star positions (x,y)
        """
        stars: list[tuple(int, int)] = []
        for y in range(max(0, self.y - 1), min(self.max_y, self.y + 2)):
            for x in range(max(0, self.x_start - 1), min(self.max_x, self.x_end + 1)):
                if self.matrix[y][x] == "*":
                    stars.append((x, y))
        return stars

    @property
    def is_partnumber(self) -> bool:
        """Determines if this number is a part number,
        based on if it is adjacent to a symbol

        Returns:
            bool: True if this is a part number
        """
        for y in range(max(0, self.y - 1), min(self.max_y, self.y + 2)):
            for x in range(max(0, self.x_start - 1), min(self.max_x, self.x_end + 1)):
                if self.matrix[y][x] == ".":
                    continue
                if self.matrix[y][x].isdigit():
                    continue
                return True
        return False


def task1():
    numbers: list[Number] = []
    for y, line in enumerate(input_lines):
        for match in re.finditer(
            NUMBER_RE,
            line,
        ):
            number = Number.from_match(matrix=input_lines, match=match, y=y)
            number.is_partnumber
            numbers.append(number)
    return sum(int(number) for number in numbers if number.is_partnumber)


def task2():
    stars: dict[tuple[int, int], list[Number]] = defaultdict(list)
    for y, line in enumerate(input_lines):
        for match in re.finditer(
            NUMBER_RE,
            line,
        ):
            number = Number.from_match(matrix=input_lines, match=match, y=y)
            number.is_partnumber
            for star_pos in number.adjacent_stars:
                stars[star_pos].append(number)
    gears = {key: value for key, value in stars.items() if len(value) == 2}
    gear_ratios = (int(value[0]) * int(value[1]) for value in gears.values())
    return sum(gear_ratios)


print(task1())
print(task2())
