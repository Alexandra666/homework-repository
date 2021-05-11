import time

from homework3 import task2
from homework3.task2 import fast_sum, slow_calculate


def test_slow_calculate_500_time():
    start_time = time.time()
    fast_sum(slow_calculate, 501)
    assert time.time() - start_time <= 60


def return_1(arg):
    """This function is for monkey patching"""
    return 1


def test_slow_calculate_501(monkeypatch):

    monkeypatch.setattr(task2, "slow_calculate", return_1)
    assert fast_sum(task2.slow_calculate, 501) == 501
