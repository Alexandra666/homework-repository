"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator


def fizzbuzz(n: int) -> Generator[str]:
    for i in range(1, n + 1):
        yield "fizz buzz" * (i % 15 == 0) or "fizz" * (i % 3 == 0) or "buzz" * (
            i % 5 == 0
        ) or f"{i}"
