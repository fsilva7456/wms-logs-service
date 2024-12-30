from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LogBase(BaseModel):
    log_type: str
    message: Optional[str] = None

class LogCreate(LogBase):
    pass

class Log(LogBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True