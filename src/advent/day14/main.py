"""Day 14 of the advent of code challenge."""
from __future__ import annotations

import itertools
from pathlib import Path
from typing import Dict, Iterable, List, NamedTuple, Tuple


def read_inputs(filename: str = "input.txt") -> List[Tuple[str, int]]:
    """Read in and parse a text file of inputs.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Returns
    -------
    list[Tuple[str, int]]
        The directions
    """
    in_path: Path = Path(__file__).resolve().parent / filename
    with open(in_path, "r") as f:
        return [(line[0], int(line[1:])) for line in f.readlines()]

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
    directions: List[Tuple[str, int]] = read_inputs(filename)
    boaty_mc_boatface = Ship()
    for direction in directions:
        boaty_mc_boatface.take_direction_deprecated(direction)
    return boaty_mc_boatface.manhattan_dist


def part2(filename: str = "input.txt") -> int:
    """Solve part 2 of the puzzle.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Returns
    -------
    int:
        The answer to part 2
    """
    directions: List[Tuple[str, int]] = read_inputs(filename)
    boaty_mc_boatface = Ship()
    for direction in directions:
        boaty_mc_boatface.take_direction_updated(direction)
    return boaty_mc_boatface.manhattan_dist