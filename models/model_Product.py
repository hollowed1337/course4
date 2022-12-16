from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship
from models.BaseModel import BaseModel, Base

class Product(BaseModel(Base)):
    __tablename__ = "products"

    name = Column(String)
    desc = Column(String)
    stock = Column(Integer)
    sale = Column(Integer)
    price = Column(Integer)
    weight = Column(Integer)
    prodtype_id = Column(Integer, ForeignKey("products_type.id"))
    material_id = Column(Integer, ForeignKey("materials.id"))
    image_id = Column(Integer, ForeignKey("images.id"))

    order = relationship("Order", back_populates="product")
    crate = relationship("Crate", back_populates="product")
    material = relationship("Material", back_populates="product")
    prodtype = relationship("ProdType", back_populates="product")
    img = relationship("Image", back_populates="product")