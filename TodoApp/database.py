from typing import Annotated, Generator, TypeAlias
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "sqlite:///./TodosApp.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    """This function is used to get the database session yield it and close it after use, when the
    session is used and control is returned. This is done to ensure that the session is closed after
    use and to avoid memory leaks.

    Yields:
        sessionmaker[Session]: The database session to be used
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DB_Dependency: TypeAlias = Annotated[Session, Depends(get_db)]