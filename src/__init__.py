from fastapi import FastAPI
from src.Books.routes import book_router
from src.auth.routes import auth_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"SErver is starting ....")
    await init_db()
    yield
    print(f"Server has been stopped")
    

version = "v1"
app = FastAPI(
    title = "Bookly",
    description="A rest api for a book review web service",
    version=version,
    lifespan = life_span
)
app.include_router(book_router, prefix ="/books")
app.include_router(auth_router, prefix=f"/auth")