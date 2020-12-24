"""Day 24 of the advent of code challenge."""
from __future__ import annotations

from dataclasses import dataclass
import itertools
from pathlib import Path
from typing import Dict, List, NamedTuple


class Vector(NamedTuple):
    """Movement through 2D space."""

    x: int
    y: int

    def __add__(self, other: Vector) -> Vector:  # type: ignore
        """Sum up vectors.

        Parameters
        ----------
        other: Vector
            The other vector to add to the first

        Returns
        -------
        Vector
            Sum of the two vectors
        """
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

    def __add__(self, other: Vector) -> Point:  # type: ignore
        """Apply a vector to a point to find a new point.

        Parameters
        ----------
        other: Vector
            The other vector to add to the first

        Returns
        -------
        Point
            The new point after the vector is applied
        """
        return Point(self.x + other.x, self.y + other.y)


@dataclass
class Tile:
    """I'm a tile."""

    point: Point
    black: bool = False
    flips: int = 0

    def flip(self) -> bool:
        """Flip the tile.

        Returns
        -------
        bool:
            Whether the tile is black after the flip
        """
        self.black = not self.black
        self.flips += 1
        return self.black


def compass_to_vec(compass: str) -> Vector:
    """Turn NSEW into a vector.

    Parameters
    ----------
    compass: str
        nw, ne, sw, se, e, or w

    Returns
    -------
    Vector
        The associated vector
    """
    compass_dict: Dict[str, Vector] = {
        "nw": Vector(-1, 1),
        "ne": Vector(1, 1),
        "sw": Vector(-1, -1),
        "se": Vector(1, -1),
        "e": Vector(2, 0),
        "w": Vector(-2, 0),
    }
    if compass not in compass_dict:
        raise IndexError(f"{compass} is not a valid orientation")
    return compass_dict[compass]


def parse_line(line: str) -> Tile:
    """Read a line.

    Parameters
    ----------
    line: str
        The input line from the puzzle

    Returns
    -------
    Tile
        The tile you land on after taking all the steps.
    """
    tile_point = Point(0, 0)
    i = 0
    while i < len(line):
        if line[i] in ("n", "s"):
            c = "".join((line[i], line[i + 1]))
            i += 2
        else:
            c = line[i]
            i += 1
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
    part1("input.txt")


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
