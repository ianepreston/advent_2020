"""I'm a computer, stop all the downloading."""
from __future__ import annotations

from pathlib import Path
from typing import List, NamedTuple, Union


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
        self.run_complete: bool = False

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
        self.run_complete = False

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
            if 0 <= self.index + instruction.num <= len(self.instructions):
                self.index += instruction.num
            else:
                raise IndexError("Jumped out of instruction set")
        else:
            raise ValueError(f"Unsupported instruction: {instruction.cmd}")
        if self.index == len(self.instructions):
            self.run_complete = True

    def step(self) -> None:
        """Execute the next instruction."""
        instruction: Instruction = self.instructions[self.index]
        self._exec_instruction(instruction)

    def full_run(self) -> None:
        """Execute the program all the way through."""
        while not self.run_complete:
            self.step()
