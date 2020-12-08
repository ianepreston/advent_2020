"""Day 08 of the advent of code challenge."""
from __future__ import annotations

from pathlib import Path
from typing import List, NamedTuple, Set, Union


class Instruction(NamedTuple):
    """I'm an instruction."""

    cmd: str
    num: int


class Compy:
    """I'm a computer."""

    def __init__(self) -> None:
        """Instantiate with index and accumulator at 0. No instructions loaded."""
        self.index: int = 0
        self.accumulator: int = 0
        self.instructions: List[Instruction] = []

    @staticmethod
    def _parse_instruction(line: str) -> Instruction:
        """Turn a line of text into an Instruction.
        
        Parameters
        ----------
        line: str
            An instruction in string form
        
        Returns
        -------
        Instruction
            The parsed instruction
        """
        cmd, num = line.strip().split()
        return Instruction(cmd, int(num))

    def load_program(self, file: Union[Path, str]) -> None:
        """Read in a text file to get a list of Instructions.

        Parameters
        ----------
        file: Path
            The file to load
        """
        with open(file, "r") as f:
            self.instructions = [
                self._parse_instruction(line) for line in f.readlines()
            ]

    def _exec_instruction(self, instruction: Instruction) -> None:
        """Run an instruction.
        
        Parameters
        ----------
        instruction: Instruction
            The instruction to run
        """
        if instruction.cmd == "nop":
            pass
            self.index += 1
        elif instruction.cmd == "acc":
            self.accumulator += instruction.num
            self.index += 1
        elif instruction.cmd == "jmp":
            if 0 <= self.index + instruction.num < len(self.instructions):
                self.index += instruction.num
            else:
                raise IndexError("Jumped out of instruction set")
        else:
            raise ValueError(f"Unsupported instruction: {instruction.cmd}")

    def step(self) -> None:
        """Execute the next instruction."""
        instruction: Instruction = self.instructions[self.index]
        self._exec_instruction(instruction)


def part1(filename: str = "input.txt") -> int:
    """Solve part 1 of the puzzle.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Returns
    -------
    int:
        The value of the accumulator right before a loop
    """
    indices: Set[int] = set()
    compy: Compy = Compy()
    infile: Path = Path(__file__).resolve().parent / filename
    compy.load_program(infile)
    while True:
        if compy.index in indices:
            return compy.accumulator
        else:
            indices.add(compy.index)
            compy.step()


# def part2(filename: str = "input.txt") -> int:
#     """Solve part 2 of the puzzle.

#     Parameters
#     ----------
#     filename: str
#         The name of the file in this directory to load

#     Returns
#     -------
#     int:
#         The number of bags that the shiny gold bag contains
#     """
#     pass
