from django.shortcuts import render
import boto3

dynamodb = boto3.resource('dynamodb')

def hello(request):
    """My first view"""
    table = dynamodb.Table('Chat')
    print(table.creation_date_time)
    return render(request, 'stuff/hello.html', {'name': 'ellie'})
