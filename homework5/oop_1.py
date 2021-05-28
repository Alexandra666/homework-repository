"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


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


class Student:
    """This is a class which contains full name of a student
        and allows to check deadline expiration of some homework.


    :param first_name: First name of a student
    :type first_name: str
    :param last_name: Last name of a student
    :type last_name: str
    """

    def __init__(self, first_name: str, last_name: str):
        """Constructor method"""
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework: Homework) -> Homework:
        """This function returns homework expired or not.

        :param homework: object with homework description
            and number of days given to complete the task
        :type homework: Homework
        :return: homework if homework is active and None otherwise.
            In the latter case prints 'You are late!'
        :rtype: Homework
        """
        if homework.is_active():
            return homework
        print("You are late")


class Teacher:
    """This is a class which contains full name of a teacher
        and allows to create some homework.


    :param first_name: First name of a teacher
    :type first_name: str
    :param last_name: Last name of a teacher
    :type last_name: str
    """

    def __init__(self, first_name: str, last_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text: str, deadline_days: int) -> Homework:
        """This function creates homework with text and deadline days given

        :param text: Description of the homework
        :type text: str
        :param deadline_days: The number of days given to complete the task
        :type deadline_days: int
        :return: homework
        :rtype: Homework
        """
        return Homework(text, deadline_days)
