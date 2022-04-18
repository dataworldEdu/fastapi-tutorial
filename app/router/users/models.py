from typing import List
from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    user_name: str
    age: int
    birthday: str


class UserList(BaseModel):
    __root__: List[User]

