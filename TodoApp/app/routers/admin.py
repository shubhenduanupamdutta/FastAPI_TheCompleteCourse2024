from typing import Annotated

from fastapi import APIRouter, HTTPException, Path, status
from sqlalchemy import select

from ..database import DB_Dependency
from ..models import Todo
from ..oauth2 import UserDependency

router = APIRouter()


@router.get("/todo", status_code=status.HTTP_200_OK)
async def get_all(user: UserDependency, db: DB_Dependency):
    if user.get("user_role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )
    result = await db.execute(select(Todo).order_by(Todo.id))
    return result.scalars().all()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    user: UserDependency, db: DB_Dependency, todo_id: Annotated[int, Path(ge=1)]
):
    if user.get("user_role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )
    todo_query = await db.execute(select(Todo).filter(Todo.id == todo_id))
    todo = todo_query.scalar_one_or_none()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await db.delete(todo)
    await db.commit()
