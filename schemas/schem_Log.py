from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LogBase(BaseModel):

    input_time: datetime
    out_time: Optional[datetime]

class LogCreate(LogBase):
    pass

class Log(LogBase):

    id: int
    user_id: int
    class Config:
        orm_mode = True