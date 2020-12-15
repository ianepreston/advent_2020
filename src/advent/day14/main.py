"""Day 14 of the advent of code challenge."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
from typing import Generator, List, NamedTuple, Optional


def int_to_bits(num: int) -> str:
    """Turn an integer into a 32 bit unsigned int.

    Parameters
    ----------
    num: int
        input integer
    
    Returns
    -------
    str
        32 bit unsigned integer
    """
    return f"{num:036b}"


def bits_to_int(bits: str) -> int:
    """Turn a bitstring back to an integer.
    
    Parameters
    ----------
    bits: str
        String representation of binary
    
    Returns
    -------
    int
        The integer equivalent
    """
    return int(bits, 2)


class Bitmask(NamedTuple):
    """Replace a bit at a point."""

    index: int
    bit: str


class Address(NamedTuple):
    """Index and value."""

    index: int
    value: int


class FileLine(NamedTuple):
    """Line from the file, can be a bitmask or an address."""

    bitmasks: Optional(List[Bitmask])
    address: Optional(Address)


def parse_bitmasks(line: str) -> List[Bitmask]:
    """Turn a line of text into a bitmask.

    Parameters
    ----------
    line: str
        raw input line for a bitmask
    
    Returns
    -------
    Bitmask:
        parsed bitmask
    """
    return [
        Bitmask(i, v)
        for i, v in enumerate(line.strip().replace("mask = ", ""))
        if v != "X"
    ]


def apply_bitmasks(bitmasks: List[Bitmask], value: int) -> int:
    """Apply a bitmask to an integer.

    Parameters
    ----------
    bitmasks: List[Bitmask]
        List of bitmasks to apply
    value: int
        The integer to apply the bitmask to
    
    Returns
    -------
    int
        Integer value after bitmask is applied
    """
    value_bitstring = int_to_bits(value)
    value_bitlist = [c for c in value_bitstring]
    for bitmask in bitmasks:
        value_bitlist[bitmask.index] = bitmask.bit
    return bits_to_int("".join(c for c in value_bitlist))


def parse_address(line: str) -> Address:
    """Line of text to address to update.
    
    Parameters
    ----------
    line: str
        Turn a line from the input into an Address
    
    Returns
    -------
    Address
        Parsed index and value
    """
    rgx = r"mem\[(\d+)\] = (\d+)"
    address_str: str
    value_str: str
    address_str, value_str = re.match(rgx, line).groups()
    return Address(int(address_str), int(value_str))


def read_inputs(filename: str = "input.txt") -> Generator(FileLine):
    """Read in and parse a text file of inputs.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Yields
    ------
    FileLine
        parsed line from the file
    """
    in_path: Path = Path(__file__).resolve().parent / filename
    with open(in_path, "r") as f:
        for line in f.readlines():
            if line.startswith("mask"):
                yield FileLine(parse_bitmasks(line), None)
            elif line.startswith("mem"):
                yield FileLine(None, parse_address(line))
            else:
                raise ValueError(f"unrecognized line: {line}")


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
    # initialize empty bitmask
    bitmasks: List[Bitmask] = list()
    addresses: Counter = Counter()
    for fileline in read_inputs(filename):
        if fileline.bitmasks is not None:
            bitmasks = fileline.bitmasks
        elif fileline.address is not None:
            addresses[fileline.address.index] = apply_bitmasks(
                bitmasks, fileline.address.value
            )
    return sum(addresses.values())


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
