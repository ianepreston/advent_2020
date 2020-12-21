"""Day 20 of the advent of code challenge."""
from __future__ import annotations

from collections import defaultdict
import numpy as np
from dataclasses import dataclass
from pathlib import Path
import re
import math
from typing import (
    Counter,
    List,
    Set,
)


@dataclass
class Tile:
    """I'm a tile in an image."""

    id: int
    layout: np.ndarray
    rotation: int = 0

    def hflip(self) -> None:
        """Flip left to right."""
        self.layout = [row[::-1] for row in self.layout]
        self.h_flipped = not self.h_flipped

    def vflip(self) -> None:
        """Flip top to bottom."""
        self.layout = self.layout[::-1]
        self.v_flipped = not self.v_flipped

    @property
    def left(self) -> str:
        """Left side of the layout."""
        return "".join(row[0] for row in self.layout)

    @property
    def right(self) -> str:
        """Right side of the layout."""
        return "".join(row[-1] for row in self.layout)

    @property
    def h_sides(self) -> List[str]:
        """Left and right sides of the layout."""
        return [self.left, self.right]

    @property
    def top(self) -> str:
        """Top of the layout."""
        return self.layout[0]

    @property
    def bottom(self) -> str:
        """Bottom of the layout."""
        return self.layout[-1]

    @property
    def v_sides(self) -> List[str]:
        """Top and bottom sides of the layout."""
        return [self.top, self.bottom]

    def h_match(self, other: Tile) -> bool:
        """If either of the horizontal edges can match."""
        for side in self.h_sides:
            if side in other.h_sides:
                return True
            other.vflip()
            if side in other.h_sides:
                other.vflip()
                return True
            other.vflip()
            return False

    def v_match(self, other: Tile) -> bool:
        """If either of the horizontal edges can match."""
        for side in self.v_sides:
            if side in other.v_sides:
                return True
            other.hflip()
            if side in other.v_sides:
                other.vflip()
                return True
            other.hflip()
            return False


def parse_tile(input: str) -> Tile:
    """Turn a string into a tile.
    
    Parameters
    ----------
    input: str
        Text representation of tile
    
    Returns
    -------
    Tile
        parsed tile
    """
    lines = input.split("\n")
    id_str = lines.pop(0)
    id = int(id_str.replace("Tile ", "").replace(":", ""))
    return Tile(id=id, layout=lines)


def read_input(filename: str):
    """Load the input for the puzzle.

    Parameters
    ----------
    filename: str
        input.txt or example.txt
    
    Returns
    -------
    A thing
    """
    file: Path = Path(__file__).resolve().parent / filename
    with open(file, "r") as f:
        return [parse_tile(line) for line in f.read().split("\n\n")]


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
    tiles = read_input(filename)
    dim = int(math.sqrt(len(tiles)))
    if dim ** 2 != len(tiles):
        raise ValueError("Didn't get a correct number of tiles to form a square")
    h_matches = Counter()
    v_matches = Counter()
    for count_tile in tiles:
        for compare_tile in tiles:
            if count_tile.id == compare_tile.id:
                pass
            else:
                if count_tile.h_match(compare_tile):
                    h_matches[count_tile.id] += 1
                if count_tile.v_match(compare_tile):
                    v_matches[count_tile.id] += 1
    h_edge_ids = [id for id, count in h_matches.items() if count == 1]
    v_edge_ids = [id for id, count in v_matches.items() if count == 1]
    if not len(h_edge_ids) == len(v_edge_ids) == dim * 2:
        raise ValueError(
            f"Didn't find the correct number of edges, v: {len(v_edge_ids)} h: {len(h_edge_ids)}, dim: {dim}"
        )
    corners = set.intersection([set(h_edge_ids), set(v_edge_ids)])
    if not len(corners) == 4:
        raise ValueError(f"Wrong number of corners found : {len(corners)}")
    return math.prod(corners)


def part2(filename: str = "input.txt") -> str:
    """Solve part 2 of the puzzle.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Returns
    -------
    str:
        The answer to part 2
    """
    return -1


if __name__ == "__main__":
    part1("example.txt")
