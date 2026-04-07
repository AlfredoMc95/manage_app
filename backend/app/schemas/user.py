from pydantic import BaseModel
from typing import List
from app.schemas.console import Console

class UserBase(BaseModel):
    name: str
    status: bool
    location: str

class CreateUser(UserBase):
    # opcional: crear usuario con consolas
    consoles: List[Console] = []

class User(UserBase):
    id: int
    consoles: List[Console] = []

    class Config:
        from_attributes = True

class UpdateUser(BaseModel):
    name: str | None = None
    status: bool | None = None
    location: str | None = None