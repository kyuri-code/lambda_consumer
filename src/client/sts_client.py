import boto3

class STSClient:
    def get_account_id():
        return boto3.client('sts').get_caller_identity()['Account']