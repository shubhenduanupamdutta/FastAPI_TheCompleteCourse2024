import pytest
from fastapi import status
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


def test_read_all_authenticated(test_todo):
    response = client.get("/todo")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "complete": False,
            "title": "Learn to code.",
            "description": "I want to learn to code in Python.",
            "id": 1,
            "priority": 5,
            "owner_id": 1,
        }
    ]


def test_read_one_authenticated(test_todo):
    response = client.get("/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "complete": False,
        "title": "Learn to code.",
        "description": "I want to learn to code in Python.",
        "id": 1,
        "priority": 5,
        "owner_id": 1,
    }


def test_read_one_authenticated_not_found():
    response = client.get("/todo/99")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}
