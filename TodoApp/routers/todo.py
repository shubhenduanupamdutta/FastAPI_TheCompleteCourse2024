from typing import Annotated, TypeAlias

from database import DB_Dependency
from fastapi import APIRouter, HTTPException, Path, status
from models import Todo
from schema import TodoRequest

router = APIRouter()


TodoId: TypeAlias = Annotated[int, Path(ge=1)]


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_todos(db: DB_Dependency):
    """# This function is used to get all the todos from the database"""
    return db.query(Todo).all()


@router.get("/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo_by_id(db: DB_Dependency, todo_id: TodoId):
    """# This function is used to get a todo by its id"""
    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(db: DB_Dependency, todo_request: TodoRequest):
    """# This function is used to create a todo"""
    todo_model = Todo(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model


@router.put("/{todo_id}", status_code=status.HTTP_200_OK)
async def update_todo(db: DB_Dependency, todo_id: TodoId, todo_request: TodoRequest):
    """# This function is used to update a todo"""
    todo_query = db.query(Todo).filter(Todo.id == todo_id)
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
async def delete_todo(db: DB_Dependency, todo_id: TodoId):
    """# This function is used to delete a todo"""
    todo_query = db.query(Todo).filter(Todo.id == todo_id)
    todo_model = todo_query.first()
    if todo_model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    todo_query.delete(synchronize_session=False)
    db.commit()
