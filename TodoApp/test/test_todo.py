# ruff: noqa: F401, F811

from fastapi import status

from ..app.models import Todo
from .utils import TestingSessionLocal, client, test_todo


def test_read_all_authenticated(test_todo):
    response = client.get("/todo")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "complete": False,
            "title": "Learn to code.",
            "description": "I want to learn to code in Python.",
            "id": 1,
            "priority": 5,
            "owner_id": 1,
        }
    ]


def test_read_one_authenticated(test_todo):
    response = client.get("/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "complete": False,
        "title": "Learn to code.",
        "description": "I want to learn to code in Python.",
        "id": 1,
        "priority": 5,
        "owner_id": 1,
    }


def test_read_one_authenticated_not_found():
    response = client.get("/todo/99")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}


def test_create_todo(test_todo):
    request_data = {
        "title": "New Todo!",
        "description": "This is a new todo.",
        "priority": 1,
        "complete": False,
    }

    response = client.post("/todo", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED
    request_data.update({"id": 2, "owner_id": 1})
    assert response.json() == request_data

    db = TestingSessionLocal()
    todo = db.query(Todo).filter(Todo.id == 2).first()
    assert todo.title == request_data.get("title")  # type: ignore
    assert todo.description == request_data.get("description")  # type: ignore
    assert todo.priority == request_data.get("priority")  # type: ignore
    assert todo.complete == request_data.get("complete")  # type: ignore
    assert todo.owner_id == request_data.get("owner_id")  # type: ignore
    assert todo.id == request_data.get("id")  # type: ignore


def test_update_todo(test_todo):
    request_data = {
        "title": "Change the title",
        "description": "Change the description",
        "priority": 1,
        "complete": True,
    }
    response = client.put("/todo/1", json=request_data)
    request_data.update({"id": 1, "owner_id": 1})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == request_data

    db = TestingSessionLocal()
    todo = db.query(Todo).filter(Todo.id == 1).first()
    assert todo.title == request_data.get("title")  # type: ignore
    assert todo.description == request_data.get("description")  # type: ignore
    assert todo.priority == request_data.get("priority")  # type: ignore
    assert todo.complete == request_data.get("complete")  # type: ignore
    assert todo.owner_id == request_data.get("owner_id")  # type: ignore
    assert todo.id == request_data.get("id")  # type: ignore


def test_update_todo_not_found(test_todo):
    request_data = {
        "title": "Change the title",
        "description": "Change the description",
        "priority": 1,
        "complete": True,
    }
    response = client.put("/todo/99", json=request_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}


def test_delete_todo(test_todo):
    response = client.delete("/todo/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    model = db.query(Todo).filter(Todo.id == 1).first()
    assert model is None


def test_delete_todo_not_found():
    response = client.delete("/todo/99")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}
