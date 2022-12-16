from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.BaseModel import BaseModel, Base

class Crate(BaseModel(Base)):
    __tablename__ = "crates"

    count = Column(Integer)
    summ = Column(Integer)
    status = Column(String)
    product_id = Column(Integer, ForeignKey("products.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="crate")
    product = relationship("Product", back_populates="crate")
    order = relationship("Order", back_populates="crate")
