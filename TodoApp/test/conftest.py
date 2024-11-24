import asyncio
import sys
from typing import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    AsyncTransaction,
    create_async_engine,
)

from ..app.config import settings
from ..app.database import Base, get_db
from ..app.main import app
from ..app.models import Todo, User
from ..app.oauth2 import get_current_user

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg_async://{settings.db_user}:{settings.db_password}@{settings.db_host}"
    f":5432/{settings.db_name}_test"
)


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    """
    Creates an instance of the default event loop for the test session.
    """
    if sys.platform.startswith("win") and sys.version_info[:2] >= (3, 8):
        # Avoid "RuntimeError: Event loop is closed" on Windows when tearing down tests
        # https://github.com/encode/httpx/issues/914
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL)


@pytest.fixture(scope="session")
async def connection(anyio_backend) -> AsyncGenerator[AsyncConnection, None]:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with async_engine.connect() as conn:
        yield conn


@pytest.fixture()
async def transaction(connection: AsyncConnection) -> AsyncGenerator[AsyncTransaction, None]:
    async with connection.begin() as transaction:
        yield transaction


# Use this fixture to get SQLAlchemy's AsyncSession.
# All changes that occur in a test function are rolled back
# after function exits, even if session.commit() is called
# in inner functions
@pytest.fixture()
async def session(
    connection: AsyncConnection, transaction: AsyncTransaction
) -> AsyncGenerator[AsyncSession, None]:
    async_session = AsyncSession(
        bind=connection,
        join_transaction_mode="create_savepoint",
    )

    yield async_session

    await transaction.rollback()


# Use this fixture to get HTTPX's client to test API.
# All changes that occur in a test function are rolled back
# after function exits, even if session.commit() is called
# in FastAPI's application endpoints
@pytest.fixture()
async def client(
    connection: AsyncConnection, transaction: AsyncTransaction
) -> AsyncGenerator[AsyncClient, None]:
    async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
        async_session = AsyncSession(
            bind=connection,
            join_transaction_mode="create_savepoint",
        )
        async with async_session:
            yield async_session

    # Here you have to override the dependency that is used in FastAPI's
    # endpoints to get SQLAlchemy's AsyncSession. In my case, it is
    # get_async_session
    app.dependency_overrides[get_db] = override_get_async_session

    # Override get_current_user dependency to return a user
    def override_get_current_user():
        return {"username": "shubhenduanupam", "id": 1, "user_role": "admin"}

    app.dependency_overrides[get_current_user] = override_get_current_user
    yield AsyncClient(transport=ASGITransport(app=app), base_url="http://test")
    del app.dependency_overrides[get_db]
    del app.dependency_overrides[get_current_user]

    await transaction.rollback()


@pytest.fixture
async def test_data(session: AsyncSession):
    bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    users = [
        User(
            username="rooh_baba",
            email="rooh_baba@bhool.bhulaiya.co.in",
            first_name="Rooh",
            last_name="Baba",
            hashed_password=bcrypt_context.hash("password_123"),
            is_active=True,
            role="admin",
            phone_number="1234567890",
        ),
        User(
            username="naruto_uzumaki",
            email="naruto_uzumaki@konoho.com",
            first_name="Naruto",
            last_name="Uzumaki",
            hashed_password=bcrypt_context.hash("Orange_Hokage"),
            is_active=True,
            role="normal",
            phone_number="+(111)-222-3333",
        ),
    ]

    session.add_all(users)
    await session.commit()

    result = await session.execute(select(User).filter(User.username == "rooh_baba"))
    admin = result.scalars().one()

    result = await session.execute(select(User).filter(User.username == "naruto_uzumaki"))
    normal = result.scalars().one()

    todos = [
        Todo(
            title="Test Todo 1",
            description="This is a test todo 1",
            priority=1,
            complete=False,
            owner_id=admin.id,
        ),
        Todo(
            title="Test Todo 2",
            description="This is a test todo 2",
            priority=2,
            complete=False,
            owner_id=normal.id,
        ),
        Todo(
            title="Learn FastAPI",
            description="Learn FastAPI from docs",
            priority=1,
            complete=False,
            owner_id=admin.id,
        ),
        Todo(
            title="Learn SQLAlchemy",
            description="Learn SQLAlchemy from docs",
            priority=2,
            complete=False,
            owner_id=normal.id,
        ),
    ]

    session.add_all(todos)
    await session.commit()
