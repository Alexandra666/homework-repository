from homework2.task4 import cache


def test_positive_case():
    """Testing that 2 calls of function are 1 object in memory"""

    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
