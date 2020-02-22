from django import forms

class ChatMessageForm(forms.Form):
    message = forms.CharField(label='Enter message', max_length=180)
