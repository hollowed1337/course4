from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.BaseModel import BaseModel, Base

class Order(BaseModel(Base)):
    __tablename__ = "orders"

    name = Column(String)
    order_num = Column(Integer, unique=True, index=True)
    price = Column(Integer)
    date = Column(DateTime)
    order_status = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    crate = relationship("Crate", back_populates="order")
    user = relationship("User", back_populates="order")
    product = relationship("Product", back_populates="order")