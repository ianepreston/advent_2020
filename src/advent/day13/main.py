"""Day 13 of the advent of code challenge."""
from __future__ import annotations

from pathlib import Path
from typing import List, NamedTuple, Tuple


def read_inputs(filename: str = "input.txt") -> Tuple[int, List[int]]:
    """Read in and parse a text file of inputs.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Returns
    -------
    List[Tuple[int, List[int]]]
        Current time and bus list
    """
    in_path: Path = Path(__file__).resolve().parent / filename
    with open(in_path, "r") as f:
        current_time: int = int(f.readline())
        busses: List[int] = [
            int(char) for char in f.readline().split(",") if char != "x"
        ]
        return current_time, busses


class Bus(NamedTuple):
    """beep beep."""

    current_time: int
    frequency: int

    @property
    def minutes_to_next(self) -> int:
        """Calculate how many minutes until the next bus.

        Returns
        -------
        int:
            How many minutes until the next bus arrives
        """
        multiplier: int = (self.current_time // self.frequency) + 1
        minutes_left: int = (self.frequency * multiplier) - self.current_time
        return minutes_left

    @property
    def part1(self) -> int:
        """Answer part1 for a given bus.

        Returns
        -------
        int
            frequency * minutes_to_next
        """
        return self.frequency * self.minutes_to_next


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
    curr_time: int
    bus_nums: List[int]
    curr_time, bus_nums = read_inputs(filename)
    busses: List[Bus] = [Bus(curr_time, num) for num in bus_nums]
    next_bus: Bus = min(busses, key=lambda bus: bus.minutes_to_next)
    return next_bus.part1


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
