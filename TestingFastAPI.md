# Testing in FastAPI

---

## What is Testing?

---

- #### It is a way for us to make sure our application is working as expected

- #### Part of Software Development Life Cycle (SDLC) that aims to identify

  - **Bugs**
  - **Errors**
  - **Defects**

- #### Testing also makes sure that our app meets user requirements and specifications

- #### Testing ensures software is of high quality, reliable, secure and user-friendly

---

## What are the types of Testing?

---

- #### Manual Testing

  - _Easiest one to understand and perform, we have already done this in our previous projects._
  - _Involves a person manually testing the software for defects by following a set of test cases._
  - _Testers act as end-users and test the software to ensure it is working as expected._

- #### Unit Testing

  - _Involves testing individual components or units of software in isolation from rest of the application._
  - _Validates that each unit of software performs as designed._
  - _**Unit = Smallest testable part of an application**_
  - _Developers write unit tests during the development phase._
  - _These tests are automated and executed by a testing framework. Python has `unittest` and `pytest`._
  - _Benefit is to identify bugs early in the development phase._

- #### Integration Testing

  - _Involves testing the integration of different components or units of software._
  - _Validates that the software works as expected when integrated together._
  - _Focuses on testing the interactions between different components of the piece of software._
  - _The scope is broader than unit testing, as we are testing multiple units together._
  - _Helps identify problems for the entire system/solution._
  - _**Example: Call and API endpoint and make sure the correct data is returned.**_

- ### NOTE: We will do a combination of Unit and Integration Testing in this tutorial

---

## Pytest

---

- #### Pytest is popular testing framework in Python

- #### It is known for simplicity, scalability and ability to handle both unit and integration testing

- #### Top reasons for using Pytest

  - _**Simple & Flexible -** Native Assertions_
  - _**Fixtures -** Setup and teardown of test data_
  - _**Parameterization -** Run the same test with different inputs_

---

## Getting started with Testing in FastAPI

---

### First Step

- **Create a new directory on our project call `test`**
- **Inside our test directory create a new file called `_init_.py`**
- **This file is required to make Python treat the directory as a package.**
- **Inside the `test` directory create a new file called `test_example.py`**

### `test_example.py`

- **Pytest will run all tests automatically that sit within files that start with `test_`**
- **For our demo, all tests will be in `test_example.py` so pytest can find them and run them.**
- **When we write tests for our application, we will create new tests from a new file that matches naming convention of project.**
- Example: `todo.py` will be tested in `test_todo.py`

### Create our first unit test

- **Write our first assertion test.**
  - _Assertion = Statement that checks if a condition is true._
  - _If the condition is true, the test passes._
  - _If the condition is false, the test fails._
- **In `test_example.py` write the following code:**

```python
def test_equal_or_not():
    assert 1 == 1
```

- **Run the test by typing `pytest` in the terminal.**

```bash
pytest
```

---

## Pytest Basics

---

- #### Validate Integers

```python
def test_equal():
    assert 1 == 1
```

- #### Validate Instances

```python
def test_instance():
    assert isinstance(1, int)
    assert not isinstance(1, str)
```

- #### Validate Booleans

```python
def test_boolean():
    validated: True
    assert validated is True
    assert ('hello' == 'world') is False
```

- #### Validate Types

```python
def test_type():
    assert type("Hello") is str
    assert type("World") is not int
```

- #### Validate Greater and Less Than

```python
def test_greater_and_less_than():
    assert 10 > 5
    assert 5 < 10
```

- #### Validate Lists

```python
def test_list():
    num_list = [1, 2, 3, 4, 5]
    any_list = [False, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)
```

---

## Pytest Objects

---

- #### We can create our Pytest objects to test our FastAPI application

```python
class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years
```

- #### Suppose we have a `Student` class as shown above

- #### We can create a test to validate the object

```python
def test_person_initialization():
    p = Student("John", "Doe", "Computer Science", 3)
    assert p.first_name == "John", "First Name should be John"
    assert p.last_name == "Doe", "Last Name should be Doe"
    assert p.major == "Computer Science"
    assert p.years == 3
```

- #### If we have to create a new object for every single function, every time, that will take a lot of time

- #### Pytest allows us to be able to use reusability on some items by calling something called `Fixture`

- #### For `Fixture` we create a function that will return the object we want to test

```python
@pytest.fixture
def default_student():
    return Student("John", "Doe", "Computer Science", 3)

def test_person_initialization(default_student):
    assert default_student.first_name == "John", "First Name should be John"
    assert default_student.last_name == "Doe", "Last Name should be Doe"
    assert default_student.major == "Computer Science"
    assert default_student.years == 3
```

---

## Test Database

---

- #### Create a fake/test database to store data

- #### Create testing dependencies that are separate from our production dependency

- #### This way we can do integration testing to make sure our entire project is working correctly when we run our tests

- #### App is live = Production Dependency

- #### App is in testing = Testing Dependency

---

## Testing Dependencies

---

- #### Create a new file called `test_todo.py` in the `test` directory, which will test our `todo.py` file

- #### Create a new database engine for our testing environment

```python
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)
```

- #### Create a new `SessionLocal` for our testing environment

```python
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
```

- #### Setup `get_testing_db` dependency and override `get_db` dependency

```python
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
app.dependency_overrides[get_db] = override_get_db
```

- #### Mock our current logged in user for testing

```python
def override_get_current_user():
    return {"username": "shubhenduanupam", "id": 1, "user_role": "admin"}
app.dependency_overrides[get_current_user] = override_get_current_user
```

- #### Create a new `client` for our testing environment

```python
client = TestClient(app)
```
