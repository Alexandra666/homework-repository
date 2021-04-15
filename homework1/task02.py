"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    data_to_consider = sorted(data)
    if len(data_to_consider) < 3:
        print("This sequence is less than 3 elements")
        return False
    elif len(data_to_consider) == 3:
        return data_to_consider[0] + data_to_consider[1] == data_to_consider[2]
    if data_to_consider[0] + data_to_consider[1] == data_to_consider[2]:
        return check_fibonacci(data_to_consider[1:])
