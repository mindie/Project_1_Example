import boto3

sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/618573814374/dev-serverless-api-google-ads-connector-queue'

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=("{\"accounts\": [3036115467414, 341156790566843], \"brand_id\": 379, \"brand_ids\": [379], \"user_uploaded\": \"mindie.brockwell@keends.com\", \"connector_id\": 140,\"end_date\": \"2019-01-01\",\"file_name\": \"Facebook Lambda Test\",\"region\": \"us-east-1\",\"start_date\": \"2018-01-01\"}")
)


print(response)