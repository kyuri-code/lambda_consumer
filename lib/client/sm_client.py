import boto3

import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from lib.constant.config import REGION

class SMClient:

    def __init__(self):
        self.secrets_clinet = boto3.client('secretsmanager', region_name=REGION)
    
    def get_secrets(self,secret_id):
        try:
            get_secret_value_response = self.secrets_clinet.get_secret_value(SecretId=secret_id)
            secret = get_secret_value_response['SecretString']
            return json.loads(secret)
        except Exception as e:
            print(f"Failed to retrieve secrets: {e}")
            raise e