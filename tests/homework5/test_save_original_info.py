from homework5.save_original_info import custom_sum


def test_save_original_info_saves_docs_of_custom_sum():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"


def test_save_original_info_saves_name_of_custom_sum():
    assert custom_sum.__name__ == "custom_sum"


def test_save_original_info_saves_decorated_func_by_printing_func_at_some_id(capsys):
    print(custom_sum.__original_func)
    captured = capsys.readouterr()
    assert captured.out.startswith("<function custom_sum at")


def test_save_original_info_saves_decorated_func_without_print():
    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == 10
