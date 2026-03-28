from django.urls import path
from . import views

urlpatterns = [
    path('', views.conversation_list, name='conversation_list'),
    path('conversations/new/', views.conversation_create, name='conversation_create'),
    path('messages/new/', views.message_create, name='message_create'),
    path('thoughts/new/', views.thought_create, name='thought_create'),
    path('conversations/<int:conversation_id>/', views.conversation_detail, name='conversation_detail'),
]