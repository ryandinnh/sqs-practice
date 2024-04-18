import boto3
import requests
import json

sqs = boto3.client('sqs')

url = 'https://sqs.us-east-1.amazonaws.com/471112568835/myqueue'

response = sqs.get_queue_attributes(
    QueueUrl= url,
    AttributeNames = [
        'All'
    ]
)

print(response)
