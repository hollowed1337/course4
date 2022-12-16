from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):

    name: str
    order_num: int
    price: int
    order_status: str
    user_id: int
    product_id: int
    

class OrderCreate(OrderBase):

    pass

class Order(OrderBase):

    date: datetime
    id: int

    class Config:
        orm_mode = True


class OrderUpdate(OrderBase):

    name: str
    order_num: int
    price: int
    order_status: str

    class Config:
        orm_mode = True