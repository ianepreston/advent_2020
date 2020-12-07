"""Test examples and solutions to day 08."""
from advent.day08 import main


def test_part_1_example():
    """Check the example for part 1."""
    test_result = main.part1("example.txt")
    assert test_result == 4


def test_part_1_actual():
    """Check the example for part 1."""
    test_result = main.part1()
    assert test_result == 121


def test_part_2_example():
    """Check the example for part 2."""
    test_result = main.part2("example.txt")
    assert test_result == 32


def test_part_2_actual():
    """Check the example for part 2."""
    test_result = main.part2()
    assert test_result == 3805
