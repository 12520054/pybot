from flask import Flask, request
from GamePlay import GamePlay
import os
import sys
import json
import requests
import unicodedata

app = Flask(__name__)
pyBot = GamePlay()

ACCESS_TOKEN = 'EAAEgy21czGwBAGbcCOx2O2ZBn1WOMjdLi53FusjF2jILRhLNZBbW3vsaQXqa9Ne4tLqwtXg8A3kJorL9BKUU1STCC3rfZAmii5Wo9ZBsve2rryvH2gjTa5Tu0yeYcy6ODPE83GGZByMjGvYO3nkgypF9QZB5u0rmUWXHKQ54aYdgZDZD'
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

                #print('server received msg: ' + message)
                return_msg = pyBot.processUserMessage(recipient_id, message)
                send_message(recipient_id, return_msg)
                #print('server return msg: ' + return_msg)
            else:
                pass
    return "ok", 200


def send_message(recipient_id, message_text):

    #log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

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
    #if r.status_code != 200:
        #log(r.status_code)
        #log(r.text)


#def log(message):  # simple wrapper for logging to stdout on heroku
    #print(str(message))

exec(open("create_default_scene.py").read(), globals())
exec(open("create_item_factory.py").read(), globals())

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
    #app.run()
