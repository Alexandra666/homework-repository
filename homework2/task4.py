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
    cache_memo = []

    def check_if_in_cache(*args, **kwargs):
        call_key = (args, kwargs)
        for key, value in cache_memo:
            if key == call_key:
                return value
        else:
            result = func(*args, **kwargs)
            cache_memo.append((call_key, result))
            return result

    return check_if_in_cache
