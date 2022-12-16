from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship, declarative_base
from models.BaseModel import BaseModel, Base

class Role(BaseModel(Base)):
    __tablename__ = "roles"

    name = Column(String, unique=True, index=True)

    user = relationship("User", back_populates="role")