import boto3
import requests
import json

sqs = boto3.client('sqs')

response = sqs.receive_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/440848399208/demo-queue',
    AttributeNames=[
        'All'
    ]
)
print(response)
handle = response['Messages'][0]['ReceiptHandle']

response2 = sqs.delete_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/440848399208/demo-queue',
    ReceiptHandle=handle
)
print(response2)