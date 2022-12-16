from datetime import date
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    
    name: Optional[str]
    login : str
    email: EmailStr
    payment: Optional[int]
    role_id: Optional[int]

class UserCreate(UserBase):

    password: str

class UserUpdate(BaseModel):
    
    name: Optional[str]
    login : str
    email: EmailStr
    password: str
    payment: Optional[int]
    role_id: Optional[int]
    

class User(UserBase):

    reg_date: date
    id: int

    class Config:
        orm_mode = True