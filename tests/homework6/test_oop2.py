import pytest

from homework6.oop_2 import *

opp_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")

expired_hw = opp_teacher.create_homework("Learn functions", 0)
oop_hw = opp_teacher.create_homework("Learn OOP", 1)
docs_hw = opp_teacher.create_homework("Read docs", 5)

result_1 = good_student.do_homework(oop_hw, "I have done this hw")
result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
result_3 = lazy_student.do_homework(docs_hw, "done")

# initialization testing


def test_initialization_of_homework_text():
    """Testing that text of homework initializes correctly"""
    assert oop_hw.text == "Learn OOP"


def test_initialization_of_homework_deadline():
    """Testing that deadline of homework initializes correctly"""
    expected = datetime.timedelta(days=1)
    assert oop_hw.deadline_days == expected


def test_initialization_of_homework_created():
    """Testing that attribute created of homework initializes correctly"""
    expected = datetime.datetime.now()
    assert oop_hw.created - expected < datetime.timedelta(seconds=1)


def test_initialization_of_student_first_name():
    """Testing that first name of student initializes correctly"""
    assert lazy_student.first_name == "Roman"


def test_initialization_of_student_last_name():
    """Testing that last name of student initializes correctly"""
    assert lazy_student.last_name == "Petrov"


def test_initialization_of_teacher_first_name():
    """Testing that first name of teacher initializes correctly"""
    assert opp_teacher.first_name == "Daniil"


def test_initialization_of_teacher_last_name():
    """Testing that last name of teacher initializes correctly"""
    assert opp_teacher.last_name == "Shadrin"


def test_initialization_of_homework_result_author():
    """Testing that author of homework result initializes correctly"""
    assert result_1.author == good_student


def test_initialization_of_homework_result_homework():
    """Testing that homework of homework result initializes correctly"""
    assert result_1.homework == oop_hw


def test_initialization_of_homework_result_solution():
    """Testing that homework of homework result initializes correctly"""
    assert result_1.solution == "I have done this hw"


def test_initialization_homework_result_homework_negative():
    """Testing that if homework as arg is not a Homework object raises TypeError"""
    with pytest.raises(TypeError):
        lazy_student.do_homework("oop_hw", "done this")


def test_initialization_of_homework_result_created():
    """Testing that attribute created of homework result initializes correctly"""
    expected = datetime.datetime.now()
    assert result_1.created - expected < datetime.timedelta(seconds=1)


# functions testing


def test_is_active_of_homework_positive():
    """Testing that homework is active"""
    assert oop_hw.is_active()


def test_negative_is_active_of_homework():
    """Testing that homework is expired"""
    assert not expired_hw.is_active()


def test_student_do_homework_positive():
    """Testing that student do homework returns homework result if it is active"""
    assert isinstance(result_1, HomeworkResult)


def test_student_do_homework_raise_deadline_error_if_expired():
    """Testing that student do homework raises DeadlineError if homework is expired"""
    with pytest.raises(DeadlineError):
        lazy_student.do_homework(expired_hw, "done")


def test_that_class_teacher_attribute_homework_done_is_the_same_with_instance_of_this_class():
    """Testing that homework_done of Teacher is the same object as homework_done of some instance of this class"""
    temp_1 = opp_teacher.homework_done
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2


def test_teacher_create_homework():
    """Testing that teacher's create homework creates instance of Homework class"""
    assert isinstance(oop_hw, Homework)


def test_teacher_check_homework_raises_type_error_if_not_a_homework_result_instance():
    """Testing that if homework_result is not a HomeworkResult object"""
    with pytest.raises(TypeError):
        opp_teacher.check_homework("done this")


def test_teacher_check_homework_positive():
    """Testing that check_homework returns true if solution is good"""
    assert opp_teacher.check_homework(result_1)


def test_teacher_reset_result_with_arg_positive():
    """Testing that if reset result with arg
    solutions of this homework are removed from dict with solutions"""
    expected = []
    Teacher.reset_results(oop_hw)
    assert Teacher.homework_done[oop_hw] == expected


def test_teacher_check_homework_raises_homework_repeat_error_if_same_solution_was_already_submitted():
    """Testing that check_homework raises HomeworkRepeatError
    if this solution for this homework was already submitted"""
    with pytest.raises(HomeworkRepeatError):
        opp_teacher.check_homework(result_1)
        advanced_python_teacher.check_homework(result_1)
    Teacher.reset_results(oop_hw)


def test_teacher_check_homework_negative_if_solution_is_not_ok():
    """Testing that if solution do not satisfies condition more than 5 symbols returns False"""
    assert not opp_teacher.check_homework(result_3)


def test_teacher_reset_results_without_arg_positive():
    """Testing that reset_results without arg removes all solutions from dict with solutions"""
    opp_teacher.check_homework(result_1)
    opp_teacher.check_homework(result_2)
    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0
