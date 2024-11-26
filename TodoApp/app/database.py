from typing import Annotated, AsyncGenerator, TypeAlias

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from .config import settings

# SQLALCHEMY_DATABASE_URL = "sqlite:///./TodosApp.db" # To connect with SQLite database

# URL to connect with PostgreSQL database normally
# SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{settings.db_user}:{settings.db_password}@{settings.db_host}:5432/{settings.db_name}"

# URL to connect with PostgreSQL database using asyncio
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg_async://{settings.db_user}:{settings.db_password}@{settings.db_host}:5432/{settings.db_name}"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# ) # To connect with SQLite database

# Connecting with PostgreSQL database normally
# engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Connecting with PostgreSQL database using asyncio
async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_session = async_sessionmaker(autocommit=False, autoflush=False, bind=async_engine)

Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """This function is used to get the database session yield it and close it after use, when the
    session is used and control is returned. This is done to ensure that the session is closed
    after use and to avoid memory leaks.

    Yields:
        AsyncSession: The database session to be used
    """
    db = async_session()
    try:
        yield db
    finally:
        await db.close()


DB_Dependency: TypeAlias = Annotated[AsyncSession, Depends(get_db)]
