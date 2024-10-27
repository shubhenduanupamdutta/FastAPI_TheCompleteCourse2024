from datetime import datetime, timedelta, timezone

from config import settings
from jose import JWTError, jwt


def create_access_token(username: str, user_id: int):
    encode = {"sub": username, "id": user_id}
    expires = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_expire_minutes
    )
    encode.update({"exp": expires})
    return jwt.encode(encode, settings.secret_key, algorithm=settings.algorithm)
