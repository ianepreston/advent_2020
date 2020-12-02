"""Test examples and solutions to day 0 (2019 day 1)."""
from advent.day01 import main


def test_part_1_example():
    """Check the example for part 1."""
    test_result = main.part1("example.txt")
    assert test_result == 514579


def test_part_1_actual():
    """Check the actual answer to part 1."""
    test_result = main.part1()
    assert test_result == 1019571
