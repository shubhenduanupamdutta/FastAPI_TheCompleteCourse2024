import pytest
from fastapi import HTTPException
from jose import jwt
from sqlalchemy.ext.asyncio import AsyncSession

from ..app.config import settings
from ..app.oauth2 import create_access_token, get_current_user
from ..app.routers.auth import authenticate_user

pytestmark = pytest.mark.anyio


async def test_authenticate_user(session: AsyncSession):
    test_username: str = "rooh_baba"

    authenticated_user = await authenticate_user(test_username, "password_123", session)
    # print(repr(authenticated_user))
    assert authenticated_user is not None
    assert authenticated_user.username == test_username  # type: ignore

    non_existent_user = await authenticate_user("WrongUserName", "test_password", session)
    assert non_existent_user is None

    wrong_password_user = await authenticate_user(test_username, "WrongPassword", session)
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


async def test_get_current_user_valid_token():
    encode = {"sub": "test_user", "id": 1, "role": "admin"}
    token = jwt.encode(encode, settings.secret_key, algorithm=settings.algorithm)

    user = await get_current_user(token=token)
    assert user == {"username": "test_user", "id": 1, "user_role": "admin"}


async def test_get_current_user_missing_payload():
    encode = {"role": "user"}
    token = jwt.encode(encode, settings.secret_key, algorithm=settings.algorithm)

    with pytest.raises(HTTPException) as exc_info:
        await get_current_user(token=token)
    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid token"
