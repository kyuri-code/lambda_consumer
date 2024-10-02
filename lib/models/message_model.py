from sqlalchemy import Column, String

import uuid
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from lib.db_client.db_client import Base

class Message(Base):
    __tablename__ = 'sample_message'

    uuid = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    message = Column(String)
    processid = Column(String)