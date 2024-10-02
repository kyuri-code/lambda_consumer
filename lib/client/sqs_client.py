import boto3

import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib.client.sts_client import STSClient 
from lib.constant.config import REGION

QUEUE_NAME = 'td-nt-iac-lambda-pc-producer-queue.fifo'

class SQSClient:
    def __init__(self):
        self.sts_client = STSClient()
        self.sqs_client = boto3.client('sqs', region_name = REGION)
        account_id = self.get_account_id()
        self.queue_url = f"https://sqs.{REGION}.amazonaws.com/{account_id}/{QUEUE_NAME}"

    def get_account_id(self):
        return self.sts_client.get_account_id()