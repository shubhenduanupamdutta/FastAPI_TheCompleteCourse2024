import pytest


def test_equal_or_not():
    assert 3 == 3
    assert 3 != 4


def test_instance():
    assert isinstance(3, int)
    assert isinstance(3.0, float)
    assert isinstance("3", str)
    assert not isinstance(3, str)


def test_boolean():
    validated = True
    assert validated is True
    assert ("hello" == "world") is False


def test_type():
    assert type("hello") is str  # noqa: E721
    assert type("world") is not int  # noqa: E721


def test_greater_and_less_than():
    assert 10 > 5
    assert 5 < 10


def test_list():
    num_list = [1, 2, 3, 4, 5]
    any_list = [False, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)


class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years


def test_person_initialization():
    p = Student("John", "Doe", "Computer Science", 3)
    assert p.first_name == "John", "First name should be John"
    assert p.last_name == "Doe", "Last name should be Doe"
    assert p.major == "Computer Science"
    assert p.years == 3


@pytest.fixture
def default_employee():
    return Student("John", "Doe", "Computer Science", 3)


def test_person_init_using_fixture(default_employee):
    assert default_employee.first_name == "John", "First name should be John"
    assert default_employee.last_name == "Doe", "Last name should be Doe"
    assert default_employee.major == "Computer Science"
    assert default_employee.years == 3
