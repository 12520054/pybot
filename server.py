from flask import Flask, request
from GamePlay import GamePlay
import os
import sys
import json
import requests
import unicodedata

app = Flask(__name__)
pyBot = GamePlay()

ACCESS_TOKEN = 'EAAEgy21czGwBAJX2S8pSZAtc8PM0TElqZCtUX1Nhlo4EvdZAKsVQCgcC2mrqIPfwsHJ3Qw2Ws0ZBCij0G1URdh7e9JZCWvsvPdZBMpDxhXNXvxLMsKZBQ8CAPGbzhyNJwlTHRn65tDSZC6WHZA2SZCf7lSWMOVyZAZBCZCsO9U3J3qJukfwZDZD'
VERIFY_TOKEN = 'Danhth'


@app.route('/webhook', methods=['GET'])
def handle_verification():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    else:
        return "Invalid verification token"


@app.route('/webhook', methods=['POST'])
def handle_incoming_message():
    data = request.json
    for event in data['entry']:
        messaging = event['messaging']
        for x in messaging:
            if x.get('message') and x['message'].get('text'):
                message = x['message']['text']
                recipient_id = x['sender']['id']
                print(message)
                return_msg = pyBot.processUserMessage(recipient_id, message)
                print(return_msg)
                send_message(recipient_id, return_msg)
            else:
                pass
    return "ok", 200


def send_message(recipient_id, message_text):
    params = {
        "access_token": ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    pass

exec(open("create_default_scene.py").read(), globals())
exec(open("create_item_factory.py").read(), globals())

if __name__ == '__main__':
    #app.run('0.0.0.0', 8080)
    app.run()
