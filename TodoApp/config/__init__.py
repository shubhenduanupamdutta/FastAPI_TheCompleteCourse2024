"""Generate environment variables for the app"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    db_user: str
    db_password: str
    db_host: str
    db_name: str

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
