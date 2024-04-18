import boto3
import requests
import json

sqs = boto3.client('sqs')

id = requests.get('https://ids.pods.uvarc.io').json().get('id')

response = sqs.send_message(
    QueueUrl= 'https://sqs.us-east-1.amazonaws.com/471112568835/myqueue',
    MessageBody = id,
    MessageAttributes={
        'Project' : {
            'StringValue' : 'Project X',
            'DataType' : 'String'
        },
        'Flavor' : {
            'StringValue' : 'Mint Chocolate Chip',
            'DataType' : 'String'
        }
    }
)

print(response)