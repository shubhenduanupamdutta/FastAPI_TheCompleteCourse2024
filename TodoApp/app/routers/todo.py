from typing import Annotated, TypeAlias

from ..database import DB_Dependency
from fastapi import APIRouter, HTTPException, Path, status
from ..models import Todo
from ..oauth2 import UserDependency
from ..schema import TodoRequest

router = APIRouter()

TodoId: TypeAlias = Annotated[int, Path(ge=1)]


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_todos(user: UserDependency, db: DB_Dependency):
    """# This function is used to get all the todos from the database"""
    return db.query(Todo).filter(Todo.owner_id == user.get("id")).all()


@router.get("/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo_by_id(user: UserDependency, db: DB_Dependency, todo_id: TodoId):
    """# This function is used to get a todo by its id"""

    todo_model = (
        db.query(Todo)
        .filter(Todo.id == todo_id)
        .filter(Todo.owner_id == user.get("id"))
        .first()
    )
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(
    db: DB_Dependency, todo_request: TodoRequest, user: UserDependency
):
    """# This function is used to create a todo"""

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    todo_model = Todo(**todo_request.model_dump(), owner_id=user.get("id"))

    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model


@router.put("/{todo_id}", status_code=status.HTTP_200_OK)
async def update_todo(
    user: UserDependency, db: DB_Dependency, todo_id: TodoId, todo_request: TodoRequest
):
    """# This function is used to update a todo"""
    todo_query = (
        db.query(Todo).filter(Todo.id == todo_id).filter(Todo.owner_id == user.get("id"))
    )
    todo_model = todo_query.first()
    if todo_model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    todo_query.update(todo_request.model_dump(), synchronize_session=False)  # type: ignore
    db.commit()
    db.refresh(todo_model)
    return todo_model


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: UserDependency, db: DB_Dependency, todo_id: TodoId):
    """# This function is used to delete a todo"""
    todo_query = (
        db.query(Todo).filter(Todo.id == todo_id).filter(Todo.owner_id == user.get("id"))
    )
    todo_model = todo_query.first()
    if todo_model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    todo_query.delete(synchronize_session=False)
    db.commit()
