"""Day 08 of the advent of code challenge."""
from __future__ import annotations

from pathlib import Path
import re
from typing import Dict, List, Optional, Tuple


def read_inputs(filename: str = "input.txt") -> Dict[str, Bag]:
    """Read in and parse a text file of inputs.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Returns
    -------
    dict:
        A dictionary of all bags
    """
    here: Path = Path(__file__).resolve().parent
    in_path: Path = here / filename
    with open(in_path, "r") as f:


def part1(filename: str = "input.txt") -> int:
    """Solve part 1 of the puzzle.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Returns
    -------
    int:
        The number of bags that contain the shiny gold bag
    """
    pass


def part2(filename: str = "input.txt") -> int:
    """Solve part 2 of the puzzle.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Returns
    -------
    int:
        The number of bags that the shiny gold bag contains
    """
    pass