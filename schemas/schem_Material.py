from pydantic import BaseModel
from typing import Optional

class MaterialBase(BaseModel):

    name: str

class MaterialCreate(MaterialBase):
    pass

class Material(MaterialBase):

    id: int

    class Config:
        orm_mode = True