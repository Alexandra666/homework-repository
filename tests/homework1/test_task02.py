import pytest
from homework1.task02 import check_fibonacci


def test_empty_list_case():
    """Testing that sequence with less than 3 elements will not pass"""
    assert not check_fibonacci([])
    assert not check_fibonacci([1])


def test_positive_case():
    """Testing that sequence is fibonacci sequence"""
    assert check_fibonacci(
        [
            0,
            1,
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34,
            55,
            89,
            144,
            233,
            377,
            610,
            987,
            1597,
            2584,
            4181,
            6765,
        ]
    )


def test_negative_case():
    """Testing that sequence is not fibonacci sequence"""
    assert not check_fibonacci([0, 1, 1, 6])
