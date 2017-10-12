import sys
sys.path.append('modules')

import json

import telegram
import flickrapi

TELEGRAM_TOKEN = "YOUR_TELEGRAM_TOKEN"
FLICKR_API_KEY = "YOUR_FLICKR_API_KEY"
FLICKR_API_SECRET = "YOUR_FLICKR_API_SECRET"

bot = telegram.Bot(TELEGRAM_TOKEN)
flickr = flickrapi.FlickrAPI(FLICKR_API_KEY,FLICKR_API_SECRET, format='parsed-json', store_token=False)

def handle(event, context):
    body = json.loads(event['body'])

    chat = body['message']['chat']
    chat_id = chat['id']
    text = body['message']['text']

    sets = flickr.interestingness.getList()
    for photo in sets['photos']['photo'][0:5]:
        image_url = "https://farm%s.staticflickr.com/%s/%s_%s_m.jpg" % (photo['farm'], photo['server'], photo['id'], photo['secret'])
        # print(image_url)
        url = "https://www.flickr.com/photos/%s/%s" % (photo['owner'], photo['id'])
        caption = "[%s] %s\n%s" % (text, photo['title'], url)
        bot.sendPhoto(chat_id=chat_id, photo=image_url, caption=caption)

    return {'statusCode' : '200'}
