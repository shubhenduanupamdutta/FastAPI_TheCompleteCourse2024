# ruff: noqa: F401, F811
from fastapi import status

from ..app.models import User
from ..app.routers.auth import bcrypt_context
from .utils import TestingSessionLocal, client, test_user


def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    json_response = response.json()
    assert json_response.get("username") == "roohbaba"
    assert json_response.get("email") == "roohbaba@gmail.co.in"
    assert json_response.get("first_name") == "Rooh"
    assert json_response.get("last_name") == "Baba"
    assert json_response.get("role") == "admin"
    assert json_response.get("phone_number") == "(111)-111-1111"
    assert bcrypt_context.verify("test_password", json_response.get("hashed_password"))


def test_change_password_success(test_user):
    response = client.put(
        "/user/change_password",
        json={"password": "test_password", "new_password": "new_password"},
    )
    assert response.status_code == status.HTTP_200_OK
    json_response = response.json()
    user = TestingSessionLocal().query(User).filter(User.id == 1).first()
    assert bcrypt_context.verify("new_password", user.hashed_password)  # type: ignore
    assert json_response.get("username") == user.username  # type: ignore
    assert json_response.get("email") == user.email  # type: ignore
    assert json_response.get("first_name") == user.first_name  # type: ignore
    assert json_response.get("last_name") == user.last_name  # type: ignore
    assert json_response.get("role") == user.role  # type: ignore
    assert json_response.get("phone_number") == user.phone_number  # type: ignore


def test_change_password_invalid_password(test_user):
    response = client.put(
        "/user/change_password",
        json={"password": "invalid_password", "new_password": "new_password"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Error on password change."}


def test_change_phone_number(test_user):
    response = client.put("/user/phone_number/(222)-222-2222")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    user = TestingSessionLocal().query(User).filter(User.id == 1).first()
    assert user.phone_number == "(222)-222-2222"  # type: ignore
