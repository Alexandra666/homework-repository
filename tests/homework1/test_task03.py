# import pytest

from homework1.task03 import find_maximum_and_minimum


def test_empty_file(tmp_path):
    """Testing that func on empty file returns None and prints that file is empty"""
    d = tmp_path
    some_file = d / "test_02_empty.txt"
    some_file.write_text("")
    assert find_maximum_and_minimum(some_file) == ()


def test_1_num(tmp_path):
    """Testing that func on file with 1 number returns that number and prints that only 1 number"""
    d = tmp_path
    some_file = d / "test_02_1_num.txt"
    some_file.write_text("5")
    assert find_maximum_and_minimum(some_file) == (5, 5)


def test_sequence(tmp_path):
    """Testing that on sequence of integers returns min and max"""
    d = tmp_path
    some_file = d / "test_02_sequence.txt"
    some_file.write_text(
        """5 7 9 -2 0 11 3 5 6
    -4 7 4  77 4 4 """
    )
    assert find_maximum_and_minimum(some_file) == (-4, 77)


def test_same_nums(tmp_path):
    """Testing that sequence of same numbers returns tuple with same numbers"""
    d = tmp_path
    some_file = d / "test_02_same_nums.txt"
    some_file.write_text(
        """9 9 9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 """
    )
    assert find_maximum_and_minimum(some_file) == (9, 9)
