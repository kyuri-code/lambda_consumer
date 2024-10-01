import boto3
import json
from src.client.sts_client import STSClient 
from src.constant.config import REGION

QUEUE_NAME = 'td-nt-iac-lambda-pc.fifo'

class SQSClient:
    def __init__(self):
        self.sqs_client = boto3.client('sqs', region_name = REGION)
        account_id = self.get_account_id()
        self.queue_url = f"https://sqs.{REGION}.amazonaws.com/{account_id}/{QUEUE_NAME}"

    def send_message(self, message, process_id):
        try:
            response = self.sqs_client.send_message(
                QueueUrl=self.queue_url,
                MessageBody=json.dumps({
                    'message': message,
                    'process_id': process_id
                })
            )
            print(f"Message sent to SQS: {response.get('MessageId')}")
        except Exception as e:
            print(f"Error sending message to SQS: {e}")
            raise e
        
    def get_account_id():
        return STSClient.get_account_id()