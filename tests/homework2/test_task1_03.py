from homework2.task1 import count_punctuation_chars


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
