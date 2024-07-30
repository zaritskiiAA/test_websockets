from django.urls import path

from .consumers import SendFileConsumer


ws_urlpatterns = [
    path('ws/send_file/', SendFileConsumer.as_asgi()),
]