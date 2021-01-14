import boto3
import json
from boto3_type_annotations.sqs import ServiceResource, Queue, Message

DATA_QUEUE_REGION = 'us-east-1'

sqs = boto3.resource('sqs',DATA_QUEUE_REGION)
queue = sqs.get_queue_by_name(QueueName='test_status_queue.fifo')
status_message = {
        'uuid': 7266,
        'title': 'Needs Validation',
        'description': 'file processed',
        'status': 'needs_validation',
    }
response = queue.send_message(
    MessageBody=json.dumps(status_message),
    MessageGroupId='test_status'
)

prit("new thing")
print(response)