from .model import User
from sqlmodel.ext.asyncio.session import AsyncSession 
from sqlmodel import select
from .schemas import UserCreateModel
from .utils import generate_password_hash
class UserService:
    async def get_user_by_email(self, email: str, session :AsyncSession):
        statement =  select(User).where(User.email==email)
        result = await session.execute(statement)
        user = result.first()
        return user
    
    async def user_exists(self, email, session:AsyncSession):
        user = await self.get_user_by_email(email, session)
        if user is None:
            return False 
        else:
            return True
        
    async def create_user(self, user_date:UserCreateModel, session:AsyncSession):
        user_data_dict = user_date.model_dump()
        new_user = User(
            **user_data_dict
        )
        new_user.password_hash = generate_password_hash(user_data_dict['password'])
        session.add(new_user)
        await session.commit()
        return new_user
        