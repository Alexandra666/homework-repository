from homework2.task1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


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


def test_rarest_positive(tmp_path):
    """Testing rarest positive case"""
    d = tmp_path
    some_file = d / "test_01.txt"
    some_file.write_text("a a c , ,")
    assert get_rarest_char(str(some_file)) == "c"


def test_rarest_negative(tmp_path):
    """Testing rarest char negative case"""
    d = tmp_path
    some_file = d / "test_02.txt"
    some_file.write_text("a a b b ,")
    assert not get_rarest_char(str(some_file)) == "a"


def test_count_punctuation_positive(tmp_path):
    d = tmp_path
    some_file = d / "test_01.txt"
    some_file.write_text('a.: , ?"-)')
    assert count_punctuation_chars(str(some_file)) == 7


def test_count_punctuation_negative(tmp_path):
    d = tmp_path
    some_file = d / "test_02.txt"
    some_file.write_text("\\u00df!.#)")
    assert not count_punctuation_chars(str(some_file)) == 3


def test_count_non_ascii_positive(tmp_path):
    """Testing positive case of counting non_ascii chars"""
    d = tmp_path
    some_file = d / "test_01.txt"
    some_file.write_text("\\u00df! \\u00ab asdf")
    assert count_non_ascii_chars(str(some_file)) == 2


def test_count_non_ascii_negative(tmp_path):
    """Testing negative case of counting non ascii chars"""
    d = tmp_path
    some_file = d / "test_02.txt"
    some_file.write_text("\\u00fc! , : \\u00f6 asdf")
    assert not count_non_ascii_chars(str(some_file)) == 3


def test_common_non_ascii_positive(tmp_path):
    """Testing positive case of finding most common non_ascii"""
    d = tmp_path
    some_file = d / "test_01.txt"
    some_file.write_text("\\u00fc! , : \\u00f6 \\u00f6 asdf")
    assert get_most_common_non_ascii_char(str(some_file)) == "\u00f6"


def test_common_non_ascii_negative(tmp_path):
    d = tmp_path
    some_file = d / "test_02.txt"
    some_file.write_text("\\u00f6 \\u00f6 \\u00fc! \\u00fc \\u00fc , :\n asdf")
    assert not get_most_common_non_ascii_char(str(some_file)) == "\u00f6"
