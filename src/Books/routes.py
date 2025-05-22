from src.Books.schema import Book, UpdateBook, BookCreateModel
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession 
from src.Books.service import BookService
from fastapi import APIRouter, Depends
from src.db.main import get_session
from datetime import datetime 
import uuid
from src.auth.dependencies import AccessTokenBearer

book_router= APIRouter()
book_service = BookService()
access_token_bearer = AccessTokenBearer()


@book_router.get('/', response_model= List[Book])
async def get_all_books(session :AsyncSession=Depends(get_session), user_detials=Depends(access_token_bearer)):
    books =await book_service.get_all_books(session)
    return books

@book_router.post('/')
async def create_a_book(book_data:BookCreateModel,session:AsyncSession=Depends(get_session),
                        user_details = Depends(access_token_bearer))->dict:
    new_book =await book_service.create_book(book_data, session)
    return new_book

@book_router.get('/{book_uid}')
async def get_book(book_uid:uuid.UUID, session:AsyncSession=Depends(get_session),user_details = Depends(access_token_bearer)):
    book =await book_service.get_book(book_uid, session )
    return book
    
        
@book_router.patch('/{book_uid}')
async def update_book(book_uid:uuid.UUID, book_update_data:UpdateBook, session:AsyncSession=Depends(get_session),user_details = Depends(access_token_bearer)):
    updated_book =await book_service.update_book(book_uid,book_update_data, session )
    return updated_book
            