import sys
sys.path.append('modules')

import json

import telegram

TELEGRAM_TOKEN = "TELEGRAM_TOKEN"

bot = telegram.Bot(TELEGRAM_TOKEN)

def handle(event, context):
    body = json.loads(event['body'])

    chat = body['message']['chat']
    chat_id = chat['id']
    text = body['message']['text']

    bot.sendMessage(chat_id, 'echo ' + text)

    return {'statusCode' : '200'}
