"""Day 04 of the advent of code challenge."""
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Generator, List, Tuple, Union


@dataclass
class Passport:
    """Class for the elements of a passport."""

    byr: Union[int, None] = None
    iyr: Union[int, None] = None
    eyr: Union[int, None] = None
    hgt: Union[str, None] = None
    hcl: Union[str, None] = None
    ecl: Union[str, None] = None
    pid: Union[str, None] = None
    cid: Union[str, None] = None

    def __getitem__(self, item: str) -> Any:
        """Use dictionary key style accessors to get passport attributes.

        Parameters
        ----------
        item: str
            The attribute to get, e.g. byr
        
        Returns
        -------
        Any
            The value of the class attribute
        """
        return getattr(self, item)

    def __setitem__(self, item: str, value: Any) -> None:
        """Use dictionary key style accessors to set passport attributes.

        Parameters
        ----------
        item: str
            The attribute to set, e.g. byr
        value: Any
            The value to set that item to
        """
        setattr(self, item, value)

    def is_valid_north_pole(self) -> bool:
        """Check if the passport is a valid North pole credential.

        Returns
        -------
        bool
            If the passport has all elements except possibly cid
        """
        fields: Tuple[str, ...] = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
        return all(self[field] is not None for field in fields)


def read_inputs(filename: str) -> Generator[Passport, None, None]:
    """Read in and parse a text file of inputs.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Yields
    ------
    Passport
        The next fully parsed passport
    """
    here: Path = Path(__file__).resolve().parent
    in_path: Path = here / filename
    numeric_fields: Tuple[str, ...] = ("byr", "iyr", "eyr")
    passport: Passport = Passport()
    with open(in_path, "r") as f:
        for line in f.readlines():
            if line != "\n":
                # print(line)
                fields: List[str] = line.split()
                for field in fields:
                    key, val = field.split(":")
                    if key in numeric_fields:
                        passport[key] = int(val)
                    else:
                        passport[key] = val
            else:
                yield passport
                passport = Passport()
    # Return the last one
    yield passport


def part1(filename: str = "input.txt") -> int:
    """Solve part 1 of the puzzle.

    Parameters
    ----------
    filename: str
        The file to read in
    
    Returns
    -------
    int:
        The number of valid passports
    """
    return sum(passport.is_valid_north_pole() for passport in read_inputs(filename))
