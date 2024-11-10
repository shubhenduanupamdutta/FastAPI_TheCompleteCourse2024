# Testing in FastAPI

---

## What is Testing?

---

- #### It is a way for us to make sure our application is working as expected.
- #### Part of Software Development Life Cycle (SDLC) that aims to identify
  - **Bugs**
  - **Errors**
  - **Defects**
- #### Testing also makes sure that our app meets user requirements and specifications.
- #### Testing ensures software is of high quality, reliable, secure and user-friendly.

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

- ### NOTE: We will do a combination of Unit and Integration Testing in this tutorial.

---

## Pytest

---

- #### Pytest is popular testing framework in Python.
- #### It is known for simplicity, scalability and ability to handle both unit and integration testing.
- #### Top reasons for using Pytest:
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
$ pytest
```