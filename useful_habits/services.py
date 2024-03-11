import os

import requests


# class MyBot:
#     URL = "https://api.telegram.org/bot"
#     TOKEN = os.getenv('TELEGRAM_TOKEN')
#
#     def send_message(self, text):
#         requests.post(
#             url=f'{self.URL}{self.TOKEN}/sendMessage',
#             data={
#                 'chat_id': os.getenv('TELEGRAM_ID'),
#                 'text': text
#             }
#         )


def send_telegram_message(chat_id, message):
    """data for sending  telegram_message to the user in telegram"""

    token = os.getenv('TELEGRAM_TOKEN')
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)

