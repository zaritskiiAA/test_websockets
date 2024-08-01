import json
from random import randint
from time import sleep
from pathlib import Path
from urllib.parse import urljoin

from channels.generic.websocket import WebsocketConsumer


class SendFileConsumer(WebsocketConsumer):

    def connect(self):
        print('CONNECT')
        self.accept()

    def receive(self, text_data=None, bytes_data=None):

        #имитируем работу воркера
        for idx in range(5, -1, -1):
            self.send(json.dumps({'message': f'Имитируем ожидание работы воркера {idx}'}))
            sleep(1)

        file_path = Path(__file__).resolve().parent.parent / 'media' / f'{text_data}.txt'
        with open(file_path, 'w') as file:

            file.write(text_data)
        # Имитируем ссылку с видео на я.диск
        result = urljoin('http://localhost:8000', f'media/{text_data}.txt')
        ans = json.dumps({'message': f'Ссылка на ресурс: {result}'})
        self.send(ans)
