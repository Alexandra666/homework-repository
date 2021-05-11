from unittest.mock import Mock

import pytest

from homework4 import task_2_mock_input
from homework4.task_2_mock_input import count_dots_on_i


def test_that_no_such_url(monkeypatch):
    """Testing that if there is no such url raise ValueError"""
    with pytest.raises(ValueError):
        count_dots_on_i("zzz")


def test_counting_mock(monkeypatch):
    request_mock = Mock()
    request_mock.get.return_value.text = "iii"
    monkeypatch.setattr(task_2_mock_input, "requests", request_mock)
    assert count_dots_on_i("xxx") == 3
