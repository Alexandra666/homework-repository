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
from typing import Iterator


def fizzbuzz(n: int) -> Iterator[str]:
    for num in range(1, n + 1):
        yield "fizz buzz" * (num % 15 == 0) or "fizz" * (num % 3 == 0) or "buzz" * (
            num % 5 == 0
        ) or f"{num}"
