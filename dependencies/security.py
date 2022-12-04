from models.User import User, decode_user
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

oath2_scheme = OAuth2PasswordBearer(tokenUrl='token')

async def get_current_user(token : str = Depends(oath2_scheme)):
    user = decode_user(token)
    return user 
