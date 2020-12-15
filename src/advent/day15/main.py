"""Day 14 of the advent of code challenge."""
from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Tuple


def part1(start_seq: Tuple[int, ...] = (9, 19, 1, 6, 0, 5, 4)) -> int:
    """Solve part 1 of the puzzle.

    Parameters
    ----------
    start_seq: List[int]
        The numbers to start the memory game

    Returns
    -------
    int:
        The answer to part 1
    """
    # set up turn trackers
    turn: int = 1
    turn_counter: Dict[int, List[int]] = defaultdict(list)
    # load in the starting sequence
    for num in start_seq:
        turn_counter[num].append(turn)
        turn += 1
    last_num: int = start_seq[-1]
    while turn <= 2020:
        if len(turn_counter[last_num]) < 2:
            last_num = 0
        else:
            last_num = turn_counter[last_num][-1] - turn_counter[last_num][-2]
        turn_counter[last_num].append(turn)
        turn += 1
    return last_num
