from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.BaseModel import BaseModel, Base

class Image(BaseModel(Base)):
    __tablename__ = "images"

    img_url = Column(String)
    
    product = relationship("Product", back_populates="img")