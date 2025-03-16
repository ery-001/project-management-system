from django.urls import path
from .consumers import TaskConsumer

websocket_urlpatterns = [
    path("ws/tasks/", TaskConsumer.as_asgi()),
]
