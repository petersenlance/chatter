from django.shortcuts import render
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')

def hello(request):
    """My first view"""
    table = dynamodb.Table('Chat')

    print(table.creation_date_time)

    table.put_item(
        Item={
            'chatId': 'general',
            'chatGroupId': 'first',
            'message': 'Hello World 2!'
        }
    )
    return render(request, 'stuff/hello.html', {'name': 'different thing'})
