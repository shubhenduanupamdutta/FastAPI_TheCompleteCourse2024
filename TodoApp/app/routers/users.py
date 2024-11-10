from ..database import DB_Dependency
from fastapi import APIRouter, HTTPException, status
from ..models import User
from ..oauth2 import UserDependency
from passlib.context import CryptContext
from ..schema import UserVerification

router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user: UserDependency, db: DB_Dependency):
    """# This function is used to get a user detail, given the user is authenticated using JWT token

    Args:
        user (UserDependency): UserDependency is a dependency that is used to get the user details from the JWT token
        db (DB_Dependency): DB_Dependency is a dependency that is used to get the database session

    Returns:
        User | None: Returns the user details if the user is found, else returns None
    """
    return db.query(User).filter(User.id == user.get("id")).first()


@router.put("/change_password", status_code=status.HTTP_200_OK)
async def change_password(
    user: UserDependency, db: DB_Dependency, passwords: UserVerification
):
    """# This function is used to change the password of the user

    - user (UserDependency): UserDependency is a dependency that is used to get the user details from the JWT token
    - db (DB_Dependency): DB_Dependency is a dependency that is used to get the database session
    - passwords (UserVerification): UserVerification is a Pydantic model that is used to verify the password
    """

    user_model = db.query(User).filter(User.id == user.get("id")).first()

    if not bcrypt_context.verify(passwords.password, user_model.hashed_password):  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Error on password change."
        )

    user_model.hashed_password = bcrypt_context.hash(passwords.new_password)  # type: ignore
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return user_model


@router.put("/phone_number/{phone_number}", status_code=status.HTTP_204_NO_CONTENT)
async def change_phone_number(
    user: UserDependency, db: DB_Dependency, phone_number: str
):
    """# This function is used to change the phone number of the user

    - user (UserDependency): UserDependency is a dependency that is used to get the user details from the JWT token
    - db (DB_Dependency): DB_Dependency is a dependency that is used to get the database session
    - phone_number (str): The new phone number of the user
    """

    user_model = db.query(User).filter(User.id == user.get("id")).first()
    user_model.phone_number = phone_number  # type: ignore
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return user_model