import boto3
import requests
import json

sqs = boto3.client('sqs')

id = requests.get('http://ids.pods.uvarc.io/').json()['id']

response = sqs.send_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/440848399208/demo-queue',
    MessageBody=id,
    MessageAttributes={
        'Flavor': {
            'StringValue': 'Vanilla',
            'DataType': 'String'
        }
    }
)

print(response)