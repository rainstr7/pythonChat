import time
from datetime import datetime

import requests


def print_message(message):
    dt = datetime.fromtimestamp(message['time'])
    print(dt.strftime('%H:%M:%S'), message['name'])
    print(message['text'])
    print()


after = 0

while True:
    response = requests.get(
        'http://127.0.0.1:5000/messages',
        params={'after': after}
    )

    # [{'name': '123', ...}, ...]
    messages = response.json()['messages']

    if messages:
        for message in messages:
            print_message(message)

        after = messages[-1]['time']

    time.sleep(1)
