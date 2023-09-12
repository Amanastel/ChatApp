from django.urls import path
from channels.routing import URLRouter
from chatapp.consumers import ChatConsumer

ws_application = URLRouter({
    path('ws/chat', ChatConsumer.as_asgi()),
    
})