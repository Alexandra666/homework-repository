import datetime

from homework5.oop_1 import Homework, Student, Teacher

homework_1 = Homework("Test text of homework", 2)
homework_2 = Homework("Learn functions", 0)
student_1 = Student("Roman", "Petrov")
teacher_1 = Teacher("Daniil", "Shadrin")


def test_initialization_of_homework_text():
    """Testing that text of homework initializes correctly"""
    assert homework_1.text == "Test text of homework"


def test_initialization_of_homework_deadline():
    """Testing that deadline of homework initializes correctly"""
    expected = datetime.timedelta(days=2)
    assert homework_1.deadline_days == expected


def test_initialization_of_homework_created():
    """Testing that attribute created of homework initializes correctly"""
    expected = datetime.datetime.now()
    assert homework_1.created - expected < datetime.timedelta(seconds=1)


def test_is_active_of_homework_positive():
    """Testing that homework is active"""
    assert homework_1.is_active()


def test_negative_is_active_of_homework():
    """Testing that homework is expired"""
    assert not homework_2.is_active()


def test_initialization_of_student_first_name():
    """Testing that first name of student initializes correctly"""
    assert student_1.first_name == "Roman"


def test_initialization_of_student_last_name():
    """Testing that last name of student initializes correctly"""
    assert student_1.last_name == "Petrov"


def test_student_do_homework_positive():
    """Testing that student do homework returns homework if it is active"""
    assert student_1.do_homework(homework_1) == homework_1


def test_student_do_homework_negative(capsys):
    """Testing that student do homework returns None if it is expired and prints 'You are late'"""
    assert student_1.do_homework(homework_2) is None
    captured = capsys.readouterr()
    assert captured.out == "You are late\n"


def test_initialization_of_teacher_first_name():
    """Testing that first name of teacher initializes correctly"""
    assert teacher_1.first_name == "Daniil"


def test_initialization_of_teacher_last_name():
    """Testing that last name of teacher initializes correctly"""
    assert teacher_1.last_name == "Shadrin"


def test_teacher_create_homework():
    """Testing that teacher's create homework creates instance of Homework class"""
    oop_homework = teacher_1.create_homework("create 2 simple classes", 5)
    assert isinstance(oop_homework, Homework)
