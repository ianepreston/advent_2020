"""Day 23 of the advent of code challenge."""
from __future__ import annotations

from itertools import cycle
from typing import List, Tuple

EG_CUPS = [int(x) for x in "389125467"]
IN_CUPS = [int(x) for x in "459672813"]


def cups_round(cups: List[int], current_cup: int = 0) -> Tuple[List[int], int]:
    """Play a round of cups.

    Parameters
    ----------
    cups: List[int]
        The sequence of cups
    current_cup: int
        The index of the current cup for the round

    Returns
    -------
    Tuple[List[int], int]
        The updated state of the game


    The crab picks up the three cups that are immediately clockwise of the current cup.
    They are removed from the circle; cup spacing is adjusted as necessary to maintain
    the circle.

    The crab selects a destination cup: the cup with a label equal to the current cup's
    label minus one. If this would select one of the cups that was just picked up, the
    crab will keep subtracting one until it finds a cup that wasn't just picked up.
    If at any point in this process the value goes below the lowest value on any cup's
    label, it wraps around to the highest value on any cup's label instead.

    The crab places the cups it just picked up so that they are immediately clockwise of
    the destination cup. They keep the same order as when they were picked up.

    The crab selects a new current cup: the cup which is immediately clockwise of the
    current cup.
    """
    # First step, pick up three cups after the current cup
    current_label = cups[current_cup]
    cup_cycle = cycle(cups)
    cycle_front = next(cup_cycle)
    while cycle_front != current_label:
        cycle_front = next(cup_cycle)
    picked_cups = [next(cup_cycle) for _ in range(3)]
    subset_cups = [cup for cup in cups if cup not in picked_cups]
    # Pick a destination cup
    dest_label = current_label - 1
    if dest_label not in subset_cups:
        # Do a brute forcey way for now
        while dest_label not in subset_cups:
            dest_label -= 1
            if dest_label < min(subset_cups):
                dest_label = max(subset_cups)
                break
    dest_index = subset_cups.index(dest_label)
    # using append so I want to supply the index after the index I'm adding at
    dest_index = (dest_index + 1) % len(subset_cups)
    while picked_cups:
        subset_cups.insert(dest_index, picked_cups.pop())
    # pick the next cup
    current_index = subset_cups.index(current_label)
    new_index = (current_index + 1) % len(subset_cups)
    return subset_cups, new_index


def part1(cups: List[int] = IN_CUPS) -> str:
    """Solve part 1 of the puzzle.

    Parameters
    ----------
    cups: List[int]
        The starting sequence of cups

    Returns
    -------
    int:
        The answer to part 1
    """
    cups_index = 0
    for _ in range(100):
        cups, cups_index = cups_round(cups, cups_index)
    one_index = cups.index(1)
    cups_ordered = cups[one_index + 1 :] + cups[:one_index]
    return "".join(str(x) for x in cups_ordered)
