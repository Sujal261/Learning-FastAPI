from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import Config

engine = create_async_engine(
    url = Config.DATABASE_URL,
    echo = True
)

async def init_db():
    async with engine.begin() as conn:
        from src.Books.models import Book 
        await conn.run_sync(SQLModel.metadata.create_all)
        
async def get_session()->AsyncSession:
    Session = sessionmaker(
        bind = AsyncEngine,
        class_= AsyncSession,
        expire_on_commit = False
    )
    
    async with Session() as session:
        yield session
        
    
