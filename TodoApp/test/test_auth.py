# ruff: noqa: F401, F811
import pytest
from fastapi import HTTPException
from jose import jwt

from ..app.config import settings
from ..app.models import User
from ..app.oauth2 import create_access_token, get_current_user
from ..app.routers.auth import authenticate_user
from .utils import TestingSessionLocal, client, test_todo, test_user


def test_authenticate_user(test_user: User):
    db = TestingSessionLocal()
    test_username: str = test_user.username  # type: ignore

    authenticated_user = authenticate_user(test_username, "test_password", db)
    print(repr(authenticated_user))
    assert authenticated_user is not None
    assert authenticated_user.username == test_username  # type: ignore

    non_existent_user = authenticate_user("WrongUserName", "test_password", db)
    assert non_existent_user is None

    wrong_password_user = authenticate_user(test_username, "WrongPassword", db)
    assert wrong_password_user is None


def test_create_access_token():
    username = "test_user"
    user_id = 1
    role = "user"

    token = create_access_token(username, user_id, role)

    decoded_token = jwt.decode(
        token,
        settings.secret_key,
        algorithms=[settings.algorithm],
        options={"verify_signature": False},
    )

    assert decoded_token.get("sub") == username
    assert decoded_token.get("id") == user_id
    assert decoded_token.get("role") == role


@pytest.mark.asyncio
async def test_get_current_user_valid_token():
    encode = {"sub": "test_user", "id": 1, "role": "admin"}
    token = jwt.encode(encode, settings.secret_key, algorithm=settings.algorithm)

    user = await get_current_user(token=token)
    assert user == {"username": "test_user", "id": 1, "user_role": "admin"}


@pytest.mark.asyncio
async def test_get_current_user_missing_payload():
    encode = {"role": "user"}
    token = jwt.encode(encode, settings.secret_key, algorithm=settings.algorithm)

    with pytest.raises(HTTPException) as exc_info:
        await get_current_user(token=token)
    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid token"
