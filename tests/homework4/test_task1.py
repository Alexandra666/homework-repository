import pytest

from homework4.task_1_read_file import read_magic_number


def test_if_file_does_not_exist_raise_value_error(tmp_path):
    with pytest.raises(ValueError):
        read_magic_number(str(tmp_path))


def test_positive_minimal_border_inclusively(tmp_path):
    d = tmp_path
    some_file = d / "test_task01.txt"
    some_file.write_text("1\n lk")
    assert read_magic_number(str(some_file))


def test_positive_medium_number(tmp_path):
    d = tmp_path
    some_file = d / "test_task01.txt"
    some_file.write_text("2.99\n lk")
    assert read_magic_number(str(some_file))


def test_negative_maximal_border_exclusively(tmp_path):
    d = tmp_path
    some_file = d / "test_task01.txt"
    some_file.write_text("3\n lk")
    assert not read_magic_number(str(some_file))


def test_negative_raise_value_error_with_number_under_minimal_border(tmp_path):
    d = tmp_path
    some_file = d / "test_task01.txt"
    some_file.write_text("0.56\n lk")
    assert not read_magic_number(str(some_file))


def test_negative_raise_value_error_with_number_over_maximal_border(tmp_path):
    d = tmp_path
    some_file = d / "test_task01.txt"
    some_file.write_text("26")
    assert not read_magic_number(str(some_file))


def test_raise_value_error_when_startswith_number_between_1_and_3_endswith_string(
    tmp_path,
):
    d = tmp_path
    some_file = d / "test_task01.txt"
    some_file.write_text("2 test")
    with pytest.raises(ValueError):
        read_magic_number(str(some_file))
