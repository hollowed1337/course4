from pydantic import BaseModel
from typing import Optional

class CrateBase(BaseModel):

    count: int
    summ: int
    status: str
    product_id: Optional[int]
    order_id: Optional[int]
    user_id: Optional[int]

class CrateCreate(CrateBase):
    pass

class Crate(CrateBase):
    
    id: int

    class Config:
        orm_mode = True