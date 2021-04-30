from homework2.task1 import get_rarest_char


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
