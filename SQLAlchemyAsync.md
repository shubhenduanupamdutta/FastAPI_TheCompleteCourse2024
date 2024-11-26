# Async SQLAlchemy with FastAPI

---

## Installation

**For Async SQLAlchemy to work correctly, you need to install using the following command:**

```bash
pip install sqlalchemy[asyncio]
```

## Creating Async Engine

```python
from sqlalchemy.ext.asyncio import create_async_engine
asyncio_engine = create_async_engine("postgresql+psycopg_async://user:password@localhost/dbname")
```

## Creating Async Session

```python
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
async_session = async_sessionmaker(autocommit=False, autoflush=False, bind=async_engine)
```
## Creating a dependency
```python
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
```
