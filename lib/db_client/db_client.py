from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib.client.sm_client import SMClient

SECRET_ID = os.environ['SECRET_ID']
DBNAME = 'sample_db'

Base = declarative_base()

class DBClient:
    def __init__(self):
        self.connection = None
        self.engine = None
        self.Session = None
        self.sm_client = SMClient()
    
    def connect(self):
        db_config = self.sm_client.get_secrets(SECRET_ID)
        db_url = f"postgresql+psycopg2://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{DBNAME}"
        self.engine = create_engine(db_url,echo=False)
        self.Session = sessionmaker(bind=self.engine)
        print("Connected to the database")
    
    def disconnect(self):
        if self.engine:
            self.engine.dispose()
            print("Disconnected from the database")