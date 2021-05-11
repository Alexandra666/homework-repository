import pytest

from homework3.task3 import Filter, make_filter


def test_filter_takes_all_args():
    """Testing that all functions are accepted as arguments of Filter object"""

    def func_1(a):
        return a % 2

    def func_2(a):
        return a > 0

    def func_3(a):
        return isinstance(a, int)

    filter_obj = Filter(func_1, func_2, func_3)
    args = (func_1, func_2, func_3)
    assert filter_obj.functions == args


def test_positive_case_filter_returns_all_positive_even_numbers():
    filter_obj = Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    assert filter_obj.apply(range(10)) == [2, 4, 6, 8]


def test_make_filter_positive_case():
    """Testing that make_filter Filter object with all functions"""
    filter_obj = make_filter(
        k1="v1",
    )
    result = filter_obj.apply(
        [{"k1": "v1", "k2": "v2"}, {"k1": "v2", "k2": "v3", "k5": "v6"}]
    )
    expected = [{"k1": "v1", "k2": "v2"}]
    assert result == expected


def test_make_filter_when_argument_has_no_such_key():
    filter_obj = make_filter(k1="v1", k2="v2")
    with pytest.raises(KeyError, match="k2"):
        filter_obj.apply([{"k1": "v1", "k3": "v3"}])


def test_make_filter_with_wrong_values():
    filter_obj = make_filter(k1="v1", k2="v2")
    result = filter_obj.apply(
        [
            {"k1": "v1", "k2": "v3"},
            {"k1": "v1", "k2": "v3", "k3": "v3"},
        ]
    )
    assert result == []


def test_make_filter_take_one_from_list():
    filter_obj = make_filter(k1="v1", k2="v2")
    result = filter_obj.apply(
        [
            {"k1": "v1", "k2": "v2", "k3": "v3"},
            {"k1": "v1", "k2": "v3", "k3": "v3"},
            {"k1": "v1", "k2": "v3", "k3": "v3"},
        ]
    )
    expected = [{"k1": "v1", "k2": "v2", "k3": "v3"}]
    assert result == expected
