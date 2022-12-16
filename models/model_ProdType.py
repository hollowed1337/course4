from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.BaseModel import BaseModel, Base

class ProdType(BaseModel(Base)):
    __tablename__ = "products_type"

    name = Column(String, unique=True, index=True)

    product = relationship("Product", back_populates="prodtype")