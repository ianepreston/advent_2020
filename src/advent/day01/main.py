"""Day 01 of the advent of code challenge."""
from pathlib import Path
from typing import List


def read_inputs(filename: str) -> List[int]:
    """Read in a text file of inputs.

    Parameters
    ----------
    filename: str
        The name of the file, should be in the same folder as this module

    Returns
    -------
    [int]
        All the inputs
    """
    here: Path = Path(__file__).resolve().parent
    in_path: Path = here / filename
    with open(in_path, "r") as f:
        return [int(line) for line in f.readlines()]


def part1(filename: str = "input.txt") -> int:
    """Solve part 1 of the challenge.

    Parameters
    ----------
    filename: str
        The name of the file, should be in the same folder as this module

    Returns
    -------
    int
        The product of the pair of numbers that add to 2020
    """
    sorted_inputs: List[int] = sorted(read_inputs(filename))
    low_index: int = 0
    high_index: int = len(sorted_inputs) - 1
    while low_index < high_index:
        low: int = sorted_inputs[low_index]
        high: int = sorted_inputs[high_index]
        lh_sum: int = low + high
        if lh_sum == 2020:
            return low * high
        elif lh_sum < 2020:
            low_index += 1
        else:
            high_index -= 1
    return -1
