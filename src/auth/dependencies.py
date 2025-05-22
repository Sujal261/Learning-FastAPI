from fastapi.security import HTTPBearer
from fastapi import Request, status
from fastapi.security.http import HTTPAuthorizationCredentials
from .utils import decode_token
from fastapi.exceptions  import HTTPException
from src.db.redis import token_in_blocklist

class TokenBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        super().__init__(auto_error=auto_error)
        
    async def __call__(self, request:Request)-> HTTPAuthorizationCredentials | None:
        creds =  await super().__call__(request)
        token = creds.credentials
        token_data = decode_token(token)
        if not self.token_valid(token):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail ="Invalid or expired token"
            )
        if await token_in_blocklist(token_in_blocklist['jti']):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail ={
                   "error": "Invalid or expired token",
                   "resolution":"Please get the new token"}
            )
            
        
            
        # print(creds.scheme)
        # print(creds.credentials)
        self.verify_token_data(token_data)
        return token_data
    
    def token_valid(self, token:str)->bool:
        token_data = decode_token(token)
        if token_data is not None:
            return True 
        
        else:
            return False
    def verify_token_data(self, token_data):
        raise NotImplementedError("Please Override this methods in child classes")
class AccessTokenBearer(TokenBearer):
    def verify_token_data(self, token_data:dict)->None:
        if token_data and token_data['refresh']:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail ="Provide access token"
            )
        
class RereshTokenBearer(TokenBearer):
    def verify_token_data(self, token_data:dict)->None:
        if token_data and not  token_data['refresh']:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail ="Provide refresh token"
            )