from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import re
from typing import Self

inputfolder = Path(__file__).parent.parent / "inputs"

with open(inputfolder / "input05.txt", "r", encoding="utf-8") as file:
    input_lines = [line.strip() for line in file.readlines() if line]

SEEDS_PATTERN = re.compile(r"^seeds: (.*)$")
MAP_START_PATTERN = re.compile(r"^(\w+)-to-(\w+) map:$")
RANGE_PATTERN = re.compile(r"^(\d+)\s+(\d+)\s+(\d+)$")


class Entity(Enum):
    Seed = "seed"
    Soil = "soil"
    Fertilizer = "fertilizer"
    Water = "water"
    Light = "light"
    Temperature = "temperature"
    Humidity = "humidity"
    Location = "location"


@dataclass(frozen=True)
class Range:
    start: int
    length: int
    target: int

    def in_range(self, number: int) -> bool:
        return number >= self.start and number < self.start + self.length

    def translate(self, number: int) -> int:
        return number - self.start + self.target


@dataclass
class Map:
    source: Entity
    target: Entity
    ranges: list[Range]

    def add_range(self, target_start: int, source_start: int, range_length: int):
        self.ranges.append(Range(source_start, range_length, target_start))

    def translate(self, number: int) -> int:
        for range in self.ranges:
            if range.in_range(number):
                return range.translate(number)
        return number


def new_map(assignment: str) -> Map:
    source, to, target = assignment.split("-")
    return Map(source=Entity(source), target=Entity(target), ranges=[])


def parse_input():
    maps = {}
    current_map = None
    for line in input_lines:
        match line.split():
            case ["seeds:", *seeds]:
                seeds = [int(seed) for seed in seeds]
            case [assignment, "map:"]:
                if current_map:
                    maps[current_map.source] = current_map
                current_map = new_map(assignment)
            case [target_start, source_start, range_length]:
                current_map.add_range(
                    int(target_start), int(source_start), int(range_length)
                )
    maps[current_map.source] = current_map
    return seeds, maps


def get_location(seed: int, maps: dict[Entity, Map]) -> int:
    source_entity = Entity.Seed
    translation_map: Map = maps[source_entity]
    data = seed
    while source_entity != Entity.Location:
        translation_map = maps[source_entity]
        data = translation_map.translate(data)
        source_entity = translation_map.target
    return data


def task1():
    seeds, maps = parse_input()
    locations = [get_location(seed, maps) for seed in seeds]
    return min(locations)


def task2():
    min_location = 99999999999999999999999999
    seeds, maps = parse_input()
    seed_range_definitions = []
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        length = seeds[i + 1]
        print(start, length)
        seed_range_definitions.append((start, length))
    for definition in seed_range_definitions:
        start, end = definition[0], sum(definition)
        print(start, end)
        seeds = range(start, end)
        for seed in seeds:
            min_location = min(min_location, get_location(seed))
    return min_location


print(task1())
print(task2())
