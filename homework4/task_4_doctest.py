"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    This function generates list with fizzbuzz* sequence

    * https://en.wikipedia.org/wiki/Fizz_buzz

    Doctests:
    >>> fizzbuzz(1)
    ['1']
    >>> fizzbuzz(3)
    ['1', '2', 'fizz']
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz buzz']

    """
    current = 1
    fizzbuzz_nums = []
    while len(fizzbuzz_nums) < n:
        if current % 15 == 0:
            fizzbuzz_nums.append("fizz buzz")
        elif current % 3 == 0:
            fizzbuzz_nums.append("fizz")
        elif current % 5 == 0:
            fizzbuzz_nums.append("buzz")
        else:
            fizzbuzz_nums.append(f"{current}")
        current += 1
    return fizzbuzz_nums
