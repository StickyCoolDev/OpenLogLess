from app.schema import LogLevel
from app.db import Base
from sqlalchemy import Column, DateTime, Integer, String, Enum

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    created_at = Column(DateTime, index=True)
    log_level = Column(Enum(LogLevel), index=True)
