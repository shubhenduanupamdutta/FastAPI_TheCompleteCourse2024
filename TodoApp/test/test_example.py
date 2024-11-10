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
    assert type("hello") is str
    assert type("world") is not int


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
