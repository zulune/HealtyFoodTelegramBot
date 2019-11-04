import json
import telebot
import requests

from config import token
from authenticate import Auth

bot = telebot.TeleBot(token)


class Telephone:

    def set_phone(value):
        url = url = 'http://185.25.117.22/api/v2/user/{}/'
        end_url = url.format(value.chat.id)
        phone = value.contact.telephone
        headers = {'Content-Type': 'application/json',}
        data = {
            'client': {
                'phone': phone
            }
        }
        r = requests.post(url, headers=headers, data=json.dumps(data))