from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

from src.client.sm_client import SMClient

SECRET_ID = os.environ['SECRET_ID']
DBNAME = 'sample_db'

Base = declarative_base()

class DBClient:
    def __init__(self):
        self.connection = None
        self.engine = None
        self.Session = None
    
    def connect(self):
        db_config = SMClient.get_secrets(SECRET_ID)
        db_url = f"postgresql+psycopg2://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{DBNAME}"
        self.engine = create_engine(db_url,echo=False)
        self.Session = sessionmaker(bind=self.engine)
        print("Connected to the database")
    
    def disconnect(self):
        if self.engine:
            self.engine.dispose()
            print("Disconnected from the database")