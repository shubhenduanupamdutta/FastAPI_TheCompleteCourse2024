from typing import Annotated, TypeAlias

from fastapi import APIRouter, HTTPException, Path, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from ..database import DB_Dependency
from ..models import Todo
from ..oauth2 import UserDependency, get_current_user
from ..schema import TodoRequest

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()

TodoId: TypeAlias = Annotated[int, Path(ge=1)]


def redirect_to_login():
    redirect_response = RedirectResponse(
        url="/auth/login-page", status_code=status.HTTP_302_FOUND
    )
    redirect_response.delete_cookie(key="access_token")
    return redirect_response


### Pages ###


@router.get("/todo-page")
async def render_todo_page(request: Request, db: DB_Dependency):
    try:
        user = await get_current_user(request.cookies.get("access_token"))  # type: ignore
        if user is None:
            return redirect_to_login()
        todos = db.query(Todo).filter(Todo.owner_id == user.get("id")).all()
        return templates.TemplateResponse(
            "todo.html", {"request": request, "todos": todos, "user": user}
        )
    except Exception as _exc:
        return redirect_to_login()


@router.get("/add-todo-page")
async def render_add_todo_page(request: Request):
    try:
        user = await get_current_user(request.cookies.get("access_token"))  # type: ignore
        if user is None:
            return redirect_to_login()
        return templates.TemplateResponse(
            "add-todo.html", {"request": request, "user": user}
        )
    except Exception as _exc:
        print(f"Error: {_exc!r}")
        return redirect_to_login()


@router.get("/edit-todo-page/{todo_id}")
async def render_edit_todo_page(request: Request, todo_id: int, db: DB_Dependency):
    try:
        user = await get_current_user(request.cookies.get("access_token"))  # type: ignore
        if user is None:
            return redirect_to_login()
        todo = (
            db.query(Todo)
            .filter(Todo.id == todo_id)
            .filter(Todo.owner_id == user.get("id"))
            .first()
        )
        if todo is None:
            return redirect_to_login()
        return templates.TemplateResponse(
            "edit-todo.html", {"request": request, "todo": todo, "user": user}
        )
    except Exception as _exc:
        print(f"Error: {_exc!r}")
        return redirect_to_login()


### Endpoints ###


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
        db.query(Todo)
        .filter(Todo.id == todo_id)
        .filter(Todo.owner_id == user.get("id"))
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
        db.query(Todo)
        .filter(Todo.id == todo_id)
        .filter(Todo.owner_id == user.get("id"))
    )
    todo_model = todo_query.first()
    if todo_model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    todo_query.delete(synchronize_session=False)
    db.commit()
