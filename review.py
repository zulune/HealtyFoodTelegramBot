import json
import telebot
import requests

from config import token
from authenticate import Auth

bot = telebot.TeleBot(token)


class Review:

    def get_review(message):
        url = 'http://localhost:8000/api/review'

    def post_review(message):
        url = 'http://localhost:8000/api/v2/review/'
        user = Auth.get_user(message.chat.id)
        headers = {'Content-Type': 'application/json',}
        data = {
            'user': user['id'],
            'text_review': message.text
        }
        r = requests.post(url, headers=headers, data=json.dumps(data))