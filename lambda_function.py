from src.services.consumer_service import ConsumerService

def lambda_hander(event, context):
    consumer_service = ConsumerService()
    for record in event['Records']:
        consumer_service.process(record)

    return {
        'statusCode': 200,
        'body': 'Consumer process completed successfully'
    }