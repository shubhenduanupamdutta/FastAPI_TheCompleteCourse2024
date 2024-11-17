from typing import Annotated

from fastapi import APIRouter, HTTPException, Path, status

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
    return db.query(Todo).all()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    user: UserDependency, db: DB_Dependency, todo_id: Annotated[int, Path(ge=1)]
):
    if user.get("user_role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )
    todo_query = db.query(Todo).filter(Todo.id == todo_id)
    if todo_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    todo_query.delete(synchronize_session=False)
    db.commit()
