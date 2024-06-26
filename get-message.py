import boto3
import requests
import json

sqs = boto3.client('sqs')

url = 'https://sqs.us-east-1.amazonaws.com/471112568835/myqueue'

def deleteMsg(handle):
    delete = sqs.delete_message(
        QueueUrl = url,
        ReceiptHandle = response['Messages'][0]['ReceiptHandle']
    )

response = sqs.receive_message(
    QueueUrl= url,
    AttributeNames = [
        'All'
    ]
)

print(response)
deleteMsg(handle)

