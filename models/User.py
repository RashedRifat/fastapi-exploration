from typing import Union
from pydantic import BaseModel

class User(BaseModel):
    username: str 
    email: Union[str, None] = None 
    full_name: Union[str, None] = None 
    disabled: Union[str, None] = None 

def decode_user(token):
    return User(
        username="john", email="john@google.com", full_name="John Smith"
    )