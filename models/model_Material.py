from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.BaseModel import BaseModel, Base

class Material(BaseModel(Base)):
    __tablename__ = "materials"

    name = Column(String, unique=True, index=True)

    product = relationship("Product", back_populates="material")