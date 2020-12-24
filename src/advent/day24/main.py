"""Day 24 of the advent of code challenge."""
from __future__ import annotations

from dataclasses import dataclass
import itertools
from pathlib import Path
from typing import Dict, Iterable, List, NamedTuple, Tuple


class Vector(NamedTuple):
    """Movement through 2D space."""

    x: int
    y: int

    def __add__(self, other: Vector) -> Vector:
        """Sum up vectors."""
        return Vector(self.x + other.x, self.y + other.y)


NEIGHBOUR_VECS = {
    Vector(*xy)
    for xy in itertools.product([1, 0, -1], repeat=2)
    if any(d != 0 for d in xy)
}


class Point(NamedTuple):
    """Location in 2D space."""

    x: int
    y: int

    def __add__(self, other: Vector) -> Point:
        """Apply a vector to a point to find a new point."""
        return Point(self.x + other.x, self.y + other.y)


@dataclass
class Tile:
    point: Point
    black: bool = False
    flips: int = 0

    def flip(self) -> bool:
        self.black = not self.black
        self.flips += 1
        return self.black


def compass_to_vec(compass: str) -> Vector:
    """Turn NSEW into a vector.

    Parameters
    ----------
    compass: str
        N,S,E,orW

    Returns
    -------
    Vector
        The associated vector
    """
    compass_dict: Dict[str, Vector] = {
        "n": Vector(0, 1),
        "s": Vector(0, -1),
        "e": Vector(1, 0),
        "w": Vector(-1, 0),
    }
    if compass not in compass_dict:
        raise IndexError(f"{compass} is not a valid orientation")
    return compass_dict[compass]


def parse_line(line: str) -> Tile:
    """Read a line."""
    tile_point = Point(0, 0)
    for c in line:
        tile_point += compass_to_vec(c)
    return Tile(tile_point)


def read_inputs(filename: str = "input.txt") -> List[Tile]:
    """Read in and parse a text file of inputs.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Returns
    -------
    list[Tile]
        The tile positions
    """
    in_path: Path = Path(__file__).resolve().parent / filename
    with open(in_path, "r") as f:
        return [parse_line(line.strip()) for line in f.readlines()]


def part1(filename: str = "input.txt") -> int:
    """Solve part 1 of the puzzle.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Returns
    -------
    int:
        The answer to part 1
    """
    tiles = read_inputs(filename)
    tile_dict = dict()
    for tile in tiles:
        if tile.point not in tile_dict:
            tile_dict[tile.point] = tile
        tile_dict[tile.point].flip()
    return sum(tile.black for tile in tile_dict.values())


if __name__ == "__main__":
    part1("example.txt")


# def part2(filename: str = "input.txt") -> int:
#     """Solve part 2 of the puzzle.

#     Parameters
#     ----------
#     filename: str
#         The name of the file in this directory to load

#     Returns
#     -------
#     int:
#         The answer to part 2
#     """
#     return -1
