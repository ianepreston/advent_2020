"""Day 02 of the advent of code challenge."""
from pathlib import Path
import math
from typing import List, Tuple


def read_inputs(filename: str) -> List[List[bool]]:
    """Read in and parse a text file of inputs.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Returns
    -------
    List[List[bool]]
        array of coordinates
    """
    here: Path = Path(__file__).resolve().parent
    in_path: Path = here / filename
    with open(in_path, "r") as f:
        return [[char == "#" for char in line] for line in f]


class Sledding:
    def __init__(self, filename: str = "input.txt") -> None:
        self.grid = read_inputs(filename)

    def traverse(self, down: int = 1, right: int = 3) -> int:
        """Follow the grid."""
        y: int = 0
        x: int = 0
        trees: int = 0
        while y < len(self.grid):
            if self.grid[y][x]:
                trees += 1
            x = (x + right) % (len(self.grid[y]) - 1)
            y += down
        return trees
    
    def part2(self) -> int:
        """Try some other paths."""
        slopes: Tuple(Tuple(int, int)) = (
            (1, 1),
            (1, 3),
            (1, 5),
            (1, 7),
            (2, 1),
        )
        return math.prod(self.traverse(*path) for path in slopes)

