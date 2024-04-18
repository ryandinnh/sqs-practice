import boto3
import requests
import json

sqs = boto3.client('sqs')

response = sqs.create_queue(
    QueueName='demo-queue',
    Attributes={
        'DelaySeconds': '5',
        'MessageRetentionPeriod': '86400'
    }
)

print(response['QueueUrl'])