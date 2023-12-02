from dataclasses import dataclass
from pathlib import Path
import re
from typing import Self

inputfolder = Path(__file__).parent.parent / "inputs"

with open(inputfolder / "input02.txt", "r", encoding="utf-8") as file:
    input_lines = [line.strip() for line in file.readlines()]

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


@dataclass
class Draw:
    red: int
    green: int
    blue: int

    @classmethod
    def parse(cls, line: str) -> Self:
        """Parses a draw string from the input line into a Draw object

        Args:
            line (str): Draw string from input line

        Returns:
            Self: Draw Object
        """
        red = green = blue = 0
        if red_match := re.search(r"(\d+)\sred", line):
            red = int(red_match.groups()[0])
        if green_match := re.search(r"(\d+)\sgreen", line):
            green = int(green_match.groups()[0])
        if blue_match := re.search(r"(\d+)\sblue", line):
            blue = int(blue_match.groups()[0])
        return cls(red, green, blue)

    @property
    def possible(self) -> bool:
        """Shows if this draw is possible with the maximum available
        clubes

        Returns:
            bool: possible draw
        """
        if self.red > MAX_RED:
            return False
        if self.green > MAX_GREEN:
            return False
        if self.blue > MAX_BLUE:
            return False
        return True


@dataclass
class Game:
    id: int
    draws: list[Draw]

    @classmethod
    def parse(cls, line: str) -> Self:
        """Parses a game line into a Game object

        Args:
            line (str): Line from input

        Returns:
            Self: Game object
        """
        game, draws = line.split(":")
        id = int(re.match(r"Game\s(\d+)", game).groups()[0])
        draws = [Draw.parse(fragment) for fragment in draws.split(";")]
        return Game(id, draws)

    @property
    def possible(self):
        """Shows if game is possible within the maximum avaiable cubes

        Returns:
            bool: shows if the game is possible
        """
        return all(draw.possible for draw in self.draws)

    def get_fewest_required(self) -> tuple[int, int, int]:
        """Gets the fewest required cubes to make this game possible

        Returns:
            tuple[int, int, int]: minimum red, green, blue required for the game
        """
        red = max(draw.red for draw in self.draws)
        green = max(draw.green for draw in self.draws)
        blue = max(draw.blue for draw in self.draws)
        return (red, green, blue)

    @property
    def power(self) -> int:
        """Returns the power for task2, which is the product
        of the minimum required cubes for each color

        Returns:
            int: power (Product of required red, green and blue cubes)
        """
        red, green, blue = self.get_fewest_required()
        return red * green * blue


def task1():
    games = (Game.parse(line) for line in input_lines)
    games = (game for game in games if game.possible)
    return sum(game.id for game in games)


def task2():
    games = (Game.parse(line) for line in input_lines)
    return sum(game.power for game in games)


print(task1())
print(task2())
