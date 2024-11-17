from dataclasses import dataclass
from typing import Annotated

from fastapi import FastAPI, HTTPException, Path, Query, status
from pydantic import BaseModel, Field

app = FastAPI()


@dataclass(slots=True)
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int


class BookRequest(BaseModel):
    id: int | None = Field(default=None, description="ID is not needed when creating a new book")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=0, le=5)
    published_date: int = Field(gt=1999, lt=2025)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Title of the book",
                "author": "Author of the book",
                "description": "Description of the book",
                "rating": 5,
                "published_date": 2021,
            }
        }
    }


BOOKS: list[Book] = [
    Book(
        1,
        "The Great Gatsby",
        "F. Scott Fitzgerald",
        "The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan.",
        4,
        2013,
    ),
    Book(
        2,
        "To Kill a Mockingbird",
        "Harper Lee",
        "The story of young Scout Finch and her father, Atticus, as they navigate issues",
        4,
        2015,
    ),
    Book(3, "Computer Science Pro", "codingwithroby", "A very nice book!", 5, 2021),
    Book(
        4,
        "Harry Potter and the Philosopher's Stone",
        "J.K. Rowling",
        "The story of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley.",
        5,
        2001,
    ),
    Book(
        5,
        "Storm Front",
        "Jim Butcher",
        "The story of Harry Dresden, a wizard detective who solves supernatural crimes in Chicago.",
        5,
        2000,
    ),
    Book(
        6,
        "The Hobbit",
        "J.R.R. Tolkien",
        "The story of Bilbo Baggins, a hobbit who embarks on an epic quest to reclaim the Lonely Mountain from the dragon Smaug.",
        5,
        2002,
    ),
    Book(
        7,
        "Harry Potter and the Chamber of Secrets",
        "J.K. Rowling",
        "The story of Harry Potter's second year at Hogwarts School of Witchcraft and Wizardry.",
        5,
        2003,
    ),
    Book(
        8,
        "Harry Potter and the Prisoner of Azkaban",
        "J.K. Rowling",
        "The story of Harry Potter's third year at Hogwarts School of Witchcraft and Wizardry.",
        5,
        2004,
    ),
    Book(
        9,
        "The Foundation",
        "Isaac Asimov",
        "The story of the decline and fall of a galactic empire and the rise of a new one.",
        5,
        2005,
    ),
    Book(
        10,
        "Fool Moon",
        "Jim Butcher",
        "The story of Harry Dresden, a wizard detective who solves supernatural crimes in Chicago.",
        5,
        2009,
    ),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def get_all_books() -> list[Book]:
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def get_book(book_id: Annotated[int, Path(gt=0)]) -> Book:
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_books_by_rating(
    book_rating: Annotated[int, Query(ge=0, le=5)],
) -> list[Book]:
    return [book for book in BOOKS if book.rating == book_rating]


@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def get_books_by_publish_date(
    publish_date: Annotated[int, Query(ge=2000, le=2026)],
) -> list[Book]:
    return [book for book in BOOKS if book.published_date == publish_date]


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book: BookRequest) -> Book:
    new_book = Book(**book.model_dump())
    find_book_id(new_book)
    BOOKS.append(new_book)
    return new_book


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1


@app.put("/books/update_book", status_code=status.HTTP_200_OK)
async def update_book(update_book: BookRequest) -> Book:
    for i, book in enumerate(BOOKS):
        if update_book.id == book.id:
            BOOKS[i] = Book(**update_book.model_dump())
            return BOOKS[i]
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: Annotated[int, Path(gt=0)]) -> None:
    for book in BOOKS:
        if book.id == book_id:
            BOOKS.remove(book)
            return
    raise HTTPException(status_code=404, detail="Book not found")
