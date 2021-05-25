"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    cls.counter = 0

    def get_created_instances():
        """This function returns number of created instances of decorated class

        :return: number of created instances
        :rtype: int
        """
        return cls.counter

    def reset_instances_counter():
        """This function returns number of created instances of decorated class
        and reset it to zero

        :return: number of created instances and nullifies it afterwards
        :rtype: int
        """
        result = cls.counter
        cls.counter = 0
        return result

    original_init = cls.__init__
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    def __init__(self, *args, **kwargs):
        """This constructor uses original init function and defines instances counter"""
        cls.counter += 1
        self.get_created_instances = get_created_instances
        self.reset_instances_counter = reset_instances_counter
        original_init(self, *args, **kwargs)

    cls.__init__ = __init__
    return cls


@instances_counter
class User:
    pass
