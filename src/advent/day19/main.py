"""Day 19 of the advent of code challenge."""
from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import Dict, List, NamedTuple, Optional, Tuple


class Rule(NamedTuple):
    """I'm  a message rule."""

    id: int
    literal: Optional[str] = None
    child_rules: List[int] = []


def parse_rule(line: str) -> Rule:
    """Generate a rule.

    Parameters
    ----------
    line: str
        input line representing a rule
    
    Returns
    -------
    Rule
        The parsed rule
    """
    id, rules = line.strip().split(": ")
    if rules.startswith('"'):
        return Rule(id=int(id), literal=rules.replace('"', ""))
    choices = rules.split("|")
    return Rule(
        id=int(id), child_rules=[[int(n) for n in choice.split()] for choice in choices]
    )


def read_inputs(filename: str) -> Tuple[Dict[int, Rule], List[str]]:
    """Read in a text file of inputs.

    Parameters
    ----------
    filename: str
        The name of the file, should be in the same folder as this module


    Returns
    -------
    rules_dict, messages
        dictionary of rule ids mapped to rule objects and a list of messages
    """
    here: Path = Path(__file__).resolve().parent
    in_path: Path = here / filename
    with open(in_path, "r") as f:
        rules_str: str
        messages_str: str
        rules_str, messages_str = f.read().split("\n\n")
    rules_dict: Dict[int, Rule] = {
        rule.id: rule
        for rule in (parse_rule(ruleline) for ruleline in rules_str.split("\n"))
    }
    messages: List[str] = [message for message in messages_str.split("\n")]
    return rules_dict, messages

def check_message(rules_dict: Dict[int, Rule], message: str) -> bool:
    """Check if a message is valid."""
    


def part1(filename: str = "input.txt") -> int:
    """Solve part 1 of the challenge.

    Parameters
    ----------
    filename: str
        The name of the file, should be in the same folder as this module

    Returns
    -------
    int
        The answer to part 1
    """
    current_active: Set[Cube] = read_inputs(filename)
    for _ in range(6):
        current_active = cycle(current_active)
    return len(current_active)


# def part2(filename: str = "input.txt") -> int:
#     """Solve part 2 of the challenge.

#     Parameters
#     ----------
#     filename: str
#         The name of the file, should be in the same folder as this module

#     Returns
#     -------
#     int
#         The answer to part 2
#     """
#     current_active: Set[Cube] = read_inputs(filename, hypercube=True)
#     for _ in range(6):
#         current_active = cycle(current_active)
#     return len(current_active)

if __name__ == "__main__":
    rules_dict, messages = read_inputs("example.txt")
