"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import unicodedata
from collections import namedtuple
from typing import List

Token = namedtuple("Token", ["type", "value"])


def tokenize(some_file):
    word = ""
    symbol = some_file.read(1)
    while symbol:
        if unicodedata.category(symbol).startswith("L"):
            word += symbol
            yield Token("symbol", symbol)
            symbol = some_file.read(1)
            if symbol == "-":
                some_file.read(1)
                symbol = some_file.read(1)
            continue
        if word:
            yield Token("word", word)
            word = ""
        if unicodedata.category(symbol).startswith("P"):
            yield Token("punctuation", symbol)
        symbol = some_file.read(1)


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, encoding="unicode-escape", errors="ignore") as fi:
        longest_unique = []
        for token in tokenize(fi):
            if token.type == "word":
                longest_unique.append(token.value)
    longest_unique = sorted(
        longest_unique, key=lambda word: len(set(word)), reverse=True
    )
    for ind in range(len(longest_unique) - 1):
        if len(longest_unique[ind]) < len(longest_unique[ind + 1]):
            longest_unique[ind], longest_unique[ind + 1] = (
                longest_unique[ind + 1],
                longest_unique[ind],
            )
    return longest_unique[:10]


def get_rarest_char(file_path: str) -> str:
    with open(file_path, encoding="unicode-escape", errors="ignore") as fi:
        set_of_symbols = set()
        list_of_symbols = []
        for token in tokenize(fi):
            if token.type != "word":
                set_of_symbols.add(token.value)
                list_of_symbols.append(token.value)
        occur_min = len(list_of_symbols)
        for symbol in set_of_symbols:
            occur_num = list_of_symbols.count(symbol)
            if occur_num < occur_min:
                occur_min = occur_num
                rarest = symbol
    return rarest


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode-escape", errors="ignore") as fi:
        punctuation_counter = 0
        for token in tokenize(fi):
            if token.type == "punctuation":
                punctuation_counter += 1
    return punctuation_counter


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode-escape", errors="ignore") as fi:
        non_ascii_counter = 0
        for token in tokenize(fi):
            if token.type != "word":
                if not token.value.isascii():
                    non_ascii_counter += 1
    return non_ascii_counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, encoding="unicode-escape", errors="ignore") as fi:
        list_of_non_ascii = []
        set_of_non_ascii = set()
        for token in tokenize(fi):
            if token.type == "symbol":
                if not token.value.isascii():
                    list_of_non_ascii.append(token.value)
                    set_of_non_ascii.add(token.value)
    occur_max = 0
    common_non_ascii = ""
    for symbol in set_of_non_ascii:
        occur_num = list_of_non_ascii.count(symbol)
        if occur_num > occur_max:
            occur_max = occur_num
            common_non_ascii = symbol
    return common_non_ascii
