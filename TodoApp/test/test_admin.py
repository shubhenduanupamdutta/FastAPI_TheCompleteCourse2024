# ruff: noqa: F401, F811

from fastapi import status

from ..app.models import Todo
from .utils import TestingSessionLocal, client, test_todo


def test_admin_read_all_authenticated(test_todo):
    response = client.get("/admin/todo")
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


def test_admin_delete_todo(test_todo):
    response = client.delete("/admin/todo/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    todo = db.query(Todo).filter(Todo.id == 1).first()
    assert todo is None


def test_admin_delete_todo_not_found():
    response = client.delete("/admin/todo/99")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}
