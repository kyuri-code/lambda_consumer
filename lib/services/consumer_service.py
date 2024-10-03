from sqlalchemy.orm import Session

import uuid
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib.models.log_model import Log
from lib.models.message_model import Message
from lib.db_client.db_client import DBClient
from lib.client.sqs_client import SQSClient

class ConsumerService:
    def __init__(self):
        self.db_client = DBClient()
        self.sqs_client = SQSClient()
        self.db_client.connect()
    
    def process(self, record):
        session: Session = self.db_client.Session()
        start_uuid = str(uuid.uuid4())
        end_uuid = str(uuid.uuid4())

        try:
            body = json.loads(record['body'])
            message = body.get('message')
            process_id = body.get('process_id')

            # 開始ログをDBに追加
            start_log = Log(uuid=start_uuid, log_message='Consumer process started', processid=process_id)
            session.add(start_log)
            session.commit()

            # メッセージをDBに保存
            new_message = Message(uuid=str(uuid.uuid4()), message=message, processid=process_id)
            session.add(new_message)
            session.commit()
            
            # 終了ログをDBに追加
            end_log = Log(uuid=end_uuid, log_message='Consumer process ended', processid=process_id)
            session.add(end_log)
            session.commit()
        
        except Exception as e:
            session.rollback()
            print(f"Error in producer process: {e}")

        finally:
            session.close()
            self.db_client.disconnect()