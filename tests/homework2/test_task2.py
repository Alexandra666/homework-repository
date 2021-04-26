from homework2.task2 import major_and_minor_elem


def test_positive_3_elements():
    """Testing boundary condition with 3 elements"""
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)


def test_positive_more_elements():
    """Testing with >3 elements"""
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_negative_case():
    """Testing negative case"""
    assert not major_and_minor_elem([5, 5, 2, 2, 2]) == (5, 2)
