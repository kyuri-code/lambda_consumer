from sqlalchemy import Column, String
from src.db_client.db_client import Base
from pydantic import BaseModel
import uuid

class Log(Base):
    __tablename__ = 'sample_log'

    uuid = Column(String, primary_key=True,default=lambda: str(uuid.uuid4()))
    log_message = Column(String)
    processid = Column(String)

class LogModel(BaseModel):
    uuid: str
    log_message: str
    processid: str

    class Config:
        orm_mode = True