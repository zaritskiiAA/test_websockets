import json

from channels.generic.websocket import WebsocketConsumer


class SendFileConsumer(WebsocketConsumer):

    def connect(self):
        print('CONNECT')
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("Receive")
        print(text_data)
