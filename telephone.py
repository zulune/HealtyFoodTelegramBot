import json
import telebot
import requests

from config import token
from authenticate import Auth

bot = telebot.TeleBot(token)


class Telephone:

    @staticmethod
    def set_phone(value):
        url = url = 'http://185.25.117.22/api/v2/user/{}/'
        end_url = url.format(value.chat.id)
        phone = value.contact.phone_number
        headers = {'Content-Type': 'application/json', }
        data = Auth.get_user(value.chat.id)
        data['client']['phone'] = phone
        r = requests.put(end_url, headers=headers, data=json.dumps(data))
        print(r.status_code)
        print(r.text)
