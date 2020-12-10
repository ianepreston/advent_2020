"""Day 10 of the advent of code challenge."""
from __future__ import annotations

from pathlib import Path
from typing import List, Dict


def read_inputs(filename: str = "input.txt") -> List[int]:
    """Read in and parse a text file of inputs.

    Parameters
    ----------
    filename: str
        The name of the file in this directory to load

    Returns
    -------
    list[int]
        The numbers in the series
    """
    in_path: Path = Path(__file__).resolve().parent / filename
    with open(in_path, "r") as f:
        return [int(line.strip()) for line in f.readlines()]


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
    sorted_inputs: List[int] = sorted(read_inputs(filename))
    current_jolts: int = 0
    jolt_1: int = 0
    jolt_3: int = 0
    for jolt in sorted_inputs:
        diff: int = jolt - current_jolts
        if diff == 1:
            jolt_1 += 1
        elif diff == 3:
            jolt_3 += 1
        else:
            raise ValueError(f"Diff of {diff} is invalid")
        current_jolts = jolt
    # Add in the device itself
    jolt_3 += 1
    return jolt_1 * jolt_3


class Node(object):
    def __init__(self, value: int):
        self.value = value
        self.children: List[Node] = []

    def __lt__(self, other: Node) -> bool:
        return self.value < other.value

    def __le__(self, other: Node) -> bool:
        return self.value <= other.value

    def __eq__(self, other: Node) -> bool:
        return self.value == other.value

    def __ne__(self, other: Node) -> bool:
        return self.value != other.value

    def __gt__(self, other: Node) -> bool:
        return self.value > other.value

    def __ge__(self, other: Node) -> bool:
        return self.value >= other.value

    def __str__(self) -> str:
        return str(self.value)
    
    def __repr__(self) -> str:
        return str(self.value)
    
    def forks(self) -> int:
        if not self.children:
            return 1
        else:
            return sum(child.forks() for child in self.children)
    


    



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
    num_list: List[int] = sorted(read_inputs(filename))
    num_list.append(max(num_list) + 3)  # add the actual device
    num_list.insert(0, 0)  # add the wall port
    top_node: int = num_list[-1]
    node_dict: Dict[int, Node] = dict()
    while num_list:
        next_num: int = num_list.pop()
        if next_num not in node_dict:
            node_dict[next_num] = Node(next_num)
        children: List[int] = [item for item in num_list[-3:] if next_num - item <= 3]
        for child in children:
            if child not in node_dict:
                node_dict[child] = Node(child)
            node_dict[next_num].children.append(node_dict[child])
    return node_dict[top_node].forks()



if __name__ == "__main__":
    part2("example1.txt")
