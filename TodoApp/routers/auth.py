from database import DB_Dependency
from fastapi import APIRouter, HTTPException, status
from models import User
from passlib.context import CryptContext
from schema import CreateUserRequest

router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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
