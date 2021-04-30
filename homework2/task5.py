"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""

from typing import Any, Iterable, List


def custom_range(
    some_iterable: Iterable[Any], start=None, end=None, step=None
) -> List[Any]:
    result = []
    if start and not end:
        for element in some_iterable:
            if element != start:
                result.append(element)
            else:
                return result
    if start and end and not step:
        ind = 0
        while ind < len(some_iterable):
            if some_iterable[ind] == start:
                while some_iterable[ind] != end:
                    result.append(some_iterable[ind])
                    ind += 1
            else:
                ind += 1
        return result
    if end and start and step:
        ind = 0
        while ind < len(some_iterable):
            if some_iterable[ind] == start:
                ind_start = ind
                while some_iterable[ind] != end:
                    if step < 0:
                        ind -= 1
                    else:
                        ind += 1
                ind_end = ind
                return list(some_iterable[ind_start:ind_end:step])
            else:
                ind += 1
    else:
        return list(some_iterable)
