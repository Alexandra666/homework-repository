import pytest
from homework1.task04 import check_sum_of_four


def test_empty_lists_case():
    """Testing that empty lists return 0 and indicates that lists are empty"""
    assert check_sum_of_four([], [], [], []) == 0


def test_no_combs():
    """Testing case with no combinations that give 0"""
    assert check_sum_of_four([8, 1], [7, 2], [0, 17], [8, 0]) == 0


def test_5_combs_case():
    """Testing lists have 5 unique combinations"""
    assert check_sum_of_four([4, 2, -5], [-4, 4, 4], [-1, 4, 4], [1, -5, 5]) == 5


def test_all_combs_case():
    """Testing lists where all combinations give 0"""
    assert check_sum_of_four([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]) == 81
