import pytest
from fastapi import status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..app.models import Todo

pytestmark = pytest.mark.anyio


async def test_read_all_authenticated(client):
    response = await client.get("/todo/")
    response_data = response.json()
    assert response.status_code == status.HTTP_200_OK
    # Admin only has two todos
    assert len(response_data) == 2
    assert response_data == [
        {
            "title": "Test Todo 1",
            "owner_id": 1,
            "complete": False,
            "id": 1,
            "description": "This is a test todo 1",
            "priority": 1,
        },
        {
            "title": "Learn FastAPI",
            "owner_id": 1,
            "complete": False,
            "id": 3,
            "description": "Learn FastAPI from docs",
            "priority": 1,
        },
    ]


async def test_read_one_authenticated(client):
    response = await client.get("/todo/1")
    response_data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_data["owner_id"] == 1
    assert response_data == {
        "title": "Test Todo 1",
        "owner_id": 1,
        "complete": False,
        "id": 1,
        "priority": 1,
        "description": "This is a test todo 1",
    }


async def test_read_one_authenticated_not_found(client):
    response = await client.get("/todo/99")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}


async def test_create_todo(client, session: AsyncSession):
    request_data = {
        "title": "New Todo!",
        "description": "This is a new todo.",
        "priority": 1,
        "complete": False,
    }

    response = await client.post("/todo/", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED
    request_data.update({"owner_id": 1})
    assert response.json() == request_data

    result = await session.execute(select(Todo).filter(Todo.id == 5))
    todo = result.scalar_one()
    assert todo.title == request_data.get("title")  # type: ignore
    assert todo.description == request_data.get("description")  # type: ignore
    assert todo.priority == request_data.get("priority")  # type: ignore
    assert todo.complete == request_data.get("complete")  # type: ignore
    assert todo.owner_id == request_data.get("owner_id")  # type: ignore


async def test_update_todo(client, session: AsyncSession):
    request_data = {
        "title": "Change the title",
        "description": "Change the description",
        "priority": 1,
        "complete": True,
    }
    response = await client.put("/todo/3", json=request_data)
    request_data.update({"id": 5, "owner_id": 1})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == request_data

    todo = await session.execute(select(Todo).filter(Todo.id == 5))
    todo = todo.scalar_one()
    assert todo.title == request_data.get("title")  # type: ignore
    assert todo.description == request_data.get("description")  # type: ignore
    assert todo.priority == request_data.get("priority")  # type: ignore
    assert todo.complete == request_data.get("complete")  # type: ignore
    assert todo.owner_id == request_data.get("owner_id")  # type: ignore
    assert todo.id == request_data.get("id")  # type: ignore


async def test_update_todo_not_found(client):
    request_data = {
        "title": "Change the title",
        "description": "Change the description",
        "priority": 1,
        "complete": True,
    }
    response = await client.put("/todo/99", json=request_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}


async def test_delete_todo(client, session: AsyncSession):
    response = await client.delete("/todo/2")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    result = await session.execute(select(Todo).filter(Todo.id == 5))
    todo = result.scalar_one_or_none()
    assert todo is None


async def test_delete_todo_not_found(client):
    response = await client.delete("/todo/99")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}
