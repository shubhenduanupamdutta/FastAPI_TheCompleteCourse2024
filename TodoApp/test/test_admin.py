import pytest
from fastapi import status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..app.models import Todo

pytestmark = pytest.mark.anyio


async def test_admin_read_all_authenticated(client):
    response = await client.get("/admin/todo")
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert len(response_data) == 4
    assert response_data == [
        {
            "id": 1,
            "title": "Test Todo 1",
            "owner_id": 1,
            "complete": False,
            "priority": 1,
            "description": "This is a test todo 1",
        },
        {
            "id": 2,
            "title": "Test Todo 2",
            "owner_id": 2,
            "complete": False,
            "priority": 2,
            "description": "This is a test todo 2",
        },
        {
            "id": 3,
            "title": "Learn FastAPI",
            "owner_id": 1,
            "complete": False,
            "priority": 1,
            "description": "Learn FastAPI from docs",
        },
        {
            "id": 4,
            "title": "Learn SQLAlchemy",
            "owner_id": 2,
            "complete": False,
            "priority": 2,
            "description": "Learn SQLAlchemy from docs",
        },
    ]


async def test_admin_delete_todo(client, session: AsyncSession):
    response = await client.delete("/admin/todo/4")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    result = await session.execute(select(Todo).filter(Todo.id == 4))
    todo = result.scalar_one_or_none()
    assert todo is None


async def test_admin_delete_todo_not_found(client):
    response = await client.delete("/admin/todo/99")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}
