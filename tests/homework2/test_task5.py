import string

from homework2.task5 import custom_range


def test_0_additional_arg():
    """Testing that with no additional args returns same iterable"""
    assert custom_range(string.ascii_lowercase) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]


def test_arg_is_not_in_sequence():
    """Testing that if at least 1 arg is not in sequence returns same iterable"""
    assert custom_range(string.ascii_lowercase) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]


def test_1_additional_arg():
    """Testing that if 1 additional argument returns everything up to this argument exclusively"""
    assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]


def test_2_additional_args():
    """Testing that if 2 additional args returns everything from 1st arg (inclusively) up to 2nd arg exclusively"""
    assert custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_3_additional_args_negative_step():
    """Testing that if 3 additional args and 3rd is negative
    returns everything from 1st arg inclusively and 2nd arg exclusively with 3rd arg as negative step"""
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]


def test_3_additional_args_positive_step():
    """Testing that if 3 additional args and 3rd is positive
    returns everything from 1st arg inclusively and 2nd arg exclusively with 3rd arg as positive step"""
    assert custom_range(string.ascii_lowercase, "a", "e", 2) == ["a", "c"]
