from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):

    name: str
    desc: str
    stock: Optional[int]
    sale: Optional[int]
    price: int
    weight: int
    prodtype_id: int
    material_id: int
    image_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):

    id: int

    class Config:
        orm_mode = True