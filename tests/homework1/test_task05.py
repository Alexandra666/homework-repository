import pytest
from homework1.task05 import find_maximal_subarray_sum


def test_empty_list_case():
    """Testing that function returns 0 if list is empty"""
    assert find_maximal_subarray_sum([], 3) == 0


def test_all_negative_case():
    """Testing that function returns correct answer with negative only"""
    assert find_maximal_subarray_sum([-1, -2, -3, -4, -10], 4) == -1


def test_pos_neg_case():
    """Testing that returns correct with positive and negative integers"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16
