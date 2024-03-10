import os

import requests


class MyBot:
    URL = "https://api.telegram.org/bot"
    TOKEN = os.getenv('TELEGRAM_TOKEN')

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': os.getenv('TELEGRAM_ID'),
                'text': text
            }
        )
