"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """You are late"""


class HomeworkRepeatError(Exception):
    """This homework result was already accepted"""


class Homework:
    """This is a class which contains homework description
        and the number of days given to complete the task
        with checking expiration of deadline.
    :param text: Description of homework
    :type text: str
    :param deadline_days: The number of days given to complete the task
    :type deadline_days: int
    """

    def __init__(self, text: str, deadline_days: int):
        """Constructor method"""
        self.text = text
        self.deadline_days = datetime.timedelta(days=deadline_days)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """This function checks whether homework deadline is active or expired
        :return: `True` if homework is active (deadline not expired) `False` otherwise
        :rtype: bool
        """
        return self.created + self.deadline_days > datetime.datetime.now()


class HomeworkResult:
    """Class which characterizes result of done homework.
    :param author: object of type 'Student'
    :type author: Student
    :param homework: object Homework
    :type homework: Homework
    :param solution: The solution of given homework.
    :type solution: str
    """

    def __init__(self, author: "Student", homework: "Homework", solution: str):
        """Constructor method"""
        self.author = author
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise TypeError("You gave a not Homework object")
        self.solution = solution
        self.created = datetime.datetime.now()


class Human:
    """Class which characterizes all people, who have first and last name.
    :param first_name: First name of a human
    :type first_name: str
    :param last_name: Last name of a human
    :type last_name: str
    """

    def __init__(self, first_name: str, last_name: str):
        """Constructor method"""
        self.last_name = last_name
        self.first_name = first_name


class Student(Human):
    """This is a class which contains full name of a student
        and allows to create solution of homework.
    :param first_name: First name of a student
    :type first_name: str
    :param last_name: Last name of a student
    :type last_name: str
    """

    def do_homework(self, homework: "Homework", solution: str) -> "HomeworkResult":
        """This function returns homework expired or not.
        :param homework: object with homework description
            and number of days given to complete the task
        :type homework: Homework
        :param solution: Solution of homework
        :type solution: str
        :return: HomeworkResult if homework is active.
            raises DeadlineError otherwise.
        :rtype: HomeworkResult
        """
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError


class Teacher(Human):
    """Class which contains full name of a teacher,
        allows to create some homework, check homework and reset results of done homework .
    :param first_name: First name of a teacher
    :type first_name: str
    :param last_name: Last name of a teacher
    :type last_name: str
    """

    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text: str, deadline_days: int) -> "Homework":
        """This function creates homework with text and deadline days given
        :param text: Description of the homework
        :type text: str
        :param deadline_days: The number of days given to complete the task
        :type deadline_days: int
        :return: homework
        :rtype: Homework
        """
        return Homework(text, deadline_days)

    @classmethod
    def check_homework(cls, homework_result: "HomeworkResult") -> bool:
        """This function accepts some homework result and checks whether it is
            unique and satisfies all conditions.
        :param homework_result: the result of done homework
        :type homework_result: HomeworkResult
        :return True if length of solution > 5 False otherwise.
            raises TypeError if homework_result is not an object of type HomeworkResult,
            raises HomeworkRepeatError if this solution for this homework was already submitted.
        :rtype: bool
        """
        if not isinstance(homework_result, HomeworkResult):
            raise TypeError("You gave a not HomeworkResult object")
        if homework_result in cls.homework_done[homework_result.homework]:
            raise HomeworkRepeatError
        if len(homework_result.solution) > 5:
            cls.homework_done[homework_result.homework].append(homework_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        """This function allows to remove all results if there is no args
            and remove all results of some homework, if homework is accepted as argument.
        :param homework: object of type Homework
        :type homework: Homework, optional
        :return: None
        """
        if homework and isinstance(homework, Homework):
            del cls.homework_done[homework]
        else:
            cls.homework_done.clear()
