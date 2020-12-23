"""Test examples and solutions to day 23."""
from advent.day23 import main


def test_part_1_example():
    """Check the example for part 1."""
    test_result = main.part1(main.EG_CUPS)
    assert test_result == "67384529"


def test_part_1_actual():
    """Check the example for part 1."""
    test_result = main.part1(main.IN_CUPS)
    assert test_result == "68245739"


# def test_part_2_example():
#     """Check the example for part 2."""
#     test_result = main.part2("example.txt")
#     assert test_result == 291


# def test_part_2_actual():
#     """Check the example for part 1."""
#     test_result = main.part2("input.txt")
#     assert test_result == 32519
