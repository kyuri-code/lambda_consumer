from sqlalchemy import Column, String
from src.db_client.db_client import Base
import uuid

class Message(Base):
    __tablename__ = 'sample_message'

    uuid = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    message = Column(String)
    processid = Column(String)