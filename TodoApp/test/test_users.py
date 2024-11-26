import pytest
from fastapi import status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..app.models import User
from ..app.routers.auth import bcrypt_context

pytestmark = pytest.mark.anyio


async def test_return_user(client):
    response = await client.get("/user/")
    assert response.status_code == status.HTTP_200_OK
    user_dict = response.json()
    assert user_dict.get("username") == "rooh_baba"
    assert user_dict.get("email") == "rooh_baba@bhool.bhulaiya.co.in"
    assert user_dict.get("role") == "admin"
    assert user_dict.get("first_name") == "Rooh"
    assert user_dict.get("last_name") == "Baba"
    assert user_dict.get("phone_number") == "1234567890"
    assert bcrypt_context.verify("password_123", user_dict.get("hashed_password"))


async def test_change_password_success(client, session: AsyncSession):
    response = await client.put(
        "/user/change_password",
        json={"password": "password_123", "new_password": "new_password"},
    )
    assert response.status_code == status.HTTP_200_OK
    json_response = response.json()
    result = await session.execute(select(User).filter(User.id == 1))
    user = result.scalars().one()
    assert bcrypt_context.verify("new_password", user.hashed_password)  # type: ignore
    assert json_response.get("username") == user.username  # type: ignore
    assert json_response.get("email") == user.email  # type: ignore
    assert json_response.get("first_name") == user.first_name  # type: ignore
    assert json_response.get("last_name") == user.last_name  # type: ignore
    assert json_response.get("role") == user.role  # type: ignore
    assert json_response.get("phone_number") == user.phone_number  # type: ignore


async def test_change_password_invalid_password(client):
    response = await client.put(
        "/user/change_password",
        json={"password": "invalid_password", "new_password": "new_password"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Error on password change."}


async def test_change_phone_number(client, session: AsyncSession):
    response = await client.put("/user/phone_number/(222)-222-2222")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    result = await session.execute(select(User).filter(User.id == 1))
    user = result.scalar_one()
    assert user.phone_number == "(222)-222-2222"  # type: ignore
