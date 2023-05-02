from django.urls import re_path, path

from ChatGPT.consumer import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat_gpt/', ChatConsumer.as_asgi()),
]