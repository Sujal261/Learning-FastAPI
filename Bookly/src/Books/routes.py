from src.Books.schema import Book, UpdateBook
from typing import List
from src.Books.book import books
from fastapi import APIRouter

book_router= APIRouter()


@book_router.get('/', response_model= List[Book])
async def get_all_books():
    return books

@book_router.post('/')
async def add_book(book1:Book)->list:
    added_book = book1.model_dump()
    books.append(added_book)
    return books

@book_router.get('/{book_id}')
async def search_book(book_id:int):
    for book in books :
        if book["id"]==book_id:
            return book
        
@book_router.patch('/{book_id}')
async def update_book(book_id:int, updated_book:UpdateBook):
    for book in books:
        if book["id"]==book_id:
            book["title"] = updated_book.title
            book['author'] = updated_book.author
            book['publisher'] = updated_book.publisher
            return book
            