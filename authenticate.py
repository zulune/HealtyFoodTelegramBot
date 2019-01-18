import json
import telebot
import requests

from utils import username_generator, password_generator

from config import token

bot = telebot.TeleBot(token)


class Auth:

    def check_user(message):
        url = 'http://localhost:8000/api/v2/user/{}/'
        r = requests.get(url.format(message.chat.id))
        if r.status_code == requests.codes.ok:
            return True
        return False

    def validate_username(username):
        return False

    def create_user(message):
        url = 'http://localhost:8000/api/v2/user/'
        username = None
        first_name = message.chat.first_name
        last_name = message.chat.last_name
        chat_id = message.chat.id
        if first_name is None:
            first_name = 'John'
        if last_name is None:
            last_name = 'Doe'

        if username is None:
            username = first_name.lower() + last_name.lower()
            check_username = Auth.validate_username(username)
            if check_username:
                username = username_generator(first_name=first_name, last_name=last_name)
        gen_password = password_generator()
        headers = {'Content-Type': 'application/json',}
        data = {
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'password': gen_password,
            'telegram': chat_id,
            'client': {
                'telegram_id': chat_id,
                'phone': ''
            }
        }
        r = requests.post(url, headers=headers, data=json.dumps(data))
    