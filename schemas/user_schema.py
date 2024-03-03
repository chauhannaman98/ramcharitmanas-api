import datetime
from pydantic import BaseModel
from typing import Optional

from tomlkit import date



class UserInputModel(BaseModel):
    username: str
    password: str
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class config():
        from_attributes = True


class UserOutputModel(BaseModel):
    created_at: datetime.datetime
    username: str
    first_name: str
    last_name: str


class UserUpdateModel(BaseModel):
    username: str
    password: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None