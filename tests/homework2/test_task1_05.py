from homework2.task1 import get_most_common_non_ascii_char


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
