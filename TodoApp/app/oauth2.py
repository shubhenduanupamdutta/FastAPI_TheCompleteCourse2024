from datetime import datetime, timedelta, timezone
from typing import Annotated, TypeAlias

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import ExpiredSignatureError, JWTError, jwt

from .config import settings

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")
OAuth2Form: TypeAlias = Annotated[OAuth2PasswordRequestForm, Depends()]


def create_access_token(username: str, user_id: int, role: str):
    encode = {"sub": username, "id": user_id, "role": role}
    expires = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    encode.update({"exp": expires})
    return jwt.encode(encode, settings.secret_key, algorithm=settings.algorithm)


async def get_current_user(
    token: Annotated[str, Depends(oauth2_bearer)],
) -> dict[str, str | int]:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        username: str | None = payload.get("sub")  # type: ignore
        user_id: int | None = payload.get("id")  # type: ignore
        user_role: str | None = payload.get("role")  # type: ignore
        if username is None or user_id is None or user_role is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return {"username": username, "id": user_id, "user_role": user_role}
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired. Create a new one.",
        ) from ExpiredSignatureError
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        ) from JWTError


UserDependency: TypeAlias = Annotated[dict, Depends(get_current_user)]
