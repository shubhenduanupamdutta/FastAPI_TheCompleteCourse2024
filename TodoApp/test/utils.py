import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine, text
from sqlalchemy.orm import sessionmaker

from ..app.database import Base, get_db
from ..app.main import app
from ..app.models import Todo
from ..app.oauth2 import get_current_user

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create Engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Create Testing Session
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in the database
Base.metadata.create_all(bind=engine)


# Dependency Injection
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Override get_current_user function
def override_get_current_user():
    return {"username": "shubhenduanupam", "id": 1, "user_role": "admin"}


# Override production function
app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

# Test Client
client = TestClient(app)


@pytest.fixture
def test_todo():
    todo = Todo(
        title="Learn to code.",
        description="I want to learn to code in Python.",
        priority=5,
        complete=False,
        owner_id=1,
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("delete from todos"))
        connection.commit()