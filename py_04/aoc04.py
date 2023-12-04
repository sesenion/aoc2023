from dataclasses import dataclass
from pathlib import Path
import re
from typing import Self

inputfolder = Path(__file__).parent.parent / "inputs"

with open(inputfolder / "input04.txt", "r", encoding="utf-8") as file:
    input_lines = [line.strip() for line in file.readlines() if line]


LINEPATTERN = re.compile(r"^Card\s*(\d+):([\d\s]+)\|([\d\s]+)$")


@dataclass
class Card:
    id: int
    winning_numbers: set[int]
    my_numbers: set[int]

    @classmethod
    def from_line(cls, line: str) -> Self:
        """create Card from input line

        Args:
            line (str): input line

        Returns:
            Self: Card
        """
        match = re.match(LINEPATTERN, line)
        cardnumber, winning_numbers, my_numbers = match.groups()
        cardnumber = int(cardnumber)
        winning_numbers = {int(number) for number in winning_numbers.strip().split()}
        my_numbers = {int(number) for number in my_numbers.strip().split()}
        return cls(cardnumber, winning_numbers, my_numbers)

    @property
    def matching_numbers(self) -> int:
        """Number of matching numbers

        Returns:
            int: number of matching numbers
        """
        return len(self.winning_numbers.intersection(self.my_numbers))

    @property
    def score(self) -> int:
        """Score for Task 1

        Returns:
            int: score
        """
        if not self.matching_numbers:
            return 0
        return 2 ** (self.matching_numbers - 1)


@dataclass
class CardStack:
    card: Card
    count: int


def task1():
    return sum(Card.from_line(line).score for line in input_lines)


def task2():
    cards = (Card.from_line(line) for line in input_lines)
    cardstacks = {card.id: CardStack(card, 1) for card in cards}
    for id, cardstack in cardstacks.items():
        factor = cardstack.count
        for i in range(cardstack.card.matching_numbers):
            target_id = id + i + 1
            if target_id > len(cardstacks):
                continue
            cardstacks[target_id].count += factor
    return sum(cardstack.count for cardstack in cardstacks.values())


print(task1())
print(task2())
