"""Day 16 of the advent of code challenge."""
from __future__ import annotations

from pathlib import Path
import re
from typing import List, NamedTuple, Optional, Set, Tuple


class Rule(NamedTuple):
    """I define a ticket field's valid numbers."""

    name: str
    valid: Set[int]


def parse_rule(line: str) -> Rule:
    """Take an input line and get a rule.

    Parameters
    ----------
    line: str
        text from the puzzle input
    
    Returns
    -------
    Rule:
        parsed rule
    """
    rgx: re.Pattern = re.compile(r"^(.+): (\d+)-(\d+) or (\d+)-(\d+)$")
    match: Optional[re.Match] = rgx.match(line)
    if not match:
        raise ValueError(f"couldn't parse rule line {line}")
    name: str
    low1: str
    high1: str
    low2: str
    high2: str
    name, low1, high1, low2, high2 = match.groups()
    valid: Set[int] = {i for i in range(int(low1), int(high1) + 1)}
    for i in range(int(low2), int(high2) + 1):
        valid.add(i)
    return Rule(name, valid)


def read_inputs(
    filename: str = "input.txt",
) -> Tuple[List[Rule], List[int], List[List[int]]]:
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
        puzzle = f.read()
    rules: str
    mine: str
    others: str
    rules, mine, others = puzzle.split("\n\n")
    rule_list: List[Rule] = [parse_rule(line) for line in rules.split("\n")]
    for line in mine.split("\n"):
        if line.startswith("your"):
            pass
        else:
            my_nums: List[int] = [int(char) for char in line.split(",")]
    other_nums: List[List[int]] = [
        [int(char) for char in line.split(",")]
        for line in others.split("\n")
        if not line.startswith("nearby")
    ]
    return rule_list, my_nums, other_nums


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
    rules: List[Rule]
    my_nums: List[int]
    other_nums: List[List[int]]
    rules, my_nums, other_nums = read_inputs(filename)
    all_valid: Set[int] = set.union(*[rule.valid for rule in rules])
    invalid_nums: List[int] = [
        num for ticket in other_nums for num in ticket if num not in all_valid
    ]
    return sum(invalid_nums)


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
    return 1


if __name__ == "__main__":
    print(part1("example.txt"))
