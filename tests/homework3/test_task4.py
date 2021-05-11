from homework3.task4 import is_armstrong


def test_is_armstrong_positive_case():
    assert is_armstrong(0)
    assert is_armstrong(1)
    assert is_armstrong(153)


def test_is_armstrong_negative_case():
    assert not is_armstrong(10)
    assert not is_armstrong(154)
