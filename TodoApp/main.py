from typing import Annotated, Generator, TypeAlias, TypeVar

import models
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, Path, Query, status
from models import Todo
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# Will only run once and if only the database is not created


def get_db() -> Generator[Session, None, None]:
    """This function is used to get the database session yield it and close it after use, when the
    session is used and control is returned. This is done to ensure that the session is closed after
    use and to avoid memory leaks.

    Yields:
        sessionmaker[Session]: The database session to be used
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(ge=1, le=5)
    complete: bool


T = TypeVar("T")
DB_Dependency: TypeAlias = Annotated[Session, Depends(get_db)]
TodoId: TypeAlias = Annotated[int, Path(ge=1)]
QueryParam: TypeAlias = Annotated[T, Query()]


@app.get("/", status_code=status.HTTP_200_OK)
async def get_all_todos(db: DB_Dependency):
    """# This function is used to get all the todos from the database"""
    return db.query(Todo).all()


@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo_by_id(db: DB_Dependency, todo_id: TodoId):
    """# This function is used to get a todo by its id"""
    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")


@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: DB_Dependency, todo_request: TodoRequest):
    """# This function is used to create a todo"""
    todo_model = Todo(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model


@app.put("/todo/{todo_id}", status_code=status.HTTP_200_OK)
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


@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
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
