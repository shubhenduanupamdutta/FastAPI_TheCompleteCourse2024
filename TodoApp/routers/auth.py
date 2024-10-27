from typing import Annotated

from database import DB_Dependency
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models import User
from passlib.context import CryptContext
from schema import CreateUserRequest

router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return True


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


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: DB_Dependency
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    return {"success": "Authentication Successful"}
