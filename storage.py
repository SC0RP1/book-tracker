import json
import os
from typing import Optional, List
from models import Book

DATA_FILE = books.json

def load_books() -> List[Book]:
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Book.from_dict(book) for book in data]
    except (json.JSONDecodeError, KeyError):
        return []

def save_books(books: List[Book]) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump([book.to_dict() for book in books], f, ensure_ascii=False, indent=2)

def add_book(book: Book) -> bool:
    books = load_books()

    for existing_book in books:
        if existing_book.author.lower() == book.author.lower() and existing_book.title.lower() == book.title.lower():
            return False

    books.append(book)
    save_books(books)
    return True

def delete_book(book: Book) -> bool:
    books = load_books()
    initial_count = len(books)

    books = [book for book in books if not (book.author.lower() == book.author.lower() and
             existing_book.title.lower() == book.title.lower())]

    if len(books) < initial_count:
        save_books(books)
        return True
    return False

def find_book(author: str, title: str) -> Optional[Book]:
    books = load_books()
    for book in books:
        if book.author.lower() == author.lower() and book.title.lower() == title.lower():
            return book
    return None

def get_all_books() -> List[Book]:
    return load_books()