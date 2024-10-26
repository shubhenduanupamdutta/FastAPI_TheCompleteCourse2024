from typing import Annotated, Final

from fastapi import Body, FastAPI

app = FastAPI()

BOOKS: Final[list[dict[str, str]]] = [
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "category": "Fantasy",
    },
    {
        "title": "Harry Potter and the Chamber of Secrets",
        "author": "J.K. Rowling",
        "category": "Fantasy",
    },
    {
        "title": "The Foundation",
        "author": "Isaac Asimov",
        "category": "Science Fiction",
    },
    {"title": "The Da Vinci Code", "author": "Dan Brown", "category": "Thriller"},
    {"title": "Angels & Demons", "author": "Dan Brown", "category": "Thriller"},
    {
        "title": "Storm Front (The Dresden Files)",
        "author": "Jim Butcher",
        "category": "Fantasy",
    },
    {
        "title": "Fool Moon (The Dresden Files)",
        "author": "Jim Butcher",
        "category": "Fantasy",
    },
    {
        "title": "The Lincoln Lawyer",
        "author": "Michael Connelly",
        "category": "Thriller",
    },
    {
        "title": "The Monk Who Sold His Ferrari",
        "author": "Robin Sharma",
        "category": "Self-help",
    },
    {"title": "The Alchemist", "author": "Paulo Coelho", "category": "Fantasy"},
]


@app.get("/")
async def first_api():
    return {"message": "Hello Shubhendu!"}


@app.get("/books")
async def get_all_books_filtered_by_category(
    category: str | None = None,
) -> list[dict[str, str]]:
    if category is None:
        return BOOKS
    return [
        book for book in BOOKS if book["category"].casefold() == category.casefold()
    ]


@app.get("/books/{book_title}")
async def read_book(book_title: str) -> dict[str, str]:
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            return book
    return {"message": "Book not found"}


@app.get("/books/{author}")
async def get_books_by_author_and_category(
    author: str, category: str
) -> list[dict[str, str]]:
    return [
        book
        for book in BOOKS
        if book["author"].casefold() == author.casefold()
        and book["category"].casefold() == category.casefold()
    ]


@app.post("/books/create_book")
async def create_book(new_book: Annotated[dict[str, str], Body()]) -> dict[str, str]:
    BOOKS.append(new_book)
    return new_book


@app.put("/books/update_book/{book_title}")
async def update_book(
    book_title: str, updated_book: Annotated[dict[str, str], Body()]
) -> dict[str, str]:
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            book.update(updated_book)
            return book
    return {"message": "Book not found"}


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str) -> dict[str, str]:
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            BOOKS.remove(book)
            return {"message": "Book deleted"}
    return {"message": "Book not found"}


@app.get("/books/by_author/{author}")
async def get_books_by_author(author: str) -> list[dict[str, str]]:
    return [book for book in BOOKS if book["author"].casefold() == author.casefold()]
