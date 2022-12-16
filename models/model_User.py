from sqlalchemy import ForeignKey, Column, String, Integer, Date
from sqlalchemy.orm import relationship
from models.BaseModel import BaseModel, Base

class User(BaseModel(Base)):
    __tablename__ = "users"

    name = Column(String)
    login = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    payment = Column(Integer)
    reg_date = Column(Date)
    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="user")
    log = relationship("Log", back_populates="user")
    order = relationship("Order", back_populates="user")
    crate = relationship("Crate", back_populates="user")