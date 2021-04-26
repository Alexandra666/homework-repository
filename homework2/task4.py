"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_memo = {}

    def check_if_in_cache(*args):
        if args in cache_memo:
            return cache_memo[args]
        else:
            result = func(*args)
            cache_memo[args] = result
            return result

    return check_if_in_cache
