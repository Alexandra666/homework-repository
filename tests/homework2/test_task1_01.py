from homework2.task1 import get_longest_diverse_words


def test_longest_diverse_positive_case_11_words_with_unicode_and_transpositions(
    tmp_path,
):
    """Testing that function returns 10 longest words in text with unicode symbols and word transpositions"""
    d = tmp_path
    some_file = d / "test_01.txt"
    some_file.write_text(
        "a, bc, de-\n"
        "fg - passs! lmnop \n"
        "qrstuv wxyzabc \n"
        "defghijk l\\u00dfnopqrst\n"
        "kalam azazazaazaz\n"
        "\n"
    )
    assert get_longest_diverse_words(str(some_file)) == [
        "lßnopqrst",
        "defghijk",
        "wxyzabc",
        "qrstuv",
        "lmnop",
        "kalam",
        "passs",
        "defg",
        "azazazaazaz",
        "bc",
    ]


def test_longest_diverse_positive_3_words(tmp_path):
    """Testing that returns list sorted by length and unique symbols"""
    d = tmp_path
    some_file = d / "test_02.txt"
    some_file.write_text("ab\ncdef\nklmno-\np\n")
    assert get_longest_diverse_words(str(some_file)) == ["klmnop", "cdef", "ab"]


def test_longest_diverse_negative_not_only_length(tmp_path):
    """Testing that returns not only longest words"""
    d = tmp_path
    some_file = d / "test_03.txt"
    some_file.write_text(
        "a\n"
        "bc cc ddd fgh\n"
        "hhhh klmn\n"
        "opqrs\n"
        "opqrtu\n"
        "qrstuvw\n"
        "ooooooob\n"
    )
    assert not get_longest_diverse_words(str(some_file)) == [
        "ooooooob",
        "qrstuvw",
        "opqrtu",
        "opqrs",
        "klmn",
        "hhhh",
        "ddd",
        "fgh",
        "bc",
        "cc",
    ]
