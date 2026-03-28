from django import forms
from .models import Conversation, Message, Thought


class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ['title', 'start_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['conversation', 'text', 'sent_at']
        widgets = {
            'sent_at': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }


class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['message', 'text', 'sent_at']
        widgets = {
            'sent_at': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }