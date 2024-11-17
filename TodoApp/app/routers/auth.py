from fastapi import APIRouter, HTTPException, Request, status
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext

from ..database import DB_Dependency
from ..models import User
from ..oauth2 import OAuth2Form, create_access_token
from ..schema import CreateUserRequest, Token

router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

templates = Jinja2Templates(directory="app/templates")


### Pages ###


@router.get("/login-page")
def render_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/register-page")
def render_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


### Endpoints ###


def authenticate_user(username: str, password: str, db) -> User | None:
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    if not bcrypt_context.verify(password, user.hashed_password):
        return None
    return user


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(create_user_request: CreateUserRequest, db: DB_Dependency):
    user_dict = create_user_request.model_dump()
    password = user_dict.pop("password")
    hashed_password = bcrypt_context.hash(password)
    user_dict.update({"hashed_password": hashed_password, "is_active": True})
    new_user = User(**user_dict)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2Form, db: DB_Dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(user.username, user.id, user.role)  # type: ignore

    return {"access_token": token, "token_type": "bearer"}
