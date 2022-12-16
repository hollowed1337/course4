from pydantic import BaseModel
from typing import Optional

class ProdTypeBase(BaseModel):

    name: str

class ProdTypeCreate(ProdTypeBase):
    pass

class ProdType(ProdTypeBase):

    id: int

    class Config:
        orm_mode = True