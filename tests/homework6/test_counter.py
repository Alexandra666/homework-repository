from homework6.counter import User


def test_counter_get_created_instances_without_instances():
    """Testing that get_created_instances returns 0 if there was no instances yet"""
    assert User.get_created_instances() == 0


def test_counter_get_created_instances_with_3_instances_class_and_instance_are_the_same():
    """Testing that get_created_instances with 3 instances returns 3"""
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3


def test_class_and_instance_have_same_counter():
    """Testing that class and its instance have the same counter"""
    assert User.reset_instances_counter() == 3
    assert User.get_created_instances() == 0
