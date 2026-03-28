from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ConversationForm, MessageForm, ThoughtForm
from .models import Conversation


def conversation_list(request):
    query = request.GET.get('q', '')
    conversations = Conversation.objects.all()

    if query:
        conversations = conversations.filter(
            Q(title__icontains=query) |
            Q(messages__text__icontains=query) |
            Q(messages__thoughts__text__icontains=query)
        ).distinct()

    return render(request, 'core/conversation_list.html', {
        'conversations': conversations,
        'query': query
    })


def conversation_create(request):
    if request.method == 'POST':
        form = ConversationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conversation_list')
    else:
        form = ConversationForm()

    return render(request, 'core/conversation_form.html', {'form': form})


def message_create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conversation_list')
    else:
        form = MessageForm()

    return render(request, 'core/message_form.html', {'form': form})


def thought_create(request):
    if request.method == 'POST':
        form = ThoughtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conversation_list')
    else:
        form = ThoughtForm()

    return render(request, 'core/thought_form.html', {'form': form})


def conversation_detail(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    message_query = request.GET.get('message_q', '')

    messages = conversation.messages.all().prefetch_related('thoughts')

    if message_query:
        messages = messages.filter(text__icontains=message_query)

    return render(request, 'core/conversation_detail.html', {
        'conversation': conversation,
        'messages': messages,
        'message_query': message_query
    })