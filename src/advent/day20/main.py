"""Day 20 of the advent of code challenge."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re
from typing import Any, DefaultDict, Dict, List, NamedTuple, Optional, Set, Tuple


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
        pass


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
    return -1


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