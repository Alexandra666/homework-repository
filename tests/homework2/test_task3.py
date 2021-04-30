from homework2.task3 import combinations


def positive_case_ints():
    """Testing positive case with list of integers"""
    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]


def positive_case_lists():
    """Testing positive case with lists of lists with strings"""
    assert combinations([["a"], ["b"]], [["c"], ["d"]]) == [
        [["a"], ["c"]],
        [["a"], ["d"]],
        [["b"], ["c"]],
        [["b"], ["d"]],
    ]


def negative_case():
    """Testing negative case of 2 lists of ints"""
    assert not combinations([1, 2], [3]) == 3
