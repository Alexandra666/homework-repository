from homework4.task_3_get_print_output import my_precious_logger


def test_positive_stderr(capsys):
    """Testing that if string starts with error output in stderr"""
    my_precious_logger("error - this should be in stderr")
    captured = capsys.readouterr()
    assert captured.err == "error - this should be in stderr"


def test_positive_stdout(capsys):
    """Testing that if string starts not with error output in stdout (or print)"""
    my_precious_logger("everything's OK")
    captured = capsys.readouterr()
    assert captured.out == "everything's OK"
