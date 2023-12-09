from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import re
from typing import Self

inputfolder = Path(__file__).parent.parent / "inputs"

with open(inputfolder / "input07.txt", "r", encoding="utf-8") as file:
    input_lines = [line.strip() for line in file.readlines() if line]


class Hand:
    def __init__(self, hand: str, j_is_joker: bool = False):
        """A Hand object able to determine its hand ranking

        Args:
            hand (str): Hand as String of 5 Card Symbols (2-9, T, J, Q, K, A)
            j_is_joker (bool, optional): J is interpreted as joker, reducing
                its value as a card, but increasing the hand value.
                Defaults to False.
        """
        self.hand = [self.card_value(card, j_is_joker) for card in hand]
        self.set = set(self.hand)
        try:
            self.set.remove(1)  # Remove Jokers from the set of cards
        except KeyError:
            pass

    @staticmethod
    def card_value(card: str, j_is_joker: bool = False) -> int:
        """Returns the numerical value of a card

        Args:
            card (str): Card Symbol (2-9, T, J, Q, K, A)

        Returns:
            int: value (2-14)
        """
        if card.isdigit():
            return int(card)
        return {
            "T": 10,
            "J": 1 if j_is_joker else 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }[card]

    def __repr__(self):
        return f"Hand <{self.hand}, {self.hand_value}>"

    def __eq__(self, other: Self) -> bool:
        return self.hand == other.hand

    def __gt__(self, other: Self) -> bool:
        if self == other:
            return False
        if self.hand_value > other.hand_value:
            return True
        if self.hand_value < other.hand_value:
            return False
        for card, other_card in zip(self.hand, other.hand):
            if card > other_card:
                return True
            if other_card < card:
                return False
        return False

    def __le__(self, other: Self) -> bool:
        return not (self > other)

    @property
    def hand_value(self) -> int:
        """Determines the value of the hand, not taking into account the card values

        Returns:
            int: Hand Value (6-0) for (Five in a Row, Four in a Row, Full House,
                Three in a Row, Two Pairs, one Pair, High Card)
        """
        hand_without_jokers = [card for card in self.hand if card != 1]
        jokers = 5 - len(hand_without_jokers)
        counts = sorted([hand_without_jokers.count(card) for card in self.set])
        if not counts:
            return 6
        counts[-1] += jokers
        counts = sorted(counts)
        match counts:
            case [5]:
                return 6
            case [1, 4]:
                return 5
            case [2, 3]:
                return 4
            case [1, 1, 3]:
                return 3
            case [1, 2, 2]:
                return 2
            case [1, 1, 1, 2]:
                return 1
            case _:
                return 0


def task1():
    splitlines = (line.split() for line in input_lines)
    games = [(Hand(line[0]), int(line[1])) for line in splitlines]
    sorted_games = sorted(games, key=lambda x: (x[0].hand_value, x[0].hand))
    # sorted_games = sorted(games, key=lambda x: x[0]) # not working, something wrong with comparing Hands
    winnings = 0
    for i, game in enumerate(sorted_games):
        winnings += (i + 1) * game[1]
    return winnings


def task2():
    splitlines = (line.split() for line in input_lines)
    games = [(Hand(line[0], j_is_joker=True), int(line[1])) for line in splitlines]
    sorted_games = sorted(games, key=lambda x: (x[0].hand_value, x[0].hand))
    winnings = 0
    for i, game in enumerate(sorted_games):
        winnings += (i + 1) * game[1]
    return winnings


print(task1())
print(task2())
