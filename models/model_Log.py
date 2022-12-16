from sqlalchemy import ForeignKey, Column, Integer, DateTime
from sqlalchemy.orm import relationship, declarative_base
from models.BaseModel import BaseModel,Base

class Log(BaseModel(Base)):
    __tablename__ = "logs"

    input_time = Column(DateTime)
    output_time = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="log")