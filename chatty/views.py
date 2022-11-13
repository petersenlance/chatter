import boto3
import uuid
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from boto3.dynamodb.conditions import Key, Attr
from .forms import ChatMessageForm

dynamodb = boto3.resource('dynamodb')

def hello(request):
    """My first view"""
    chat_db = dynamodb.Table('Chat')

    chat_db.put_item(
        Item={
            'chat_id': 'general',
            'sort_key': 'user_id_1',
            'user_name': 'only one',
            'message': 'Hello World 2!'
        }
    )
    return render(request, 'hello.html', {'name': 'new locations'})

def chat(request):
    chat_db = dynamodb.Table('Chat')
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            now = datetime.now()
            id = uuid.uuid4()
            chat_db.put_item(
                Item={
                    'chat_id': 'general',
                    'sort_key': f'message_{now}_{id}',
                    'user_name': 'only one',
                    'message': form.cleaned_data['message']
                }
            )
            return HttpResponseRedirect('/chat/')

    else:
        response = chat_db.query(
            KeyConditionExpression=Key('chat_id').eq('general')
        )

        form = ChatMessageForm()
        data = {'name': 'new route', 'messages': response['Items'], 'form': form}

        return render(request, 'chat.html', data)
