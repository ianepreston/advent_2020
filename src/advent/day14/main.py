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


def part2_bitmasks(line: str) -> str:
    """Now I have to handle X explicitly. Sigh.

    Parameters
    ----------
    line: str
        Line from the input file
    
    Returns
    -------
    str:
        Clean text string of the bitmask
    """
    return line.strip().replace("mask = ", "")


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


def apply_bitmasks2(bitmask: str, index: int) -> List[int]:
    """Apply a bitmask using part 2 rules to an integer.

    Parameters
    ----------
    bitmask: str
        The bitmask to apply
    index: int
        The index integer to apply the bitmask on
    
    Returns
    -------
    List[int]
        All permutations of the bitmasked address
    """
    index_bitstring: str = int_to_bits(index)
    index_bitlist: List[str] = [c for c in index_bitstring]
    # Do the simple flips first
    floating_indices = []
    for i, v in enumerate(c for c in bitmask):
        if v == "1":
            index_bitlist[i] = v
        elif v == "X":
            floating_indices.append(i)
    # If there's no masks we're set
    if not floating_indices:
        return [bits_to_int("".join(index_bitlist))]
    # Handle all the permutations
    permutations: int = 2 ** len(floating_indices)
    addresses: List[int] = []
    for i in range(permutations):
        update_bitlist: List[str] = index_bitlist[:]
        mask_str: str = f"{i:0b}".zfill(len(floating_indices))
        for j, v in zip(floating_indices, mask_str):
            update_bitlist[j] = v
        addresses.append(bits_to_int("".join(update_bitlist)))
    return addresses


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
    bitmask: str = ""
    addresses: Counter = Counter()
    in_path: Path = Path(__file__).resolve().parent / filename
    with open(in_path, "r") as f:
        for line in f.readlines():
            if line.startswith("mask"):
                bitmask = part2_bitmasks(line)
            elif line.startswith("mem"):
                address: Address = parse_address(line)
                for index in apply_bitmasks2(bitmask, address.index):
                    addresses[index] = address.value
            else:
                raise ValueError(f"unrecognized line: {line}")
    return sum(addresses.values())


if __name__ == "__main__":
    part2("example2.txt")
