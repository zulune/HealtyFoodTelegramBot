import json
import telebot
import requests

from config import token
from authenticate import Auth

bot = telebot.TeleBot(token)


class Review:

    @staticmethod
    def get_review(message):
        url = 'http://185.25.117.22/api/review'

    @staticmethod
    def post_review(message):
        url = 'http://185.25.117.22/api/v2/review/'
        user = Auth.get_user(message.chat.id)
        headers = {'Content-Type': 'application/json',}
        data = {
            'user': user['id'],
            'text_review': message.text
        }
        r = requests.post(url, headers=headers, data=json.dumps(data))