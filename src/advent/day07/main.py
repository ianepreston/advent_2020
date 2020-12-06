"""Day 06 of the advent of code challenge."""
from __future__ import annotations

from pathlib import Path
from typing import Generator, Set


def read_inputs(filename: str = "input.txt") -> Generator[Set, None, None]:
    """Read in and parse a text file of inputs.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Yields
    ------
    Set
        All questions answered "yes" at least once on the questionnaire per group
    """
    here: Path = Path(__file__).resolve().parent
    in_path: Path = here / filename
    with open(in_path, "r") as f:
        for line in f.read().split("\n\n"):
            yield set(char for char in line.replace("\n", ""))