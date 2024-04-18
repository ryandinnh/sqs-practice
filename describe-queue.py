import boto3
import requests
import json

sqs = boto3.client('sqs')

response = sqs.get_queue_attributes(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/440848399208/demo-queue',
    AttributeNames=[
        'All'
    ]
)

print(json.dumps(response, indent=2, default=str))