from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


books = [
    
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "published_date": "2020-08-20",
        "page_count": 792,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2019-05-03",
        "page_count": 544,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "publisher": "No Starch Press",
        "published_date": "2015-04-14",
        "page_count": 504,
        "language": "English",
    },
]
class Book(BaseModel):
    id:int  
    title:str
    author: str
    publisher: str
    published_date:str
    page_count: int
    language:str
    
class UpdateBook(BaseModel):
    title:str
    author: str
    publisher: str
    
    
@app.get('/getbooks', response_model= List[Book])
async def get_all_books():
    return books

@app.post('/getbooks')
async def add_book(book1:Book)->list:
    added_book = book1.model_dump()
    books.append(added_book)
    return books

@app.get('/book/{book_id}')
async def search_book(book_id:int):
    for book in books :
        if book["id"]==book_id:
            return book
        
@app.patch('/book/{book_id}')
async def update_book(book_id:int, updated_book:UpdateBook):
    for book in books:
        if book["id"]==book_id:
            book["title"] = updated_book.title
            book['author'] = updated_book.author
            book['publisher'] = updated_book.publisher
            return book
            
        