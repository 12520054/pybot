from flask import Flask, request
from pymessenger.bot import Bot

from GamePlay import GamePlay
from GameModels.PlayerData import PlayerData
app = Flask(__name__)
pyBot = GamePlay()

ACCESS_TOKEN = 'EAAEgy21czGwBAFp51ZCCiO1ZBJEPIGB2ICZAkNxUWBYZBDZA0IXgzzZBTsATlY6WOToywU6ivvq5vb3frBLRGTgjNZAEDLNQDn2DQlZBq19ZC7dHDQKHrJ5KGKZCiFoernZCQtEgupnt6S4XAelJbZBA79uX28cnoigYEsCV7Tlb489QUQZDZD'
VERIFY_TOKEN = 'Danhth'

bot = Bot(ACCESS_TOKEN)

@app.route('/webhook', methods=['GET'])
def handle_verification():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    else:
        return "Invalid verification token"
    return

@app.route('/webhook', methods=['POST'])
def handle_incoming_message():
    data = request.json
    print(data)
    for event in data['entry']:
        messaging = event['messaging']
        for x in messaging:
            if x.get('message') and x['message'].get('text'):
                message = x['message']['text']
                recipient_id = x['sender']['id']
                print('server received msg: ' + message)
                return_msg = pyBot.processUserMessage(recipient_id, message)
                bot.send_text_message(recipient_id, return_msg)
                print('server return msg: ' + return_msg)
            else:
                pass
    return "ok", 200

if __name__ == '__main__':
    app.run()