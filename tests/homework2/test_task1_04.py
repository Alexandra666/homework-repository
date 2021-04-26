from homework2.task1 import count_non_ascii_chars


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
