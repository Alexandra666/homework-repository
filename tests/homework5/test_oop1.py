import datetime

from homework5.oop_1 import Homework, Student, Teacher


def test_initialization_of_homework_text():
    """Testing that text of homework initializes correctly"""
    homework_1 = Homework("Test text of homework", 2)
    assert homework_1.text == "Test text of homework"


def test_initialization_of_homework_deadline():
    """Testing that deadline of homework initialize correctly"""
    homework_1 = Homework("Test text of homework", 2)
    expected = datetime.timedelta(days=2)
    assert homework_1.deadline == expected


def test_initialization_of_homework_created():
    """Testing that attribute created of homework initialize correctly"""
    homework_1 = Homework("Test text of homework", 2)
    expected = datetime.datetime.now()
    assert homework_1.created - expected < datetime.timedelta(seconds=1)


def test_is_active_of_homework_positive():
    """Testing that homework is active"""
    homework_1 = Homework("Test text of homework", 2)
    assert homework_1.is_active()


def test_negative_is_active_of_homework():
    """Testing that homework is expired"""
    homework_1 = Homework("Learn functions", 0)
    assert not homework_1.is_active()


def test_initialization_of_student_first_name():
    """Testing that first name of student initialize correctly"""
    student_1 = Student("Roman", "Petrov")
    assert student_1.first_name == "Roman"


def test_initialization_of_student_last_name():
    """Testing that last name of student initialize correctly"""
    student_1 = Student("Roman", "Petrov")
    assert student_1.last_name == "Petrov"


def test_student_do_homework_positive():
    """Testing that student do homework returns homework if it is active"""
    student_1 = Student("Roman", "Petrov")
    homework_1 = Homework("Test text of homework", 2)
    assert student_1.do_homework(homework_1) == homework_1


def test_student_do_homework_negative(capsys):
    """Testing that student do homework returns None if it is expired and prints 'You are late'"""
    student_1 = Student("Roman", "Petrov")
    homework_1 = Homework("Learn functions", 0)
    assert student_1.do_homework(homework_1) is None
    captured = capsys.readouterr()
    assert captured.out == "You are late\n"


def test_initialization_of_teacher_first_name():
    """Testing that first name of teacher initialize correctly"""
    teacher_1 = Teacher("Daniil", "Shadrin")
    assert teacher_1.first_name == "Daniil"


def test_initialization_of_teacher_last_name():
    """Testing that last name of teacher initialize correctly"""
    teacher_1 = Teacher("Daniil", "Shadrin")
    assert teacher_1.last_name == "Shadrin"


def test_teacher_create_homework():
    """Testing that teacher's create homework create instance of Homework class"""
    teacher_1 = Teacher("Daniil", "Shadrin")
    oop_homework = teacher_1.create_homework("create 2 simple classes", 5)
    assert isinstance(oop_homework, Homework)
