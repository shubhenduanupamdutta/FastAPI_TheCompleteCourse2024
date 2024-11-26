from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    # id = Column(Integer, primary_key=True, index=True)
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # email = Column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    # username = Column(String, unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    # first_name = Column(String)
    first_name: Mapped[str]
    # last_name = Column(String)
    last_name: Mapped[str]
    # hashed_password = Column(String)
    hashed_password: Mapped[str]
    # is_active = Column(Boolean)
    is_active: Mapped[bool]
    # role = Column(String)
    role: Mapped[str]
    # phone_number = Column(String(45), default=None)
    phone_number: Mapped[str] = mapped_column(String(45), default=None)

    user_todos: Mapped[list["Todo"]] = relationship(
        back_populates="owner", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"


class Todo(Base):
    __tablename__ = "todos"

    # id = Column(Integer, primary_key=True, index=True)
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # title = Column(String)
    title: Mapped[str]
    # description = Column(String)
    description: Mapped[str]
    # priority = Column(Integer)
    priority: Mapped[int]
    # complete = Column(Boolean, default=False)
    complete: Mapped[bool] = mapped_column(default=False)
    # owner_id = Column(Integer, ForeignKey("users.id"))
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    owner: Mapped[User] = relationship(back_populates="user_todos")

    def __repr__(self) -> str:
        return f"Todo(id={self.id!r}, title={self.title!r})"
