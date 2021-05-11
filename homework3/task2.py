"""
Here's a not very efficient calculation function that calculates something important::


Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.

"""
import hashlib
import random
import struct
import time
from multiprocessing import Pool
from typing import Callable


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def fast_sum(func: Callable, num: float):
    with Pool(60) as p:
        return sum(p.map(func, range(num)))


if __name__ == "__main__":
    print(fast_sum(slow_calculate, 501))
