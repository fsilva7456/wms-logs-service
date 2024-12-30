from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

Base = declarative_base()

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    log_type = Column(String(255), nullable=False)
    message = Column(Text, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())