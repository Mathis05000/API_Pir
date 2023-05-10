from typing import Union
from datetime import date
from pydantic import BaseModel 

# Message

class MessageBase(BaseModel):
    content: str
    date: int


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# Users

class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    messages: list[Message] = []

    class Config:
        orm_mode = True

