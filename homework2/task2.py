"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    elem_set = set(inp)
    major_elem_counter = 0
    minor_elem_counter = len(inp)
    minor_elem = 0
    major_elem = 0
    for element in elem_set:
        if inp.count(element) > major_elem_counter:
            major_elem = element
            major_elem_counter = inp.count(element)
        if inp.count(element) < minor_elem_counter:
            minor_elem = element
            minor_elem_counter = inp.count(element)
    return major_elem, minor_elem
