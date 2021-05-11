from unittest.mock import Mock, call

from homework3.task1 import cache


def test_cached_1_times():
    """Testing that function is called 1 time instead of 2 when it is cached"""
    mock = Mock()
    cached_func = cache(times=1)(mock)
    cached_func(0, 1)
    cached_func(0, 1)
    assert mock.mock_calls == [call(0, 1)]


def test_not_cached_with_different_args():
    """Testing that with cache works with different args"""
    mock = Mock()
    cached_func = cache(times=1)(mock)
    cached_func(0, 1)
    cached_func(1, 2)
    cached_func(0, 1)
    cached_func(1, 2)
    assert mock.mock_calls == [call(0, 1), call(1, 2)]


def test_not_cached_with_2_times():
    """Testing that with cache works with times = 2"""
    mock = Mock()
    cached_func = cache(times=2)(mock)
    cached_func(0, 1)
    cached_func(0, 1)
    cached_func(0, 1)
    assert mock.mock_calls == [call(0, 1)]
